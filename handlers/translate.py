from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

import database as db
from keyboards import continue_kb, main_menu_kb, back_to_menu_kb
from states import Game
from utils import fuzzy_match

router = Router()


async def ask_word(callback_or_msg, state: FSMContext, user_id: int):
    user = await db.get_user(user_id)
    words = await db.get_due_words(user_id, user["levels"], limit=1)
    if not words:
        await callback_or_msg.answer(
            "🎉 Все слова на сегодня повторены! Загляни попозже 💪", reply_markup=main_menu_kb()
        )
        await state.clear()
        return
    w = words[0]
    await state.set_state(Game.translate)
    await state.update_data(word_id=w["id"], de=w["de"], ru=w["ru"])
    text = (
        f"✍️ <b>Введи перевод на немецкий</b>\n\n"
        f"Слово: <b>{w['ru']}</b>\n\n"
        f"<i>Напиши ответ прямо в чат (артикль можно не писать)</i>"
    )
    await callback_or_msg.answer(text, reply_markup=back_to_menu_kb())


@router.callback_query(F.data == "mode:translate")
async def start_translate(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await ask_word(callback.message, state, callback.from_user.id)
    await callback.answer()


@router.message(Game.translate)
async def check_translation(message: Message, state: FSMContext):
    data = await state.get_data()
    if not data:
        return
    is_correct = fuzzy_match(message.text, data["de"])
    await db.record_answer(message.from_user.id, data["word_id"], is_correct)
    if is_correct:
        text = f"✅ <b>Верно!</b> {data['de']} +3 XP 🎉"
    else:
        text = f"❌ Неверно. Правильный ответ: <b>{data['de']}</b>"
    await message.answer(text, reply_markup=continue_kb("translate"))
    await state.clear()
