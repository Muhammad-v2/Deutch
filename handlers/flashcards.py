from aiogram import Router, F
from aiogram.types import CallbackQuery

import database as db
from keyboards import flashcard_kb, main_menu_kb

router = Router()

POS_EMOJI = {"n": "📦", "v": "🏃", "adj": "🎨", "adv": "➡️", "other": "🔹"}


async def send_next_card(callback: CallbackQuery):
    user = await db.get_user(callback.from_user.id)
    words = await db.get_due_words(callback.from_user.id, user["levels"], limit=1)
    if not words:
        await callback.message.edit_text(
            "🎉 <b>Вау! На сегодня все карточки повторены!</b>\n\n"
            "Возвращайся позже или попробуй другой режим — квиз или собери слово 💪",
            reply_markup=main_menu_kb(),
        )
        return
    w = words[0]
    emoji = POS_EMOJI.get(w.get("pos") or "other", "🔹")
    text = f"{emoji} <b>{w['de']}</b>\n\n<i>{w['category']} · {w['level']}</i>"
    await callback.message.edit_text(text, reply_markup=flashcard_kb(w["id"], revealed=False))


@router.callback_query(F.data == "mode:flashcards")
async def start_flashcards(callback: CallbackQuery):
    await send_next_card(callback)
    await callback.answer()


@router.callback_query(F.data.startswith("fc_reveal:"))
async def reveal_card(callback: CallbackQuery):
    word_id = int(callback.data.split(":")[1])
    async with db.pool.acquire() as con:
        w = await con.fetchrow("SELECT * FROM words WHERE id=$1", word_id)
    emoji = POS_EMOJI.get(w["pos"] or "other", "🔹")
    text = f"{emoji} <b>{w['de']}</b>\n\n➡️ <b>{w['ru']}</b>\n\n<i>{w['category']} · {w['level']}</i>\n\nЗнал(а) это слово?"
    await callback.message.edit_text(text, reply_markup=flashcard_kb(word_id, revealed=True))
    await callback.answer()


@router.callback_query(F.data.startswith("fc_answer:"))
async def answer_card(callback: CallbackQuery):
    _, word_id, correct = callback.data.split(":")
    word_id, correct = int(word_id), bool(int(correct))
    await db.record_answer(callback.from_user.id, word_id, correct)
    if correct:
        await callback.answer("✅ +2 XP", show_alert=False)
    else:
        await callback.answer("Ничего, повторим ещё раз позже 🔁", show_alert=False)
    await send_next_card(callback)
