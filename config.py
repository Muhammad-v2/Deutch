import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
DATABASE_URL = os.getenv("DATABASE_URL")  # Neon.tech connection string, вида postgresql://user:pass@host/dbname?sslmode=require
ADMIN_IDS = [int(x) for x in os.getenv("ADMIN_IDS", "").split(",") if x.strip()]

# Публичный URL мини-аппа (домен, который выдаёт Railway после деплоя), например:
# https://deutsch-trainer-bot-production.up.railway.app
WEBAPP_URL = os.getenv("WEBAPP_URL", "")

# Порт для встроенного веб-сервера (мини-апп + API). Railway сам прокидывает PORT.
PORT = int(os.getenv("PORT", 8080))

# Времена напоминаний в UTC (подстрой под свой часовой пояс -3/+3 итд при желании)
REMINDER_HOURS_UTC = [6, 9, 12, 15, 18, 20]  # 6 напоминаний в день

DAILY_GOAL = 15  # слов в день для "закрытого" дня и сохранения streak
