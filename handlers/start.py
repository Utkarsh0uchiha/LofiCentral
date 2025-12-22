from telegram import Update
from telegram.ext import ContextTypes


async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    text = (
        f"Hello, {user.first_name}!\n\n"
        "I'm LofiCentral — your personal lofi vibe bot 🎧\n"
        "Send me any vibe (rainy, chill, study, midnight etc)\n"
        "and I'll recommend a lofi playlist.\n\n"
        "Commands:\n"
        "/playlists - show all available tags\n"
        "/help - how to use the bot\n"
        "/about - to know about us\n"
        "/random - to get a random playlist if not sure what to listen"
    )
    await update.message.reply_text(text)
