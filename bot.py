import logging
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8651551807:AAHAEkW6vYglSTA5QGhL5vT6s2G6j1GGAdc"
GAME = "lumberjack"
URL = "https://quiet-heliotrope-a67a45.netlify.app/lumberjack.html"

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("🪓 Play!", callback_game=True)]]
    await update.message.reply_game(GAME, reply_markup=InlineKeyboardMarkup(keyboard))

async def callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    if query.game_short_name == GAME:
        await query.answer(url=URL)

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("play", start))
app.add_handler(CallbackQueryHandler(callback))
app.run_polling()
