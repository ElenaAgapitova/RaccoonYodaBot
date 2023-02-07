from aiogram import types


def get_kb(values: list, param: str) -> types.InlineKeyboardMarkup:
    buttons = [
        [types.InlineKeyboardButton(text=str(values[x]) + '🍬',
                                    callback_data='kb_candy_change_' + param +
                                                  '_' + str(values[x])) for x in
         range(len(values))],
    ]
    markup = types.InlineKeyboardMarkup(inline_keyboard=buttons)

    return markup
