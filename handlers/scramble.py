from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

import database as db
from keyboards import scramble_kb, continue_kb, main_menu_kb
from states import Game
from utils import shuffle_word_letters, strip_article

router = Router()


def render_progress(target: str, typed: str) -> str:
    cells = []
    for i, ch in enumerate(target):
        if i < len(typed):
            cells.append(typed[i].upper())
        else:
            cells.append("_")
    return " ".join(cells)


async def new_word(callback: CallbackQuery, state: FSMContext):
    user = await db.get_user(callback.from_user.id)
    words = await db.get_due_words(callback.from_user.id, user["levels"], limit=1)
    if not words:
        await callback.message.edit_text(
            "🎉 Все слова на сегодня повторены! Загляни попозже 💪", reply_markup=main_menu_kb()
        )
        return
    w = words[0]
    target = strip_article(w["de"]).lower()
    letters = shuffle_word_letters(w["de"])
    await state.set_state(Game.scramble)
    await state.update_data(
        word_id=w["id"], de=w["de"], ru=w["ru"], target=target,
        letters=letters, used=[False] * len(letters),
    )
    available = [(l, i) for i, l in enumerate(letters)]
    text = (
        f"🔤 <b>Собери слово</b>\n\nПеревод: <b>{w['ru']}</b>\n\n"
        f"<code>{render_progress(target, '')}</code>"
    )
    await callback.message.edit_text(text, reply_markup=scramble_kb(available, w["id"]))


@router.callback_query(F.data == "mode:scramble")
async def start_scramble(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await new_word(callback, state)
    await callback.answer()


@router.callback_query(F.data.startswith("scr_letter:"))
async def pick_letter(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if not data:
        await callback.answer()
        return
    _, word_id, idx = callback.data.split(":")
    idx = int(idx)
    used = data["used"]
    if used[idx]:
        await callback.answer()
        return
    used[idx] = True
    typed = data.get("typed", "") + data["letters"][idx]
    await state.update_data(used=used, typed=typed)

    target = data["target"]
    if len(typed) == len(target):
        correct = typed == target
        await db.record_answer(callback.from_user.id, data["word_id"], correct)
        if correct:
            text = f"✅ <b>Правильно!</b>\n\n{data['de']} — {data['ru']}\n\n+3 XP 🎉"
        else:
            text = f"❌ <b>Почти!</b> Правильно: <b>{data['de']}</b>\n\n{data['ru']}"
        await callback.message.edit_text(text, reply_markup=continue_kb("scramble"))
        await state.clear()
        await callback.answer()
        return

    available = [(l, i) for i, l in enumerate(data["letters"]) if not used[i]]
    text = (
        f"🔤 <b>Собери слово</b>\n\nПеревод: <b>{data['ru']}</b>\n\n"
        f"<code>{render_progress(target, typed)}</code>"
    )
    await callback.message.edit_text(text, reply_markup=scramble_kb(available, word_id))
    await callback.answer()


@router.callback_query(F.data.startswith("scr_back:"))
async def erase_letter(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if not data or not data.get("typed"):
        await callback.answer()
        return
    typed = data["typed"]
    used = data["used"]
    last_char = typed[-1]
    # находим последний использованный индекс с этой буквой и освобождаем
    for i in reversed(range(len(data["letters"]))):
        if used[i] and data["letters"][i] == last_char:
            used[i] = False
            break
    typed = typed[:-1]
    await state.update_data(used=used, typed=typed)

    target = data["target"]
    available = [(l, i) for i, l in enumerate(data["letters"]) if not used[i]]
    text = (
        f"🔤 <b>Собери слово</b>\n\nПеревод: <b>{data['ru']}</b>\n\n"
        f"<code>{render_progress(target, typed)}</code>"
    )
    await callback.message.edit_text(text, reply_markup=scramble_kb(available, data["word_id"]))
    await callback.answer()
