from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

import database as db
from keyboards import main_menu_kb, settings_kb, level_kb
from utils import progress_bar

router = Router()


async def menu_text(user_id: int) -> str:
    stats = await db.get_stats(user_id)
    u = stats["user"]
    bar = progress_bar(stats["known"], max(stats["total_words"], 1))
    fire = "🔥" if u["streak"] > 0 else "💤"
    due_line = f"\n⏰ Слов ждут повторения: <b>{stats['due_now']}</b>" if stats["due_now"] else ""
    return (
        f"<b>🇩🇪 Главное меню</b>\n\n"
        f"{fire} Streak: <b>{u['streak']}</b> дней (рекорд {u['longest_streak']})\n"
        f"⭐️ XP: <b>{u['xp']}</b> · Уровень словаря: <b>{u['level']}</b>\n"
        f"📗 Выучено слов: <b>{stats['known']}</b> / {stats['total_words']}\n"
        f"{bar}"
        f"{due_line}\n\n"
        f"Выбирай режим и погнали 👇"
    )


async def render_main_menu(user_id: int, target: Message):
    text = await menu_text(user_id)
    await target.answer(text, reply_markup=main_menu_kb())


@router.callback_query(F.data == "mode:menu")
async def show_menu(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    text = await menu_text(callback.from_user.id)
    await callback.message.edit_text(text, reply_markup=main_menu_kb())
    await callback.answer()


@router.callback_query(F.data == "mode:stats")
async def show_stats(callback: CallbackQuery):
    stats = await db.get_stats(callback.from_user.id)
    u = stats["user"]
    bar = progress_bar(stats["known"], max(stats["total_words"], 1))
    text = (
        "<b>📊 Твоя статистика</b>\n\n"
        f"🔥 Текущий streak: <b>{u['streak']}</b> дней\n"
        f"🏆 Лучший streak: <b>{u['longest_streak']}</b> дней\n"
        f"⭐️ Всего XP: <b>{u['xp']}</b>\n"
        f"📚 Уровень: <b>{u['level']}</b>\n\n"
        f"📗 Выучено (закреплено): <b>{stats['known']}</b>\n"
        f"📖 В процессе изучения: <b>{stats['learning']}</b>\n"
        f"📕 Всего слов в базе: <b>{stats['total_words']}</b>\n"
        f"{bar}\n\n"
        f"⏰ Слов ждут повторения прямо сейчас: <b>{stats['due_now']}</b>"
    )
    await callback.message.edit_text(text, reply_markup=main_menu_kb())
    await callback.answer()


@router.callback_query(F.data == "mode:settings")
async def show_settings(callback: CallbackQuery):
    user = await db.get_user(callback.from_user.id)
    await callback.message.edit_text(
        "<b>⚙️ Настройки</b>\n\nЗдесь можно отключить напоминания или сменить уровень слов.",
        reply_markup=settings_kb(user["reminders_enabled"]),
    )
    await callback.answer()


@router.callback_query(F.data == "toggle_reminders")
async def toggle_reminders(callback: CallbackQuery):
    user = await db.get_user(callback.from_user.id)
    new_val = not user["reminders_enabled"]
    await db.set_reminders(callback.from_user.id, new_val)
    await callback.answer("🔔 Напоминания включены" if new_val else "🔕 Напоминания выключены", show_alert=True)
    await callback.message.edit_reply_markup(reply_markup=settings_kb(new_val))


@router.callback_query(F.data == "change_level")
async def change_level(callback: CallbackQuery):
    await callback.message.edit_text("Выбери новый уровень слов:", reply_markup=level_kb())
    await callback.answer()
