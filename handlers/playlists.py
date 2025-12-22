import json
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from handlers.screens import render_screen_1


async def playlists_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # load playlist.json
    with open("data/playlists.json", "r", encoding="utf-8") as f:
        db = json.load(f)

    await render_screen_1(update.message, db, "reply")
