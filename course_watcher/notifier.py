

import asyncio
from telegram import Bot
from telegram.error import TelegramError
from .config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

async def _send(message: str):
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)

def send_telegram_message(message: str):
    try:
        asyncio.run(_send(message))
        print("📨 Telegram message sent")
    except TelegramError as e:
        print("❌ Telegram error:", e)
    except RuntimeError:

        loop = asyncio.get_event_loop()
        loop.create_task(_send(message))
