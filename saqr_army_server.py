import os
from flask import Flask
from threading import Thread
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.environ.get("@SaqeAmyBot")

app = Flask(__name__)

@app.route('/')
def home():
    return "Saqr Army 500 - Online 🦅"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🦅 أهلا قائد! جيش الصقر 500 جاهز! ابعت كلمة 'تداول'")

async def reply_all(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if "تداول" in text:
        await update.message.reply_text("🔥 تداول مفعل! قرار مجلس الـ 500: شراء! #صقر_الجيش")
    else:
        await update.message.reply_text(f"🦅 تم استلام: {update.message.text} - الجيش بانتظار الأوامر")

def run_flask():
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))

async def run_bot():
    app_tg = ApplicationBuilder().token(TOKEN).build()
    app_tg.add_handler(CommandHandler("start", start))
    app_tg.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_all))
    print("Bot Started")
    await app_tg.run_polling()

if __name__ == "__main__":
    Thread(target=run_flask).start()
    import asyncio
    asyncio.run(run_bot())
