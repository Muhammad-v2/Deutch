import random
from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

import database as db
from keyboards import quiz_kb, continue_kb, main_menu_kb
from states import Game

router = Router()

QUIZ_LEN = 8


async def ask_question(callback: CallbackQuery, state: FSMContext):
    user = await db.get_user(callback.from_user.id)
    words = await db.get_due_words(callback.from_user.id, user["level"], limit=1)
    if not words:
        await finish_quiz(callback, state)
        return
    word = words[0]
    distractors = await db.get_random_words(user["level"], word["id"], n=3)
    if len(distractors) < 3:
        await finish_quiz(callback, state)
        return
    options = [(word["ru"], True)] + [(d["ru"], False) for d in distractors]
    random.shuffle(options)

    await state.update_data(current_word_id=word["id"], current_de=word["de"])
    data = await state.get_data()
    q_num = data.get("q_num", 0) + 1
    await state.update_data(q_num=q_num)

    text = f"🎯 <b>Вопрос {q_num}/{QUIZ_LEN}</b>\n\nКак переводится слово:\n\n<b>{word['de']}</b>"
    await callback.message.edit_text(text, reply_markup=quiz_kb(word["id"], options))


async def finish_quiz(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    correct = data.get("correct", 0)
    total = data.get("q_num", 0)
    await db.update_game_score(callback.from_user.id, "quiz", correct)
    await state.clear()
    pct = round(100 * correct / total) if total else 0
    if pct >= 80:
        mood = "🏆 Отличный результат!"
    elif pct >= 50:
        mood = "👍 Неплохо, но есть куда расти!"
    else:
        mood = "💪 Не сдавайся, повтори карточки и возвращайся!"
    text = (
        f"<b>🎯 Квиз завершён!</b>\n\n"
        f"Правильно: <b>{correct}/{total}</b> ({pct}%)\n\n"
        f"{mood}"
    )
    await callback.message.edit_text(text, reply_markup=continue_kb("quiz"))


@router.callback_query(F.data == "mode:quiz")
async def start_quiz(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await state.set_state(Game.quiz)
    await state.update_data(q_num=0, correct=0)
    await ask_question(callback, state)
    await callback.answer()


@router.callback_query(F.data.startswith("quiz_answer:"))
async def handle_quiz_answer(callback: CallbackQuery, state: FSMContext):
    _, word_id, is_correct, _idx = callback.data.split(":")
    word_id, is_correct = int(word_id), bool(int(is_correct))
    await db.record_answer(callback.from_user.id, word_id, is_correct)

    data = await state.get_data()
    correct_count = data.get("correct", 0) + (1 if is_correct else 0)
    await state.update_data(correct=correct_count)

    await callback.answer("✅ Верно! +2 XP" if is_correct else "❌ Неверно", show_alert=False)

    if data.get("q_num", 0) >= QUIZ_LEN:
        await finish_quiz(callback, state)
    else:
        await ask_question(callback, state)
