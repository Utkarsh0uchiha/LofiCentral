from telegram.ext import ContextTypes
from telegram import Update
async def about_handler(update: Update, context = ContextTypes.DEFAULT_TYPE):
    text = (
        "🎧 *LofiCentral*\n\n"
        "A vibe-based lofi playlist recommender built using *Python* and the "
        "*Telegram Bot API*.\n\n"
        "Explore curated playlists by mood and enjoy a minimal, "
        "distraction-free listening experience through an interactive interface.\n\n"
        "*Built by:* Utkarsh\n"
        "*GitHub:* https://github.com/Utkarsh0uchiha\n"
        "*Tech stack:* Python · Telegram Bot API · JSON\n"
        "*Status:* Actively improving\n\n"
        "Made with ❤️ and a lot of late-night debugging."
    )
    await update.message.reply_text(text, parse_mode = "Markdown")