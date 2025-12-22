from telegram import Update
from telegram.ext import ContextTypes


async def help_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "How to use LofiCentral:\n\n"
        "• Send any vibe (e.g., 'rainy study', 'chill night')\n"
        "  and I'll pick the right playlist.\n"
        "• Use /playlists to see all available tags.\n"
        "• Use /random to get a random playlist.\n"
        "• Try sending: 'send me some rainy vibes'\n\n"
        "I'm always learning your preferences!"
    )
    await update.message.reply_text(text)
