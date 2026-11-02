# -*- coding: utf-8 -*-
import os
import time
import random
import asyncio
from flask import Flask
from threading import Thread
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from telegram import Update

TOKEN = (os.getenv("TELEGRAM_TOKEN") or "").strip()
print(f"TOKEN FOUND: {bool(TOKEN)} - LEN: {len(TOKEN)}")

app = Flask(__name__)

@app.route('/')
def home():
    return "🦅 Saqr Army Bot LIVE - OK"

def run_flask():
    port = int(os.getenv("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🦅 اهلا يا قائد! انا بوت جيش صقر جاهز! 🔥\n/help للمساعدة")

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📜 /start /jesh /nukte /hikme - احكيني عربي!")

async def jesh(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🪖 جيش صقر جاهز 100% ✅🔥")

async def nukte(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(["مرة عسكري راح عالبحر 😂", "جيش صقر فات العدو هرب! 🦅"]))

async def hikme(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🦅 النصر صبر ساعة.")

async def talk_arabic(update: Update, context: ContextTypes.DEFAULT_TYPE):
    txt = update.message.text or ""
    low = txt.lower()
    if "سلام" in low or "مرحبا" in low or "هلا" in low:
        reply = "وعليكم السلام يا قائد! 🦅 هلا والله"
    elif "كيفك" in low:
        reply = "الحمدلله بخير يا بطل! 🔥"
    elif "بحبك" in low or "بتحبني" in low:
        reply = "وانا بحبك اكتر يا قائد! ❤️🦅"
    elif "جيش" in low:
        reply = "جيش صقر جاهز 100%! 🦅🔥"
    else:
        reply = "سمعتك: " + txt + " 🦅"
    await update.message.reply_text(reply)

def run_bot():
    if not TOKEN or ":" not in TOKEN:
        print("❌ TOKEN غلط!")
        while True:
            time.sleep(100)
    
    # تصحيح Event Loop لـ Python 3.11
    try:
        asyncio.set_event_loop(asyncio.new_event_loop())
    except:
        pass

    print("✅ TOKEN OK - بوت عربي STARTING POLLING...")
    bot_app = ApplicationBuilder().token(TOKEN).build()
    bot_app.add_handler(CommandHandler("start", start))
    bot_app.add_handler(CommandHandler("help", help_cmd))
    bot_app.add_handler(CommandHandler("jesh", jesh))
    bot_app.add_handler(CommandHandler("nukte", nukte))
    bot_app.add_handler(CommandHandler("hikme", hikme))
    bot_app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, talk_arabic))
    bot_app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    Thread(target=run_flask, daemon=True).start()
    run_bot()
