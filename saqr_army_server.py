# -*- coding: utf-8 -*-
import os
import time
import random
from flask import Flask
from threading import Thread
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from telegram import Update

TOKEN = (os.getenv("TELEGRAM_TOKEN") or "").strip()
print(f"TOKEN FOUND: {bool(TOKEN)} - LEN: {len(TOKEN)}")

app = Flask(__name__)
@app.route('/')
def home():
    return "Saqr Army Bot LIVE - Arabic"

def run_flask():
    app.run(host="0.0.0.0", port=10000)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🦅 اهلا يا قائد!\n\n"
        "انا بوت جيش صقر - جاهز! 🔥\n"
        "/help - مساعدة\n"
        "/jesh - حالة الجيش\n"
        "/nukte - نكتة\n"
        "/hikme - حكمة"
    )

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📜 اوامر جيش صقر:\n\n"
        "- احكيني اي شي بالعربي برد عليك\n"
        "- /jesh - وضع الجيش\n"
        "- /nukte - نكتة عسكرية\n"
        "- /hikme - حكمة اليوم"
    )

async def jesh(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🪖 تقرير جيش صقر:\n\n"
        "✅ البوت شغال 100%\n"
        "✅ السيرفر Live\n"
        "✅ الرد العربي فعال\n"
        "✅ القائد مسيطر 🔥\n\n"
        "جاهزين لاي مهمة يا قائد!"
    )

async def nukte(update: Update, context: ContextTypes.DEFAULT_TYPE):
    nukat = [
        "مرة عسكري راح عالبحر، قالولو ليش لابس بوط؟ قال بلكي صار غزو برمائي 😂",
        "جندي سأل القائد: فينا ناخد بريك؟ قالو: ايه، بريك قلب العدو! 😎",
        "مرة جيش صقر فات عالمعركة، العدو هرب قبل ما نبلش! 🦅"
    ]
    await update.message.reply_text(random.choice(nukat))

async def hikme(update: Update, context: ContextTypes.DEFAULT_TYPE):
    hikam = [
        "🦅 النصر صبر ساعة.",
        "🔥 القائد الناجح هو اللي بيسمع لجيشو.",
        "⚔️ لا تؤجل معركة اليوم للغد.",
        "🪖 القوة مش بالعدد، القوة بالعزيمة!"
    ]
    await update.message.reply_text(random.choice(hikam))

async def talk_arabic(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = (update.message.text or "").lower()
    
    if any(x in msg for x in ["سلام", "مرحبا", "هلا"]):
        reply = "وعليكم السلام يا قائد! 🦅 هلا والله، شو الاخبار؟"
    elif "كيفك" in msg or "شلونك" in msg:
        reply = "الحمدلله بالف خير! انت كيفك يا بطل؟ جاهز للمهمة؟ 🔥"
    elif "شو اسمك" in msg:
        reply = "انا صقر 🦅 بوت جيش صقر، الذراع اليمين للقائد!"
    elif "بتحبني" in msg or "بحبك" in msg:
        reply = "اكيد بحبك يا قائد! انت قائدي الغالي ❤️🦅"
    elif "شو بتعمل" in msg:
        reply = "عم راقب الحدود، عم احمي الجيش، وناطر اوامرك! 🪖"
    elif "تعبان" in msg:
        reply = "سلامتك يا قائد! ارتاح شوي، الجيش بامان معي 😉"
    elif "جيش" in msg:
        reply = "جيش صقر جاهز 100%! كل الجنود بالمواقع، ناطرين اشارة منك! 🦅🔥"
    else:
        reply = f"سمعتك يا قائد: {update.message.text}\n\nانا معك! شو بدك نعمل هلا؟ احكيني امر! 🦅"

    await update.message.reply_text(reply)

def run_bot():
    if not TOKEN or ":" not in TOKEN:
        print("❌ TOKEN غلط!")
        while True:
            time.sleep(100)

    print("✅ TOKEN OK - بوت عربي STARTING...")
    bot_app = ApplicationBuilder().token(TOKEN).updater(None).build()
    
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
