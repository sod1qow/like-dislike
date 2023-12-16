from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def get_text_inline_btn():
    btn = InlineKeyboardMarkup(row_width=2)
    btn.add(
        InlineKeyboardButton(text="👍", callback_data="like"),
        InlineKeyboardButton(text="👎", callback_data="dislike")
    )

    return btn
