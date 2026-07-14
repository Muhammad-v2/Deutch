// ===================== Telegram WebApp init =====================
const tg = window.Telegram?.WebApp;
if (tg) {
  tg.ready();
  tg.expand();
  try { tg.setHeaderColor("#12151B"); } catch (e) {}
  try { tg.setBackgroundColor("#12151B"); } catch (e) {}
}
const INIT_DATA = tg?.initData || "";

// ===================== API helper =====================
async function api(path, options = {}) {
  const res = await fetch(path, {
    ...options,
    headers: {
      "Content-Type": "application/json",
      "X-Telegram-Init-Data": INIT_DATA,
      ...(options.headers || {}),
    },
  });
  if (!res.ok) throw new Error(`API ${path} failed: ${res.status}`);
  return res.json();
}

function haptic(type = "light") {
  try {
    if (type === "success") tg.HapticFeedback.notificationOccurred("success");
    else if (type === "error") tg.HapticFeedback.notificationOccurred("error");
    else tg.HapticFeedback.impactOccurred(type);
  } catch (e) {}
}

// ===================== State =====================
const state = { me: null };
const root = document.getElementById("screen-root");
const navButtons = document.querySelectorAll(".nav-btn");

navButtons.forEach((btn) => {
  btn.addEventListener("click", () => {
    setActiveNav(btn.dataset.screen);
    if (btn.dataset.screen === "home") renderHome();
    if (btn.dataset.screen === "profile") renderProfile();
  });
});

function setActiveNav(screen) {
  navButtons.forEach((b) => b.classList.toggle("active", b.dataset.screen === screen));
}

function showLoader() {
  root.innerHTML = `<div class="loader"><span></span><span></span><span></span></div>`;
}

// ===================== Split-flap number =====================
function flapRow(value, size = "normal") {
  const str = String(value);
  return `<div class="flap-row">${[...str]
    .map((ch) => `<div class="flap">${ch}</div>`)
    .join("")}</div>`;
}

// ===================== HOME =====================
async function renderHome() {
  setActiveNav("home");
  showLoader();
  try {
    const me = await api("/api/me");
    state.me = me;
    const u = me.user;
    const pct = me.total_words ? Math.round((100 * me.known) / me.total_words) : 0;

    root.innerHTML = `
      <div class="hero">
        <div class="hero-top">
          <div>
            <div class="streak-badge"><span class="flame">${u.streak > 0 ? "🔥" : "💤"}</span> ${flapRow(u.streak)}</div>
            <div class="streak-label">дней подряд</div>
          </div>
          <div class="xp-pill">⭐ ${u.xp} XP</div>
        </div>
        <div class="progress-track">
          <div class="progress-track-label"><span>Словарный запас</span><span>${me.known}/${me.total_words}</span></div>
          <div class="rail"><div class="rail-fill" style="width:${pct}%"></div></div>
        </div>
        ${me.due_now > 0 ? `<div style="margin-top:12px;font-size:12px;color:var(--chalk-dim)">⏰ ${me.due_now} слов ждут повторения</div>` : ""}
      </div>

      <div class="section-label">Тренировки</div>
      <div class="tiles">
        <button class="tile" data-go="flashcards">
          <div class="tile-badge badge-1">📚</div>
          <div><div class="tile-title">Карточки</div><div class="tile-sub">Повторение слов</div></div>
        </button>
        <button class="tile" data-go="quiz">
          <div class="tile-badge badge-2">🎯</div>
          <div><div class="tile-title">Квиз</div><div class="tile-sub">Выбери перевод</div></div>
        </button>
        <button class="tile" data-go="scramble">
          <div class="tile-badge badge-3">🔤</div>
          <div><div class="tile-title">Собери слово</div><div class="tile-sub">Из букв</div></div>
        </button>
        <button class="tile" data-go="translate">
          <div class="tile-badge badge-4">✍️</div>
          <div><div class="tile-title">Ввод перевода</div><div class="tile-sub">Сложный режим</div></div>
        </button>
        <button class="tile" data-go="matching" style="grid-column: span 2;">
          <div class="tile-badge badge-5">⚡</div>
          <div><div class="tile-title">Найди пару</div><div class="tile-sub">На скорость</div></div>
        </button>
      </div>
    `;
    root.querySelectorAll("[data-go]").forEach((el) => {
      el.addEventListener("click", () => {
        haptic("light");
        GAME_ROUTER[el.dataset.go]();
      });
    });
  } catch (e) {
    renderError();
  }
}

function renderError() {
  root.innerHTML = `<div class="empty-state"><div class="emoji">📡</div>Не удалось загрузить данные.<br>Попробуй перезайти в приложение.</div>`;
}

function topbar(title, backFn) {
  return `<div class="topbar"><button class="back-btn" id="back-btn">←</button><div class="topbar-title">${title}</div></div>`;
}
function wireBack(fn) {
  document.getElementById("back-btn")?.addEventListener("click", () => {
    haptic("light");
    fn();
  });
}

// ===================== PROFILE =====================
async function renderProfile() {
  setActiveNav("profile");
  showLoader();
  try {
    const me = await api("/api/me");
    state.me = me;
    const u = me.user;
    root.innerHTML = `
      <h2 style="margin-bottom:16px;">🪪 Профиль</h2>
      <div class="stat-grid">
        <div class="stat-card"><div class="stat-value">${u.streak}</div><div class="stat-label">Streak сейчас</div></div>
        <div class="stat-card"><div class="stat-value">${u.longest_streak}</div><div class="stat-label">Рекорд streak</div></div>
        <div class="stat-card"><div class="stat-value">${u.xp}</div><div class="stat-label">Всего XP</div></div>
        <div class="stat-card"><div class="stat-value">${me.known}</div><div class="stat-label">Слов выучено</div></div>
      </div>

      <div class="section-label">Уровень словаря</div>
      <div class="level-grid" id="level-grid">
        ${["A1", "A2", "B1", "B2"].map((lvl) => `<button class="level-chip ${u.level === lvl ? "active" : ""}" data-level="${lvl}">${lvl}</button>`).join("")}
      </div>

      <div class="section-label">Настройки</div>
      <div class="toggle-row" id="reminders-toggle">
        <span>🔔 Напоминания</span>
        <div class="switch ${u.reminders_enabled ? "on" : ""}" id="reminders-switch"></div>
      </div>
    `;
    root.querySelectorAll("[data-level]").forEach((el) => {
      el.addEventListener("click", async () => {
        haptic("light");
        await api("/api/level", { method: "POST", body: JSON.stringify({ level: el.dataset.level }) });
        renderProfile();
      });
    });
  } catch (e) {
    renderError();
  }
}

// ===================== FLASHCARDS =====================
async function renderFlashcards() {
  root.innerHTML = topbar("Карточки");
  wireBack(renderHome);
  const body = document.createElement("div");
  root.appendChild(body);
  body.innerHTML = `<div class="loader"><span></span><span></span><span></span></div>`;

  const data = await api("/api/words/due?limit=1");
  if (!data.words.length) {
    body.innerHTML = emptyDone();
    wireDoneButtons();
    return;
  }
  const w = data.words[0];
  let revealed = false;

  function draw() {
    body.innerHTML = `
      <div class="ticket">
        <div class="ticket-cat">${w.category} · ${w.level}</div>
        <div class="ticket-word">${w.de}</div>
        ${revealed ? `<div class="ticket-perforation"></div><div class="ticket-translation">${w.ru}</div>` : ""}
      </div>
      ${
        !revealed
          ? `<button class="btn btn-primary" style="margin-top:18px" id="reveal">👀 Показать перевод</button>`
          : `<div class="btn-row">
               <button class="btn btn-danger" id="no">❌ Не знаю</button>
               <button class="btn btn-success" id="yes">✅ Знаю</button>
             </div>`
      }
    `;
    if (!revealed) {
      document.getElementById("reveal").addEventListener("click", () => {
        revealed = true;
        haptic("light");
        draw();
      });
    } else {
      document.getElementById("yes").addEventListener("click", () => answer(true));
      document.getElementById("no").addEventListener("click", () => answer(false));
    }
  }

  async function answer(correct) {
    haptic(correct ? "success" : "error");
    await api("/api/answer", { method: "POST", body: JSON.stringify({ word_id: w.id, correct }) });
    renderFlashcards();
  }

  draw();
}

// ===================== QUIZ =====================
async function renderQuiz(qNum = 1, correctCount = 0) {
  const TOTAL = 8;
  root.innerHTML = topbar(`Квиз · ${qNum}/${TOTAL}`);
  wireBack(renderHome);
  const body = document.createElement("div");
  root.appendChild(body);
  body.innerHTML = `<div class="loader"><span></span><span></span><span></span></div>`;

  const data = await api("/api/quiz/question");
  if (data.done || qNum > TOTAL) {
    renderQuizResult(correctCount, qNum - 1);
    return;
  }
  const w = data.word;
  body.innerHTML = `
    <div class="ticket" style="min-height:140px;">
      <div class="ticket-cat">${w.category}</div>
      <div class="ticket-word">${w.de}</div>
    </div>
    <div class="option-list">
      ${data.options.map((o, i) => `<button class="option" data-i="${i}" data-correct="${o.correct}">${o.text}</button>`).join("")}
    </div>
  `;
  const buttons = [...body.querySelectorAll(".option")];
  buttons.forEach((btn) => {
    btn.addEventListener("click", async () => {
      buttons.forEach((b) => (b.disabled = true));
      const isCorrect = btn.dataset.correct === "true";
      btn.classList.add(isCorrect ? "correct" : "wrong");
      if (!isCorrect) buttons.find((b) => b.dataset.correct === "true").classList.add("correct");
      haptic(isCorrect ? "success" : "error");
      await api("/api/answer", { method: "POST", body: JSON.stringify({ word_id: w.id, correct: isCorrect }) });
      setTimeout(() => renderQuiz(qNum + 1, correctCount + (isCorrect ? 1 : 0)), 700);
    });
  });
}

function renderQuizResult(correct, total) {
  const pct = total ? Math.round((100 * correct) / total) : 0;
  const mood = pct >= 80 ? "🏆 Отличный результат!" : pct >= 50 ? "👍 Неплохо, но есть куда расти!" : "💪 Повтори карточки и возвращайся!";
  root.innerHTML = `
    ${topbar("Результат")}
    <div class="result-icon">🎯</div>
    <div class="result-title">${correct}/${total} правильно</div>
    <div class="result-sub">${mood}</div>
    <div class="btn-row">
      <button class="btn btn-ghost" id="home-btn">🏠 В меню</button>
      <button class="btn btn-primary" id="again-btn">🔁 Ещё раз</button>
    </div>
  `;
  wireBack(renderHome);
  document.getElementById("home-btn").addEventListener("click", renderHome);
  document.getElementById("again-btn").addEventListener("click", () => renderQuiz());
}

// ===================== SCRAMBLE =====================
async function renderScramble() {
  root.innerHTML = topbar("Собери слово");
  wireBack(renderHome);
  const body = document.createElement("div");
  root.appendChild(body);
  body.innerHTML = `<div class="loader"><span></span><span></span><span></span></div>`;

  const data = await api("/api/scramble/word");
  if (data.done) {
    body.innerHTML = emptyDone();
    wireDoneButtons();
    return;
  }
  const w = data.word;
  const letters = data.letters.map((l, i) => ({ letter: l, idx: i, used: false }));
  let typed = "";

  function draw() {
    body.innerHTML = `
      <div class="ticket-cat" style="text-align:center;margin-bottom:4px;">Перевод</div>
      <div class="ticket-translation" style="text-align:center;">${w.ru}</div>
      <div class="scramble-slots">
        ${Array.from({ length: data.target_length }).map((_, i) => `<div class="scramble-slot">${typed[i] ? typed[i].toUpperCase() : ""}</div>`).join("")}
      </div>
      <div class="letter-pool">
        ${letters.map((l) => `<button class="letter-btn" data-idx="${l.idx}" ${l.used ? "disabled" : ""}>${l.letter}</button>`).join("")}
      </div>
      <button class="btn btn-ghost" style="margin-top:18px" id="erase">⌫ Стереть</button>
    `;
    body.querySelectorAll(".letter-btn").forEach((btn) => {
      btn.addEventListener("click", async () => {
        const idx = Number(btn.dataset.idx);
        letters[idx].used = true;
        typed += letters[idx].letter;
        haptic("light");
        if (typed.length === data.target_length) {
          const res = await api("/api/scramble/check", { method: "POST", body: JSON.stringify({ word_id: w.id, answer: typed }) });
          haptic(res.correct ? "success" : "error");
          root.innerHTML = `
            ${topbar("Собери слово")}
            <div class="result-icon">${res.correct ? "✅" : "❌"}</div>
            <div class="result-title">${res.correct ? "Правильно!" : "Почти!"}</div>
            <div class="result-sub">${res.correct_word} — ${w.ru}</div>
            <div class="btn-row">
              <button class="btn btn-ghost" id="home-btn">🏠 В меню</button>
              <button class="btn btn-primary" id="again-btn">➡️ Дальше</button>
            </div>
          `;
          wireBack(renderHome);
          document.getElementById("home-btn").addEventListener("click", renderHome);
          document.getElementById("again-btn").addEventListener("click", renderScramble);
        } else {
          draw();
        }
      });
    });
    document.getElementById("erase").addEventListener("click", () => {
      if (!typed) return;
      const lastChar = typed[typed.length - 1];
      for (let i = letters.length - 1; i >= 0; i--) {
        if (letters[i].used && letters[i].letter === lastChar) {
          letters[i].used = false;
          break;
        }
      }
      typed = typed.slice(0, -1);
      draw();
    });
  }
  draw();
}

// ===================== TRANSLATE (manual input) =====================
async function renderTranslate() {
  root.innerHTML = topbar("Введи перевод");
  wireBack(renderHome);
  const body = document.createElement("div");
  root.appendChild(body);
  body.innerHTML = `<div class="loader"><span></span><span></span><span></span></div>`;

  const data = await api("/api/words/due?limit=1");
  if (!data.words.length) {
    body.innerHTML = emptyDone();
    wireDoneButtons();
    return;
  }
  const w = data.words[0];
  body.innerHTML = `
    <div class="ticket-cat" style="text-align:center;">Переведи на немецкий</div>
    <div class="ticket-translation" style="text-align:center;font-size:24px;margin-top:6px;">${w.ru}</div>
    <input class="answer-input" id="answer" placeholder="Напиши ответ..." autocomplete="off" autocapitalize="off">
    <button class="btn btn-primary" style="margin-top:14px" id="submit">Проверить</button>
  `;
  const input = document.getElementById("answer");
  input.focus();
  async function submit() {
    const val = input.value.trim();
    if (!val) return;
    const res = await api("/api/translate/check", { method: "POST", body: JSON.stringify({ word_id: w.id, answer: val }) });
    haptic(res.correct ? "success" : "error");
    root.innerHTML = `
      ${topbar("Результат")}
      <div class="result-icon">${res.correct ? "✅" : "❌"}</div>
      <div class="result-title">${res.correct ? "Верно!" : "Неверно"}</div>
      <div class="result-sub">Правильный ответ: ${res.correct_word}</div>
      <div class="btn-row">
        <button class="btn btn-ghost" id="home-btn">🏠 В меню</button>
        <button class="btn btn-primary" id="again-btn">➡️ Дальше</button>
      </div>
    `;
    wireBack(renderHome);
    document.getElementById("home-btn").addEventListener("click", renderHome);
    document.getElementById("again-btn").addEventListener("click", renderTranslate);
  }
  document.getElementById("submit").addEventListener("click", submit);
  input.addEventListener("keydown", (e) => { if (e.key === "Enter") submit(); });
}

// ===================== MATCHING =====================
async function renderMatching() {
  root.innerHTML = topbar("Найди пару");
  wireBack(renderHome);
  const body = document.createElement("div");
  root.appendChild(body);
  body.innerHTML = `<div class="loader"><span></span><span></span><span></span></div>`;

  const data = await api("/api/matching/session");
  const items = [];
  data.words.forEach((w) => {
    items.push({ text: w.de, wordId: w.id, type: "de", matched: false });
    items.push({ text: w.ru, wordId: w.id, type: "ru", matched: false });
  });
  items.sort(() => Math.random() - 0.5);

  let selected = [];
  let matchedCount = 0;
  const startTime = Date.now();

  function draw() {
    body.innerHTML = `
      <div class="match-timer">Пар найдено: ${matchedCount}/${data.words.length}</div>
      <div class="match-grid">
        ${items.map((it, i) => `<button class="match-card ${it.matched ? "matched" : ""} ${selected.includes(i) ? "selected" : ""}" data-i="${i}">${it.text}</button>`).join("")}
      </div>
    `;
    body.querySelectorAll(".match-card").forEach((el) => {
      el.addEventListener("click", () => pick(Number(el.dataset.i)));
    });
  }

  async function pick(i) {
    if (items[i].matched || selected.includes(i)) return;
    selected.push(i);
    if (selected.length < 2) {
      draw();
      return;
    }
    const [i1, i2] = selected;
    if (items[i1].wordId === items[i2].wordId && items[i1].type !== items[i2].type) {
      items[i1].matched = true;
      items[i2].matched = true;
      matchedCount++;
      haptic("success");
      await api("/api/answer", { method: "POST", body: JSON.stringify({ word_id: items[i1].wordId, correct: true }) });
      selected = [];
      if (matchedCount >= data.words.length) {
        const elapsed = Math.round((Date.now() - startTime) / 1000);
        root.innerHTML = `
          ${topbar("Результат")}
          <div class="result-icon">🎉</div>
          <div class="result-title">Все пары найдены!</div>
          <div class="result-sub">⏱ Время: ${elapsed} сек</div>
          <div class="btn-row">
            <button class="btn btn-ghost" id="home-btn">🏠 В меню</button>
            <button class="btn btn-primary" id="again-btn">🔁 Ещё раз</button>
          </div>
        `;
        wireBack(renderHome);
        document.getElementById("home-btn").addEventListener("click", renderHome);
        document.getElementById("again-btn").addEventListener("click", renderMatching);
        return;
      }
      draw();
    } else {
      haptic("error");
      draw();
      setTimeout(() => {
        selected = [];
        draw();
      }, 500);
    }
  }
  draw();
}

// ===================== Shared helpers =====================
function emptyDone() {
  return `<div class="empty-state"><div class="emoji">🎉</div>Все слова на сегодня повторены!<br>Загляни попозже 💪</div>`;
}
function wireDoneButtons() {
  const btn = document.createElement("button");
  btn.className = "btn btn-primary";
  btn.style.marginTop = "16px";
  btn.textContent = "🏠 В меню";
  btn.addEventListener("click", renderHome);
  root.appendChild(btn);
}

const GAME_ROUTER = {
  flashcards: renderFlashcards,
  quiz: () => renderQuiz(),
  scramble: renderScramble,
  translate: renderTranslate,
  matching: renderMatching,
};

// ===================== Init =====================
renderHome();
