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

# Напоминания каждые N минут (агрессивный режим по запросу)
REMINDER_INTERVAL_MINUTES = 30

# Тихие часы по UTC — в это время напоминания не шлём, чтобы не будить людей ночью
# и не получать жалобы на спам от Telegram. Подстрой под свой часовой пояс.
QUIET_HOURS_UTC_START = 21  # 21:00 UTC
QUIET_HOURS_UTC_END = 5     # 05:00 UTC

DAILY_GOAL = 15  # слов в день для "закрытого" дня и сохранения streak
