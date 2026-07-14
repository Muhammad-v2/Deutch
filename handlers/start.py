from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

import database as db
from keyboards import level_kb, main_menu_kb

router = Router()

WELCOME = (
    "👋 <b>Привет! Я — твой личный тренер немецкого 🇩🇪</b>\n\n"
    "Помогу закрепить и расширить словарный запас с A1 до B2: карточки, квизы, "
    "игры на скорость и память. Всё с системой интервального повторения — "
    "чтобы слова реально оседали в памяти, а не забывались на следующий день.\n\n"
    "Для начала скажи, какой у тебя сейчас уровень 👇"
)


@router.message(CommandStart())
async def cmd_start(message: Message):
    user = await db.get_or_create_user(
        message.from_user.id, message.from_user.username, message.from_user.first_name
    )
    await message.answer(WELCOME, reply_markup=level_kb())


@router.callback_query(F.data.startswith("level:"))
async def choose_level(callback: CallbackQuery):
    level = callback.data.split(":")[1]
    await db.set_level(callback.from_user.id, level)
    await callback.message.edit_text(
        f"✅ Отлично, уровень <b>{level}</b> установлен!\n\n"
        "🎯 Теперь жми на кнопку ниже и начинай учить слова. "
        "Я буду показывать тебе новые слова и повторять те, которые пора закрепить.\n\n"
        "💡 Совет: занимайся понемногу, но каждый день — так слова запоминаются лучше всего.",
        reply_markup=main_menu_kb(),
    )


@router.message(Command("menu"))
async def cmd_menu(message: Message):
    from handlers.menu import render_main_menu
    await render_main_menu(message.from_user.id, message)
