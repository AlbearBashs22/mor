from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup



def botplaylist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(text=_["O7_05"], url=SUPPORT_CHAT),
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close"),
        ],
    ]
    return buttons


def close_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                ),
            ]
        ]
    )
    return upl
