import random
from datetime import date

from aiogram import Bot
from aiogram.exceptions import TelegramForbiddenError, TelegramBadRequest
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

import database as db
from config import REMINDER_HOURS_UTC, DAILY_GOAL
from keyboards import main_menu_kb

NAG_MESSAGES = [
    "👋 Привет! Пара минут — и ты станешь чуточку ближе к свободному немецкому. Заглянешь?",
    "🧠 Мозг забывает новое уже через несколько часов. Повтори слова, пока не поздно!",
    "📚 Твои карточки заскучали без тебя. Загляни, разомнись немного 🇩🇪",
    "⏳ Всего 5 минут в день — и через месяц ты не узнаешь свой немецкий. Начни сейчас!",
    "🎯 Маленький шаг сегодня = большой словарный запас завтра. Погнали?",
    "😴 Слова не выучатся сами. Загляни на минутку!",
    "🔥 Не дай своему прогрессу остыть — повтори пару карточек прямо сейчас.",
    "💬 Как сказать это по-немецки? Проверь себя — открой бота!",
]

STREAK_RISK_MESSAGES = [
    "🔥⚠️ Твой streak в {streak} дней под угрозой! Позанимайся пару минут, чтобы не потерять его.",
    "⏰ Ещё чуть-чуть — и streak в {streak} дней сгорит. Не дай этому случиться!",
    "🚨 Streak {streak} дней ещё жив, но ненадолго. Спаси его прямо сейчас!",
]

ZERO_STREAK_MESSAGES = [
    "🌱 Начни новый streak прямо сегодня — первый шаг всегда самый важный!",
    "💪 Готов начать заново? Учить язык маленькими шагами — лучшая стратегия.",
]


def build_reminder_text(user: dict) -> str:
    streak = user["streak"]
    if streak >= 2:
        return random.choice(STREAK_RISK_MESSAGES).format(streak=streak)
    if streak == 0:
        return random.choice(ZERO_STREAK_MESSAGES)
    return random.choice(NAG_MESSAGES)


async def send_reminders(bot: Bot):
    users = await db.get_users_for_reminder()
    today = date.today()
    for u in users:
        goal_met = u["last_study_date"] == today and u["words_today"] >= DAILY_GOAL
        if goal_met:
            continue  # цель дня выполнена — не докучаем
        text = build_reminder_text(u)
        try:
            await bot.send_message(u["user_id"], text, reply_markup=main_menu_kb())
        except (TelegramForbiddenError, TelegramBadRequest):
            # юзер заблокировал бота — отключаем напоминания, чтобы не долбить в пустоту
            await db.set_reminders(u["user_id"], False)
        except Exception:
            pass


def setup_scheduler(bot: Bot) -> AsyncIOScheduler:
    scheduler = AsyncIOScheduler(timezone="UTC")
    for hour in REMINDER_HOURS_UTC:
        scheduler.add_job(
            send_reminders,
            trigger=CronTrigger(hour=hour, minute=0),
            args=[bot],
            id=f"reminder_{hour}",
            replace_existing=True,
        )
    return scheduler
