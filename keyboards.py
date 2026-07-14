from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder

import config


def main_menu_kb() -> InlineKeyboardMarkup:
    b = InlineKeyboardBuilder()
    if config.WEBAPP_URL:
        b.button(text="🎮 Открыть приложение", web_app=WebAppInfo(url=config.WEBAPP_URL))
    b.button(text="📚 Учить слова", callback_data="mode:flashcards")
    b.button(text="🎯 Квиз", callback_data="mode:quiz")
    b.button(text="🔤 Собери слово", callback_data="mode:scramble")
    b.button(text="✍️ Введи перевод", callback_data="mode:translate")
    b.button(text="⚡ Найди пару", callback_data="mode:matching")
    b.button(text="📊 Статистика", callback_data="mode:stats")
    b.button(text="⚙️ Настройки", callback_data="mode:settings")
    if config.WEBAPP_URL:
        b.adjust(1, 2, 2, 2, 1)
    else:
        b.adjust(2, 2, 2, 1)
    return b.as_markup()


def level_kb() -> InlineKeyboardMarkup:
    b = InlineKeyboardBuilder()
    for lvl, desc in [("A1", "начинающий"), ("A2", "элементарный"), ("B1", "средний"), ("B2", "выше среднего")]:
        b.button(text=f"{lvl} — {desc}", callback_data=f"level:{lvl}")
    b.adjust(2, 2)
    return b.as_markup()


def flashcard_kb(word_id: int, revealed: bool) -> InlineKeyboardMarkup:
    b = InlineKeyboardBuilder()
    if not revealed:
        b.button(text="👀 Показать перевод", callback_data=f"fc_reveal:{word_id}")
    else:
        b.button(text="❌ Не знаю", callback_data=f"fc_answer:{word_id}:0")
        b.button(text="✅ Знаю", callback_data=f"fc_answer:{word_id}:1")
    b.button(text="🏠 В меню", callback_data="mode:menu")
    b.adjust(1) if not revealed else b.adjust(2, 1)
    return b.as_markup()


def quiz_kb(word_id: int, options: list[tuple[str, bool]]) -> InlineKeyboardMarkup:
    b = InlineKeyboardBuilder()
    for i, (text, is_correct) in enumerate(options):
        b.button(text=text, callback_data=f"quiz_answer:{word_id}:{1 if is_correct else 0}:{i}")
    b.adjust(1)
    return b.as_markup()


def scramble_kb(available: list[tuple[str, int]], word_id: int) -> InlineKeyboardMarkup:
    """available: список (буква, оригинальный_индекс) ещё не использованных букв"""
    b = InlineKeyboardBuilder()
    for letter, idx in available:
        b.button(text=letter.upper(), callback_data=f"scr_letter:{word_id}:{idx}")
    b.button(text="⌫ Стереть", callback_data=f"scr_back:{word_id}")
    b.button(text="🏠 В меню", callback_data="mode:menu")
    row_size = min(len(available), 6) or 1
    b.adjust(row_size, 1)
    return b.as_markup()


def settings_kb(reminders_on: bool) -> InlineKeyboardMarkup:
    b = InlineKeyboardBuilder()
    b.button(
        text=f"🔔 Напоминания: {'ВКЛ' if reminders_on else 'ВЫКЛ'}",
        callback_data="toggle_reminders",
    )
    b.button(text="🎚 Изменить уровень", callback_data="change_level")
    b.button(text="🏠 В меню", callback_data="mode:menu")
    b.adjust(1)
    return b.as_markup()


def back_to_menu_kb() -> InlineKeyboardMarkup:
    b = InlineKeyboardBuilder()
    b.button(text="🏠 В меню", callback_data="mode:menu")
    return b.as_markup()


def continue_kb(mode: str) -> InlineKeyboardMarkup:
    b = InlineKeyboardBuilder()
    b.button(text="➡️ Дальше", callback_data=f"mode:{mode}")
    b.button(text="🏠 В меню", callback_data="mode:menu")
    b.adjust(2)
    return b.as_markup()


def matching_kb(items: list[tuple[str, str]], word_ids: list[int], selected: list[int]) -> InlineKeyboardMarkup:
    """items: список (текст, тип 'de'/'ru') в перемешанном порядке, индекс = позиция"""
    b = InlineKeyboardBuilder()
    for idx, (text, _type) in enumerate(items):
        prefix = "✅ " if idx in selected else ""
        b.button(text=f"{prefix}{text}", callback_data=f"match_pick:{idx}")
    b.adjust(2)
    return b.as_markup()
