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
    return "🦅 Saqr Army Bot LIVE - عربي 🔥"

def run_flask():
    app.run(host="0.0.0.0", port=10000)

# === ردود عربية ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🦅 أهلا يا قائد! \n\n"
        "أنا بوت جيش صقر - جاهز! 🔥\n"
        "احكيني شو بدك؟\n\n"
        "الأوامر:\n"
        "/start - البداية\n"
        "/help - مساعدة\n"
        "/jesh - حالة الجيش"
    )

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📜 أوامر جيش صقر:\n\n"
        "• احكيني أي شي بالعربي برد عليك\n"
        "• /jesh - بشوفلك وضع الجيش\n"
        "• /nukte - نكتة عسكرية 😂\n"
        "• /hikme - حكمة اليوم"
    )

async def jesh(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🪖 تقرير جيش صقر:\n\n"
        "✅ البوت شغال 100%\n"
        "✅ السيرفر Live\n"
        "✅ الرد العربي فعال\n"
        "✅ القائد مسيطر 🔥\n\n"
        "جاهزين لأي مهمة يا قائد!"
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

# === الرد الذكي بالعربي على أي كلام ===
async def talk_arabic(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text.lower()
    
    if "سلام" in msg or "مرحبا" in msg or "هلا" in msg:
        reply = "وعليكم السلام يا قائد! 🦅 هلا والله، شو الأخبار؟"
    elif "كيفك" in msg or "شلونك" in msg:
        reply = "الحمدلله بألف خير! انت كيفك يا بطل؟ جاهز للمهمة؟ 🔥"
    elif "شو اسمك" in msg:
        reply = "أنا صقر 🦅 بوت جيش صقر، الذراع اليمين للقائد!"
    elif "بتحبني" in msg:
        reply = "أكيد بحبك يا قائد! انت قائ
