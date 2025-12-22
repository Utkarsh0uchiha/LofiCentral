# handlers/screens.py
import random
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# ---- shared UI config ----

EMOJIS = {
    "chill": "🤙",
    "study": "📚",
    "rain": "🌧️",
    "night": "🌙",
    "jazzhop": "🎷",
    "anime": "⛩️",
    "vibe": "✨",
    "gaming": "🎮"
}

# ---- Screen 1 ----


async def render_screen_1(message, db, mode):
    # extract all unique tags
    tags = sorted(db.keys())

    buttons = []
    for tag in tags:
        emoji = EMOJIS.get(tag, "🎵")
        buttons.append(
            InlineKeyboardButton(
                text=f"{tag.capitalize()} {emoji}",
                callback_data=f"v:{tag}"
            )
        )

    keyboard = []

    for i in range(0, len(buttons), 2):
        keyboard.append(buttons[i:i+2])

    keyboard.append([
        InlineKeyboardButton(
            text="random 🎲",
            callback_data="r"
        )]
    )

    reply_markup = InlineKeyboardMarkup(keyboard)

    if(mode == "reply"):
        await message.reply_text(
            "Choose a genre 🎧",
            reply_markup=reply_markup
        )
    else:
        await message.edit_text(
            "Choose a genre 🎧",
            reply_markup=reply_markup
        )
    

# ---- Screen 2 ----
async def render_screen_2(message, db, tag):
    emoji = EMOJIS.get(tag, "🎵")
    n = len(db[tag])
    idx = random.sample(range(n), min(3, n))

    buttons = []

    for i in range(len(idx)):
            buttons.append(
                InlineKeyboardButton(
                    text=f" {emoji}  {db[tag][idx[i]]['title']}",
                    callback_data=f"p:{tag}:{idx[i]}"
                )
            )
    keyboard = []

    for i in range(len(buttons)):
        keyboard.append([buttons[i]])

    keyboard.append([
        InlineKeyboardButton(
                text="Back to Genre 🔙",
                callback_data="b:root"
            )]
        )

    reply_markup = InlineKeyboardMarkup(keyboard)

    await message.edit_text(
        f"Here are some {tag} playlists you might like 🎧",
            reply_markup=reply_markup
    )


# ---- Screen 3 ----
async def render_screen_3(message, db, tag, index):
    song = db[tag][index]
    emoji = EMOJIS.get(tag, "🎵")
    title = song['title']
    link = song['spotify']
    keyboard = []
    keyboard.append([
        InlineKeyboardButton(
            text=f"Back to {tag.capitalize()} 🔙",
            callback_data=f"b:{tag}"
        )
    ])

    reply_markup = InlineKeyboardMarkup(keyboard)
    await message.edit_text(
        f"Enjoy the vibes 🎧 \n {emoji} ** {title}**\n{link}", parse_mode="Markdown",
        reply_markup=reply_markup
    )
