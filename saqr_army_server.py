import os
import asyncio
from flask import Flask
from threading import Thread
from telegram import Bot
from telegram.ext import Application
import datetime

TOKEN = os.environ.get("@SaqrAmyBot")
CHAT_ID = os.environ.get("9126988116")

app = Flask(__name__)

@app.route('/')
def home():
    return "Saqr Army 500 - Online 🦅"

def run_flask():
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))

async def send_hourly():
    bot = Bot(token=TOKEN)
    while True:
        now = datetime.datetime.now().strftime("%H:%M %d/%m")
        msg = f"🦅 قرار مجلس الـ 500\n\nالوقت: {now}\nالحالة: الجيش جاهز وقيد الاستعداد\n\n#صقر_الجيش"
        try:
            await bot.send_message(chat_id=CHAT_ID, text=msg)
        except Exception as e:
            print(f"Error: {e}")
        await asyncio.sleep(3600) # كل ساعة

async def main_bot():
    await send_hourly()

if __name__ == "__main__":
    Thread(target=run_flask).start()
    asyncio.run(main_bot())
