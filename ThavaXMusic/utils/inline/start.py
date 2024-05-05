from pyrogram.types import InlineKeyboardButton

import config
from ThavaXMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="❤️‍🔥 𝑨𝒅𝒅 𝑴𝒆 𝑰𝒎 𝑰𝒏𝒗𝒊𝒔𝒊𝒃𝒍𝒆 🥂",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text="❤️‍🔥 𝑯𝒆𝒍𝒑 🥂", callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text="❤️‍🔥 𝑮𝒓𝒐𝒖𝒑 🥂", url=config.SUPPORT_CHAT),
            InlineKeyboardButton(text="❤️‍🔥 𝒄𝒉𝒂𝒏𝒏𝒆𝒍 🥂", url=config.SUPPORT_CHANNEL),
        ],
       
    ]
    return buttons
