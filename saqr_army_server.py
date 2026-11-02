# -*- coding: utf-8 -*-
import os
import time
import random
from flask import Flask
from threading import Thread
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from telegram import Update

# === تصحيح 1: قراءة التوكن وتنضيفو ===
TOKEN = (os.getenv("TELEGRAM_TOKEN") or "").strip()
print(f"TOKEN FOUND: {bool(TOKEN)} - LEN: {len(TOKEN)}")

# === تصحيح 2: Flask للـ Render ===
app = Flask(__name__)

@app.route('/')
def home():
    return "🦅 Saqr Army Bot LIVE - Arabic - OK - TOKEN OK"

def run_flask():
    port = int(os.getenv("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

# === تصحيح 3: كل الاوامر بالعربي ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = "🦅 اهلا يا قائد!\n\n"
    msg += "انا بوت جيش صقر - جاهز! 🔥\n\n"
    msg += "/help - مساعدة\n"
    msg += "/jesh - حالة الجيش\n"
    msg += "/nukte - نكتة\n"
    msg += "/hikme - حكمة\n\n"
    msg += "احكيني اي شي بالعربي!"
    await update.message.reply_text(msg)

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = "📜 اوامر جيش صقر:\n\n"
    msg += "/start - البداية\n"
    msg += "/jesh - وضع الجيش\n"
    msg += "/nukte - نكتة عسكرية\n"
    msg += "/hikme - حكمة\n"
    msg += "واي جملة عربية برد عليها"
    await update.message.reply_text(msg)

async def jesh(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = "🪖 تقرير جيش صقر:\n\n"
    msg += "✅ البوت شغال 100%\n"
    msg += "✅ السيرفر Live\n"
    msg += "✅ الرد العربي فعال\n"
    msg += "✅ القائد مسيطر 🔥\n\n"
    msg += "جاهزين لاي مهمة يا قائد!"
    await update.message.reply_text(msg)

async def nukte(update: Update, context: ContextTypes.DEFAULT_TYPE):
    n1 = "مرة عسكري راح عالبحر، قالولو ليش لابس بوط؟ قال بلكي صار غزو برمائي 😂"
    n2 = "جندي سأل القائد: فينا ناخد بريك؟ قالو: ايه، بريك قلب العدو! 😎"
    n3 = "جيش صقر فات عالمعركة، العدو هرب قبل ما نبلش! 🦅"
    await update.message.reply_text(random.choice([n1, n2, n3]))

async def hikme(update: Update, context: ContextTypes.DEFAULT_TYPE):
    h1 = "🦅 النصر صبر ساعة."
    h2 = "🔥 القائد الناجح هو اللي بيسمع لجيشو."
    h3 = "⚔️ لا تؤجل معركة اليوم للغد."
    h4 = "🪖 القوة مش بالعدد، القوة بالعزيمة!"
    await update.message.reply_text(random.choice([h1, h2, h3, h4]))

async def talk_arabic(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text or ""
    low = text.lower()
    if "سلام" in low or "مرحبا" in low or "هلا" in low:
        reply = "وعليكم السلام يا قائد! 🦅 هلا والله، شو الاخبار؟"
    elif "كيفك" in low or "شلونك" in low:
        reply = "الحمدلله بالف خير! انت كيفك يا بطل؟ جاهز للمهمة؟ 🔥"
    elif "شو اسمك" in low:
        reply = "انا صقر 🦅 بوت جيش صقر، الذراع اليمين للقائد!"
    elif "بحبك" in low or "بتحبني" in low:
        reply = "وانا بحبك اكتر يا قائد! ❤️🦅"
    elif "شو بتعمل" in low:
        reply = "عم راقب الحدود وعم احمي الجيش، ناطر اوامرك! 🪖"
    elif "تعبان" in low:
        reply = "سلامتك يا قائد! ارتاح شوي، الجيش بامان معي 😉"
    elif "جيش" in low:
        reply = "جيش صقر جاهز 100%! كل الجنود بالمواقع، ناطرين اشارة منك! 🦅🔥"
    else:
        reply = "سمعتك يا قائد: " + text + "\n\nانا معك! شو بدك نعمل هلا؟ 🦅"
    await update.message.reply_text(reply)

# === تصحيح 4: تشغيل البوت بدون اخطاء ===
def run_bot():
    if not TOKEN:
        print("❌ TELEGRAM_TOKEN not set in Render Environment!")
        while True:
            time.sleep(100)
    if ":" not in TOKEN:
        print("❌ TOKEN غلط! لازم فيه نقطتين :")
        print(f"LEN is {len(TOKEN)}")
        while True:
            time.sleep(100)
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
