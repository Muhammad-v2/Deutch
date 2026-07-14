import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiohttp import web

import database as db
from config import BOT_TOKEN, PORT
from data.words import WORDS
from scheduler import setup_scheduler
from api import build_app

from handlers import start, menu, flashcards, quiz, scramble, translate, matching

logging.basicConfig(level=logging.INFO)


async def run_bot():
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_router(start.router)
    dp.include_router(menu.router)
    dp.include_router(flashcards.router)
    dp.include_router(quiz.router)
    dp.include_router(scramble.router)
    dp.include_router(translate.router)
    dp.include_router(matching.router)

    scheduler = setup_scheduler(bot)
    scheduler.start()

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


async def run_webserver():
    app = build_app()
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", PORT)
    await site.start()
    logging.info(f"Веб-сервер мини-аппа запущен на порту {PORT}")
    while True:
        await asyncio.sleep(3600)


async def main():
    if not BOT_TOKEN:
        raise RuntimeError("Не задан BOT_TOKEN в переменных окружения")

    await db.init_pool()
    inserted = await db.seed_words(WORDS)
    logging.info(f"Слов в базе: {inserted}")

    await asyncio.gather(run_bot(), run_webserver())


if __name__ == "__main__":
    asyncio.run(main())
