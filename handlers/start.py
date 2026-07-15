from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

import database as db
from keyboards import level_multiselect_kb, main_menu_kb

router = Router()

WELCOME = (
    "👋 <b>Привет! Я — твой личный тренер немецкого 🇩🇪</b>\n\n"
    "Помогу закрепить и расширить словарный запас с A1 до B2: карточки, квизы, "
    "игры на скорость и память. Всё с системой интервального повторения — "
    "чтобы слова реально оседали в памяти, а не забывались на следующий день.\n\n"
    "Можешь выбрать сразу несколько уровней — слова будут показываться из всех "
    "выбранных сразу. Отметь нужные и жми «Готово» 👇"
)


@router.message(CommandStart())
async def cmd_start(message: Message):
    user = await db.get_or_create_user(
        message.from_user.id, message.from_user.username, message.from_user.first_name
    )
    if user["onboarded"]:
        from handlers.menu import render_main_menu
        await render_main_menu(message.from_user.id, message)
        return
    await message.answer(WELCOME, reply_markup=level_multiselect_kb(user["levels"], "onboard"))


@router.callback_query(F.data.startswith("lvl_toggle:"))
async def toggle_level(callback: CallbackQuery):
    _, level, context = callback.data.split(":")
    levels = await db.toggle_level(callback.from_user.id, level)
    await callback.message.edit_reply_markup(reply_markup=level_multiselect_kb(levels, context))
    await callback.answer()


@router.callback_query(F.data.startswith("lvl_done:"))
async def finish_level_pick(callback: CallbackQuery):
    context = callback.data.split(":")[1]
    if context == "onboard":
        await db.set_onboarded(callback.from_user.id)
        user = await db.get_user(callback.from_user.id)
        levels_str = ", ".join(user["levels"])
        await callback.message.edit_text(
            f"✅ Отлично, уровни <b>{levels_str}</b> выбраны!\n\n"
            "🎯 Теперь жми на кнопку ниже и начинай учить слова. "
            "Я буду показывать тебе новые слова и повторять те, которые пора закрепить.\n\n"
            "💡 Совет: занимайся понемногу, но каждый день — так слова запоминаются лучше всего.",
            reply_markup=main_menu_kb(),
        )
    else:
        from handlers.menu import show_settings_text
        await show_settings_text(callback)
    await callback.answer()


@router.message(Command("menu"))
async def cmd_menu(message: Message):
    from handlers.menu import render_main_menu
    await render_main_menu(message.from_user.id, message)
