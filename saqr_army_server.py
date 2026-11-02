import os
from flask import Flask
from threading import Thread
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

TOKEN = os.getenv("TELEGRAM_TOKEN").strip()
print(f"TOKEN LEN: {len(TOKEN)} - START: {TOKEN[:5]}...")
if ":" not in TOKEN:
    print("ERROR: TOKEN MISSING COLON! You pasted only ID!")
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
