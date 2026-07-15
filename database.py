import asyncpg
from datetime import datetime, timedelta, date

from config import DATABASE_URL

pool: asyncpg.Pool | None = None

ALL_LEVELS = ["A1", "A2", "B1", "B2"]

# Интервалы для системы Лейтнера (box -> через сколько показать снова)
BOX_INTERVALS = {
    0: timedelta(minutes=0),
    1: timedelta(hours=1),
    2: timedelta(hours=8),
    3: timedelta(days=1),
    4: timedelta(days=3),
    5: timedelta(days=7),
    6: timedelta(days=16),
    7: timedelta(days=35),
}
MAX_BOX = 7


async def init_pool():
    global pool
    pool = await asyncpg.create_pool(DATABASE_URL, min_size=1, max_size=10)
    await create_schema()


async def create_schema():
    async with pool.acquire() as con:
        await con.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id BIGINT PRIMARY KEY,
            username TEXT,
            first_name TEXT,
            level TEXT DEFAULT 'A1',
            xp INT DEFAULT 0,
            streak INT DEFAULT 0,
            longest_streak INT DEFAULT 0,
            last_study_date DATE,
            words_today INT DEFAULT 0,
            reminders_enabled BOOLEAN DEFAULT TRUE,
            created_at TIMESTAMP DEFAULT now()
        );

        CREATE TABLE IF NOT EXISTS words (
            id SERIAL PRIMARY KEY,
            de TEXT NOT NULL,
            ru TEXT NOT NULL,
            level TEXT NOT NULL,
            category TEXT NOT NULL,
            pos TEXT
        );

        CREATE TABLE IF NOT EXISTS progress (
            user_id BIGINT REFERENCES users(user_id) ON DELETE CASCADE,
            word_id INT REFERENCES words(id) ON DELETE CASCADE,
            box INT DEFAULT 0,
            correct INT DEFAULT 0,
            wrong INT DEFAULT 0,
            next_review TIMESTAMP DEFAULT now(),
            last_seen TIMESTAMP,
            PRIMARY KEY (user_id, word_id)
        );

        CREATE TABLE IF NOT EXISTS game_stats (
            user_id BIGINT REFERENCES users(user_id) ON DELETE CASCADE,
            game_type TEXT,
            played INT DEFAULT 0,
            best_score INT DEFAULT 0,
            PRIMARY KEY (user_id, game_type)
        );

        CREATE INDEX IF NOT EXISTS idx_progress_next_review ON progress(user_id, next_review);
        CREATE INDEX IF NOT EXISTS idx_words_level ON words(level);
        """)

        # ---- Миграция: мульти-уровни вместо одного уровня + флаг онбординга ----
        # onboarded по умолчанию TRUE — это применится к уже существующим строкам
        # (они уже проходили выбор уровня раньше). Новых юзеров создаём с onboarded=FALSE явно.
        await con.execute("""
            ALTER TABLE users ADD COLUMN IF NOT EXISTS levels TEXT[] DEFAULT ARRAY['A1','A2','B1','B2'];
            ALTER TABLE users ADD COLUMN IF NOT EXISTS onboarded BOOLEAN DEFAULT TRUE;
        """)
        # для старых строк, где levels мог остаться NULL/пустым — переносим старый level в массив
        await con.execute("""
            UPDATE users SET levels = ARRAY[level]
            WHERE (levels IS NULL OR array_length(levels, 1) IS NULL) AND level IS NOT NULL;
        """)


async def seed_words(word_list: list[dict]):
    async with pool.acquire() as con:
        count = await con.fetchval("SELECT count(*) FROM words")
        if count and count > 0:
            return count
        await con.executemany(
            "INSERT INTO words (de, ru, level, category, pos) VALUES ($1,$2,$3,$4,$5)",
            [(w["de"], w["ru"], w["level"], w["category"], w.get("pos", "")) for w in word_list],
        )
        return await con.fetchval("SELECT count(*) FROM words")


async def get_or_create_user(user_id: int, username: str, first_name: str):
    async with pool.acquire() as con:
        user = await con.fetchrow("SELECT * FROM users WHERE user_id=$1", user_id)
        if user:
            return dict(user)
        await con.execute(
            """INSERT INTO users (user_id, username, first_name, levels, onboarded)
               VALUES ($1,$2,$3,$4,FALSE)""",
            user_id, username, first_name, ["A2", "B1"],
        )
        user = await con.fetchrow("SELECT * FROM users WHERE user_id=$1", user_id)
        return dict(user)


async def toggle_level(user_id: int, level: str) -> list[str]:
    """Переключает уровень в мультивыборе юзера. Не даёт снять последний оставшийся уровень."""
    async with pool.acquire() as con:
        user = await con.fetchrow("SELECT levels FROM users WHERE user_id=$1", user_id)
        levels = list(user["levels"] or [])
        if level in levels:
            if len(levels) > 1:
                levels.remove(level)
        else:
            levels.append(level)
        await con.execute("UPDATE users SET levels=$1 WHERE user_id=$2", levels, user_id)
        return levels


async def set_onboarded(user_id: int):
    async with pool.acquire() as con:
        await con.execute("UPDATE users SET onboarded=TRUE WHERE user_id=$1", user_id)


async def get_user(user_id: int):
    async with pool.acquire() as con:
        row = await con.fetchrow("SELECT * FROM users WHERE user_id=$1", user_id)
        return dict(row) if row else None


async def touch_streak(user_id: int):
    """Обновляет streak и xp при завершении дневной активности (вызывается при каждом правильном ответе)."""
    async with pool.acquire() as con:
        user = await con.fetchrow("SELECT * FROM users WHERE user_id=$1", user_id)
        today = date.today()
        last = user["last_study_date"]
        words_today = user["words_today"]

        if last == today:
            words_today += 1
            new_streak = user["streak"]
        else:
            words_today = 1
            if last == today - timedelta(days=1):
                new_streak = user["streak"] + 1
            else:
                new_streak = 1

        longest = max(user["longest_streak"], new_streak)
        await con.execute(
            """UPDATE users SET last_study_date=$1, words_today=$2, streak=$3,
               longest_streak=$4, xp = xp + 2 WHERE user_id=$5""",
            today, words_today, new_streak, longest, user_id,
        )
        return words_today, new_streak


async def get_due_words(user_id: int, levels: list[str], limit: int = 10):
    """Слова к повторению по выбранным юзером уровням: сначала новые, потом просроченные по Лейтнеру."""
    if not levels:
        levels = ALL_LEVELS
    async with pool.acquire() as con:
        rows = await con.fetch(
            """
            SELECT w.* FROM words w
            LEFT JOIN progress p ON p.word_id = w.id AND p.user_id = $1
            WHERE w.level = ANY($2::text[]) AND p.word_id IS NULL
            ORDER BY random() LIMIT $3
            """,
            user_id, levels, limit,
        )
        new_words = [dict(r) for r in rows]
        if len(new_words) >= limit:
            return new_words

        remaining = limit - len(new_words)
        rows2 = await con.fetch(
            """
            SELECT w.*, p.box FROM words w
            JOIN progress p ON p.word_id = w.id AND p.user_id = $1
            WHERE p.next_review <= now() AND w.level = ANY($2::text[])
            ORDER BY p.next_review ASC LIMIT $3
            """,
            user_id, levels, remaining,
        )
        return new_words + [dict(r) for r in rows2]


async def get_random_words(levels: list[str], exclude_id: int, n: int = 3):
    if not levels:
        levels = ALL_LEVELS
    async with pool.acquire() as con:
        rows = await con.fetch(
            "SELECT * FROM words WHERE level = ANY($1::text[]) AND id != $2 ORDER BY random() LIMIT $3",
            levels, exclude_id, n,
        )
        return [dict(r) for r in rows]


async def record_answer(user_id: int, word_id: int, correct: bool):
    async with pool.acquire() as con:
        row = await con.fetchrow(
            "SELECT * FROM progress WHERE user_id=$1 AND word_id=$2", user_id, word_id
        )
        if row is None:
            box = 1 if correct else 0
            next_review = datetime.utcnow() + BOX_INTERVALS[box]
            await con.execute(
                """INSERT INTO progress (user_id, word_id, box, correct, wrong, next_review, last_seen)
                   VALUES ($1,$2,$3,$4,$5,$6, now())""",
                user_id, word_id, box, 1 if correct else 0, 0 if correct else 1, next_review,
            )
        else:
            box = row["box"]
            if correct:
                box = min(box + 1, MAX_BOX)
            else:
                box = max(box - 2, 0)
            next_review = datetime.utcnow() + BOX_INTERVALS[box]
            await con.execute(
                """UPDATE progress SET box=$1, correct = correct + $2, wrong = wrong + $3,
                   next_review=$4, last_seen=now() WHERE user_id=$5 AND word_id=$6""",
                box, 1 if correct else 0, 0 if correct else 1, next_review, user_id, word_id,
            )
    await touch_streak(user_id)


async def get_stats(user_id: int):
    async with pool.acquire() as con:
        user = await con.fetchrow("SELECT * FROM users WHERE user_id=$1", user_id)
        levels = user["levels"] or ALL_LEVELS
        known = await con.fetchval(
            """SELECT count(*) FROM progress p JOIN words w ON w.id = p.word_id
               WHERE p.user_id=$1 AND p.box >= 4 AND w.level = ANY($2::text[])""",
            user_id, levels,
        )
        learning = await con.fetchval(
            """SELECT count(*) FROM progress p JOIN words w ON w.id = p.word_id
               WHERE p.user_id=$1 AND p.box < 4 AND w.level = ANY($2::text[])""",
            user_id, levels,
        )
        total_words = await con.fetchval(
            "SELECT count(*) FROM words WHERE level = ANY($1::text[])", levels
        )
        due_now = await con.fetchval(
            """SELECT count(*) FROM progress p JOIN words w ON w.id = p.word_id
               WHERE p.user_id=$1 AND p.next_review <= now() AND w.level = ANY($2::text[])""",
            user_id, levels,
        )
        return {
            "user": dict(user),
            "known": known,
            "learning": learning,
            "total_words": total_words,
            "due_now": due_now,
        }


async def update_game_score(user_id: int, game_type: str, score: int):
    async with pool.acquire() as con:
        row = await con.fetchrow(
            "SELECT * FROM game_stats WHERE user_id=$1 AND game_type=$2", user_id, game_type
        )
        if row is None:
            await con.execute(
                "INSERT INTO game_stats (user_id, game_type, played, best_score) VALUES ($1,$2,1,$3)",
                user_id, game_type, score,
            )
        else:
            best = max(row["best_score"], score)
            await con.execute(
                "UPDATE game_stats SET played = played + 1, best_score=$1 WHERE user_id=$2 AND game_type=$3",
                best, user_id, game_type,
            )


async def set_reminders(user_id: int, enabled: bool):
    async with pool.acquire() as con:
        await con.execute("UPDATE users SET reminders_enabled=$1 WHERE user_id=$2", enabled, user_id)


async def get_users_for_reminder():
    """Юзеры у кого включены напоминания и они ещё не выполнили дневную цель сегодня."""
    async with pool.acquire() as con:
        rows = await con.fetch(
            """SELECT user_id, first_name, streak, words_today, last_study_date
               FROM users WHERE reminders_enabled = TRUE AND onboarded = TRUE"""
        )
        return [dict(r) for r in rows]


async def record_answer_and_stats(user_id: int, word_id: int, correct: bool) -> dict:
    """Как record_answer, но сразу возвращает свежие xp/streak/known — удобно для мини-аппа."""
    await record_answer(user_id, word_id, correct)
    user = await get_user(user_id)
    async with pool.acquire() as con:
        known = await con.fetchval(
            """SELECT count(*) FROM progress p JOIN words w ON w.id = p.word_id
               WHERE p.user_id=$1 AND p.box >= 4 AND w.level = ANY($2::text[])""",
            user_id, user["levels"] or ALL_LEVELS,
        )
    return {
        "xp": user["xp"],
        "streak": user["streak"],
        "words_today": user["words_today"],
        "known": known,
    }
