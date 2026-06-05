import logging
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

logging.basicConfig(level=logging.INFO)

TOKEN = "8651551807:AAHAEkW6vYglSTA5QGhL5vT6s2G6j1GGAdc"
GAME = "lumberjack"
URL = "https://quiet-heliotrope-a67a45.netlify.app/"

async def play(update: Update, context: ContextTypes.DEFAULT_TYPE):
    kb = [[InlineKeyboardButton("🪓 Play!", callback_game=True)]]
    await update.message.reply_game(GAME, reply_markup=InlineKeyboardMarkup(kb))

async def answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer(url=URL)

application = Application.builder().token(TOKEN).build()
application.add_handler(CommandHandler("play", play))
application.add_handler(CallbackQueryHandler(answer))
application.run_polling()
