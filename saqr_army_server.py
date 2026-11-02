import os
from flask import Flask
from threading import Thread
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update

# هون التصحيح
TOKEN = (os.getenv("TELEGRAM_TOKEN") or "").strip()
print(f"TOKEN FOUND: {bool(TOKEN)} - LEN: {len(TOKEN)}")

if not TOKEN:
    print("ERROR: TELEGRAM_TOKEN not set in Render Environment!")
if ":" not in TOKEN and TOKEN:
    print("ERROR: Token missing ':' - you pasted only ID!")
app = Flask(__name__)
@app.route('/')
def home():
    return "Saqr Army 500 - Online 🦅"

# --- اوامر البوت ---
async def start(update, context):
    await update.message.reply_text("🦅 اهلا قائد! انا شغال! اكتب 'تداول'")

async def handle_msg(update, context):
    txt = update.message.text
    if "تداول" in txt:
        await update.message.reply_text("🔥 قرار مجلس الـ500: شراء الآن! #صقر")
    else:
        await update.message.reply_text(f"وصلتني: {txt}")

def run_flask():
    app.run(host='0.0.0.0', port=10000)

def run_bot():
    bot_app = ApplicationBuilder().token(TOKEN).build()
    bot_app.add_handler(CommandHandler("start", start))
    bot_app.add_handler(MessageHandler(filters.TEXT, handle_msg))
    bot_app.run_polling()

if __name__ == "__main__":
    Thread(target=run_flask).start()
    run_bot()
