import random
import time
import json as jsonlib
from pathlib import Path

from aiohttp import web

import database as db
from auth import validate_init_data
from utils import fuzzy_match, shuffle_word_letters, strip_article

WEBAPP_DIR = Path(__file__).parent / "webapp"


def cors(resp: web.Response) -> web.Response:
    resp.headers["Access-Control-Allow-Origin"] = "*"
    resp.headers["Access-Control-Allow-Headers"] = "*"
    return resp


@web.middleware
async def auth_middleware(request: web.Request, handler):
    if request.path.startswith("/api/"):
        init_data = request.headers.get("X-Telegram-Init-Data", "")
        user = validate_init_data(init_data)
        if not user:
            return cors(web.json_response({"error": "unauthorized"}, status=401))
        request["tg_user"] = user
    return await handler(request)


routes = web.RouteTableDef()


@routes.options("/{tail:.*}")
async def options_handler(request):
    return cors(web.Response())


@routes.get("/api/me")
async def api_me(request: web.Request):
    tg_user = request["tg_user"]
    user = await db.get_or_create_user(
        tg_user["id"], tg_user.get("username", ""), tg_user.get("first_name", "")
    )
    stats = await db.get_stats(tg_user["id"])
    return cors(web.json_response({
        "user": jsonify_row(stats["user"]),
        "known": stats["known"],
        "learning": stats["learning"],
        "total_words": stats["total_words"],
        "due_now": stats["due_now"],
    }))


@routes.post("/api/level")
async def api_set_level(request: web.Request):
    tg_user = request["tg_user"]
    body = await request.json()
    level = body.get("level")
    if level not in ("A1", "A2", "B1", "B2"):
        return cors(web.json_response({"error": "bad level"}, status=400))
    await db.set_level(tg_user["id"], level)
    return cors(web.json_response({"ok": True}))


@routes.get("/api/words/due")
async def api_words_due(request: web.Request):
    tg_user = request["tg_user"]
    limit = int(request.query.get("limit", 1))
    user = await db.get_user(tg_user["id"])
    words = await db.get_due_words(tg_user["id"], user["level"], limit=limit)
    return cors(web.json_response({"words": [jsonify_row(w) for w in words]}))


@routes.get("/api/quiz/question")
async def api_quiz_question(request: web.Request):
    tg_user = request["tg_user"]
    user = await db.get_user(tg_user["id"])
    words = await db.get_due_words(tg_user["id"], user["level"], limit=1)
    if not words:
        return cors(web.json_response({"done": True}))
    word = words[0]
    distractors = await db.get_random_words(user["level"], word["id"], n=3)
    if len(distractors) < 3:
        return cors(web.json_response({"done": True}))
    options = [{"text": word["ru"], "correct": True}] + [
        {"text": d["ru"], "correct": False} for d in distractors
    ]
    random.shuffle(options)
    return cors(web.json_response({
        "word": jsonify_row(word), "options": options,
    }))


@routes.get("/api/scramble/word")
async def api_scramble_word(request: web.Request):
    tg_user = request["tg_user"]
    user = await db.get_user(tg_user["id"])
    words = await db.get_due_words(tg_user["id"], user["level"], limit=1)
    if not words:
        return cors(web.json_response({"done": True}))
    w = words[0]
    target = strip_article(w["de"]).lower()
    letters = shuffle_word_letters(w["de"])
    return cors(web.json_response({
        "word": jsonify_row(w), "target_length": len(target), "letters": letters,
    }))


@routes.post("/api/scramble/check")
async def api_scramble_check(request: web.Request):
    tg_user = request["tg_user"]
    body = await request.json()
    word_id, answer = body["word_id"], body["answer"]
    async with db.pool.acquire() as con:
        w = await con.fetchrow("SELECT * FROM words WHERE id=$1", word_id)
    target = strip_article(w["de"]).lower()
    correct = answer.strip().lower() == target
    stats = await db.record_answer_and_stats(tg_user["id"], word_id, correct)
    return cors(web.json_response({"correct": correct, "correct_word": w["de"], "stats": stats}))


@routes.post("/api/translate/check")
async def api_translate_check(request: web.Request):
    tg_user = request["tg_user"]
    body = await request.json()
    word_id, answer = body["word_id"], body["answer"]
    async with db.pool.acquire() as con:
        w = await con.fetchrow("SELECT * FROM words WHERE id=$1", word_id)
    correct = fuzzy_match(answer, w["de"])
    stats = await db.record_answer_and_stats(tg_user["id"], word_id, correct)
    return cors(web.json_response({"correct": correct, "correct_word": w["de"], "stats": stats}))


@routes.post("/api/answer")
async def api_answer(request: web.Request):
    tg_user = request["tg_user"]
    body = await request.json()
    word_id, correct = body["word_id"], bool(body["correct"])
    stats = await db.record_answer_and_stats(tg_user["id"], word_id, correct)
    return cors(web.json_response({"stats": stats}))


@routes.get("/api/matching/session")
async def api_matching_session(request: web.Request):
    tg_user = request["tg_user"]
    user = await db.get_user(tg_user["id"])
    words = await db.get_due_words(tg_user["id"], user["level"], limit=6)
    if len(words) < 6:
        extra = await db.get_random_words(user["level"], -1, n=6 - len(words))
        words += extra
    words = words[:6]
    return cors(web.json_response({"words": [jsonify_row(w) for w in words]}))


def jsonify_row(row: dict) -> dict:
    out = {}
    for k, v in row.items():
        if hasattr(v, "isoformat"):
            out[k] = v.isoformat()
        else:
            out[k] = v
    return out


async def index_handler(request: web.Request):
    return web.FileResponse(WEBAPP_DIR / "index.html")


def build_app() -> web.Application:
    app = web.Application(middlewares=[auth_middleware])
    app.add_routes(routes)
    app.router.add_get("/", index_handler)
    app.router.add_static("/static/", WEBAPP_DIR, show_index=False)
    return app
