import json
import random
from telegram import Update
from telegram.ext import ContextTypes
from utils.smart import choose_weighted_playlist
KEYWORDS = {
    "chill": ["chill", "calm", "relax", "soft"],
    "study": ["study", "focus", "work", "concentrate", "exam"],
    "rain": ["rain", "rainy", "monsoon", "storm", "wet", "drizzle"],
    "night": ["night", "midnight", "late", "dark"],
    "jazzhop": ["jazz", "jazzhop", "sax", "smooth"],
    "anime": ["anime", "otaku", "ghibli", "waifu", "japan"],
    "vibe": ["vibe", "aesthetic", "mood", "cloudy"],
    "gaming": ["game", "gaming", "gamer", "fps", "valorant"]
}

 # load playlists.json
with open("data/playlists.json", "r", encoding="utf-8") as f:
    db = json.load(f)

async def recommender_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text.lower()

   

    matched_tags = []

    # check which tag matches user text
    for tag, keywords in KEYWORDS.items():
        for kw in keywords:
            if kw in user_text:
                matched_tags.append(tag)
                break

    if not matched_tags:
        await update.message.reply_text(
            "I couldn't detect a vibe 😔\nTry something like: 'rainy chill', 'study night', 'anime lofi'."
        )
        return

    # select the first vibe
    selected_tag = matched_tags[0]

    # pick a random playlist from that category
    playlist = choose_weighted_playlist(db[selected_tag])

    title = playlist["title"]
    link = playlist["spotify"]

    await update.message.reply_text(f"🎧 ** {title}**\n{link}", parse_mode="Markdown")

async def random_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    

    tags = []

    for vibe, keywords in db.items():
        tags.append(vibe)
    
    #randomly choosing a tag
    tag = random.choice(tags)

    #randomly choosing a playlist from the randomly choosen tag
    playlist = random.choice(db[tag])

    title = playlist["title"]
    link = playlist["spotify"]

    await update.message.reply_text(f"🎲 Random vibe drop just for you!\nMood: **{tag}** \n🎧 ** {title}**\n{link}", parse_mode="Markdown")
