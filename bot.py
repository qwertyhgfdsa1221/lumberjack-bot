import logging
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

# ==========================
# CONFIG
# ==========================

TOKEN = "SIZNING_TOKENINGIZ"
GAME_SHORT_NAME = "lumberjack"
GAME_URL = "https://quiet-heliotrope-a67a45.netlify.app/"

# ==========================
# LOGGING
# ==========================

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)

# Foydalanuvchilar scorelari
user_scores = {}

# ==========================
# COMMANDS
# ==========================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🌲 Welcome to LumberJack!\n\n"
        "Available commands:\n"
        "▶️ /play - Start game\n"
        "🏆 /score - Show score\n"
        "❓ /help - Help"
    )

    await update.message.reply_text(text)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "📖 Help Menu\n\n"
        "/play - Start LumberJack\n"
        "/score - Show your best score\n"
        "/help - Open help menu\n"
        "/start - Restart bot"
    )

    await update.message.reply_text(text)


async def play(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("🪓 Play!", callback_game=True)]
    ]

    await update.message.reply_game(
        game_short_name=GAME_SHORT_NAME,
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


async def score(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id

    score_value = user_scores.get(user_id, 0)

    await update.message.reply_text(
        f"🏆 Your best score: {score_value}"
    )


# ==========================
# GAME CALLBACK
# ==========================

async def game_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer(
        url=GAME_URL
    )


# ==========================
# ERROR HANDLER
# ==========================

async def error_handler(update, context):
    logger.error("Error:", exc_info=context.error)


# ==========================
# MAIN
# ==========================

def main():

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("play", play))
    app.add_handler(CommandHandler("score", score))

    app.add_handler(CallbackQueryHandler(game_callback))

    app.add_error_handler(error_handler)

    print("✅ LumberJack Bot Started")

    app.run_polling()


if name == "__main__":
    main()
