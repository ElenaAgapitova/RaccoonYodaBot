from aiogram import types

callback_list = ['kb_change_total_candy_' + str(x) for x in range(1000)] + \
                ['kb_change_total_candy_self']


def get_kb(values: list) -> types.InlineKeyboardMarkup:
    buttons = [
        [types.InlineKeyboardButton(text=str(values[x]) + '🍬',
                                    callback_data='kb_change_total_candy_' + str(values[x])) for x in
         range(len(values))],
        [types.InlineKeyboardButton(text='Ввести своё количество',
                                    callback_data='kb_change_total_candy_self')],
    ]
    markup = types.InlineKeyboardMarkup(inline_keyboard=buttons)

    return markup


def get_callback_list() -> list:
    return ['kb_change_total_candy_' + str(x) for x in range(1000)] + \
                    ['kb_change_total_candy_self']
