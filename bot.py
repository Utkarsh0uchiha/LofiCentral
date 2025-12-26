from handlers import playlists
from handlers.help import help_handler
from handlers.start import start_handler
from handlers.playlists import playlists_handler
from handlers.recommender import recommender_handler
from handlers.recommender import random_handler
from handlers.about import about_handler
import os
import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
import json
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler
from handlers.screens import render_screen_1, render_screen_2, render_screen_3

# loading the .env file
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

async def fallback_handler(update, context):
    await update.message.reply_text("Send /help to understand how to use the bot.")

# callback handler
async def button_click_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    with open("data/playlists.json", "r", encoding = "utf-8") as f:
        db = json.load(f)
    
    query = update.callback_query
    await query.answer()

    data = query.data

    # screen 2
    if data.startswith("v:"):
        tag = data.removeprefix("v:")
        await render_screen_2(query.message, db, tag)

    # screen 3
    elif data.startswith("p:"):
        _, tag, index = data.split(":")
        index = int(index)
        await render_screen_3(query.message, db, tag, index)
    
    elif data.startswith("b:"):
        tag = data.removeprefix("b:")
        if(tag == "root"):
            await render_screen_1(query.message, db, "edit")
        else:
            await render_screen_2(query.message, db, tag)

    elif data.startswith("r"):
        keywords = []

        for vibes, links in db.items():
            keywords.append(vibes)
        key = random.choice(keywords)

        await render_screen_2(query.message, db, key)

def create_application():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Register the /start command
    app.add_handler(CommandHandler("start", start_handler))

    # Register the /help command
    app.add_handler(CommandHandler("help", help_handler))

    # Register the /playlists command

    app.add_handler(CommandHandler("playlists", playlists_handler))

    # Register the /about command
    app.add_handler(CommandHandler("about", about_handler))

    # free text vibe detection
    app.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND, recommender_handler))

    # random vibe
    app.add_handler(CommandHandler("random", random_handler))

    # button click handler
    app.add_handler(CallbackQueryHandler(button_click_handler))

    # Fallback for unknown commands/message

    app.add_handler(MessageHandler(filters.COMMAND, fallback_handler))

    return app

application = create_application()
def main():
    if not BOT_TOKEN:
        print("BOT_TOKEN is missing, add it in .env file.")
        return
    print("BOT is running....")
   


if __name__ == "__main__":
    main()
