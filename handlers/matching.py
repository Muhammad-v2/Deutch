import random
import time
from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

import database as db
from keyboards import matching_kb, continue_kb, main_menu_kb
from states import Game

router = Router()

PAIRS_COUNT = 6


async def start_matching(callback: CallbackQuery, state: FSMContext):
    user = await db.get_user(callback.from_user.id)
    words = await db.get_due_words(callback.from_user.id, user["level"], limit=PAIRS_COUNT)
    if len(words) < PAIRS_COUNT:
        extra = await db.get_random_words(user["level"], -1, n=PAIRS_COUNT - len(words))
        words += extra
    words = words[:PAIRS_COUNT]

    items = []
    for w in words:
        items.append({"text": w["de"], "type": "de", "word_id": w["id"], "matched": False})
        items.append({"text": w["ru"], "type": "ru", "word_id": w["id"], "matched": False})
    random.shuffle(items)

    await state.set_state(Game.matching)
    await state.update_data(items=items, selected=[], start_time=time.time(), matched_count=0)
    await render_board(callback, state)


async def render_board(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    items = [(it["text"], it["type"]) for it in data["items"]]
    matched_selected = [
        i for i, it in enumerate(data["items"]) if it["matched"] or i in data["selected"]
    ]
    text = (
        f"⚡ <b>Найди пару</b>\n\nСоедини немецкие слова с переводом. "
        f"Найдено пар: <b>{data['matched_count']}/{PAIRS_COUNT}</b>"
    )
    kb = matching_kb(items, [it["word_id"] for it in data["items"]], matched_selected)
    # прячем уже найденные пары из клавиатуры
    from aiogram.utils.keyboard import InlineKeyboardBuilder
    b = InlineKeyboardBuilder()
    for idx, it in enumerate(data["items"]):
        if it["matched"]:
            continue
        prefix = "🔵 " if idx in data["selected"] else ""
        b.button(text=f"{prefix}{it['text']}", callback_data=f"match_pick:{idx}")
    b.adjust(2)
    await callback.message.edit_text(text, reply_markup=b.as_markup())


@router.callback_query(F.data == "mode:matching")
async def matching_entry(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await start_matching(callback, state)
    await callback.answer()


@router.callback_query(F.data.startswith("match_pick:"))
async def pick_item(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if not data:
        await callback.answer()
        return
    idx = int(callback.data.split(":")[1])
    items = data["items"]
    selected = data["selected"]

    if items[idx]["matched"] or idx in selected:
        await callback.answer()
        return

    selected.append(idx)

    if len(selected) < 2:
        await state.update_data(selected=selected)
        await render_board(callback, state)
        await callback.answer()
        return

    i1, i2 = selected
    it1, it2 = items[i1], items[i2]
    if it1["word_id"] == it2["word_id"] and it1["type"] != it2["type"]:
        items[i1]["matched"] = True
        items[i2]["matched"] = True
        matched_count = data["matched_count"] + 1
        await db.record_answer(callback.from_user.id, it1["word_id"], True)
        await state.update_data(items=items, selected=[], matched_count=matched_count)
        await callback.answer("✅ Пара найдена!")
        if matched_count >= PAIRS_COUNT:
            elapsed = round(time.time() - data["start_time"])
            score = max(0, 300 - elapsed)
            await db.update_game_score(callback.from_user.id, "matching", score)
            await state.clear()
            await callback.message.edit_text(
                f"🎉 <b>Все пары найдены!</b>\n\n⏱ Время: <b>{elapsed} сек</b>\n\nОтличная память! 🧠",
                reply_markup=continue_kb("matching"),
            )
            return
        await render_board(callback, state)
    else:
        await state.update_data(selected=[])
        await callback.answer("❌ Не пара, попробуй ещё")
        await render_board(callback, state)
