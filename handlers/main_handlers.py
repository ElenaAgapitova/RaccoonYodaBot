from create_bot import dp, bot
from aiogram.filters import Command, Text
# from aiogram.types import Message, CallbackQuery

from aiogram import types

from keyboards import candy_grab_candy, yes_no_kb, change_candy_kb
import games.candy.game as candy_game
from database.db_dict import db_dict, default_for_user


@dp.message(Command(commands=['start', 'старт']))
async def start(message: types.Message):
    user_id = message.from_user.id
    db_dict[user_id] = default_for_user.copy()
    await bot.send_sticker(chat_id=user_id,
                           sticker=r'CAACAgIAAxkBAAEHnLRj4WioWMoa681p9WDASaNu5HciNgAC4wMAApzW5wrxvCnqcyLhQC4E')
    await message.answer('Привет, я Йода!')


@dp.message(Command(commands=['test_choice_step']))
async def test(message: types.Message):
    user_id = message.from_user.id
    step_list = candy_game.get_step_list(10)
    await message.answer('Выбери кол-во конфет за ход.',
                         reply_markup=change_candy_kb.get_kb(step_list, 'step'))


@dp.message(Command(commands=['test_choice_total']))
async def test(message: types.Message):
    user_id = message.from_user.id
    step_list = candy_game.get_total_list(db_dict[user_id]['candy']['step'])
    await message.answer('Выбери кол-во конфет на столе.',
                         reply_markup=change_candy_kb.get_kb(step_list, 'total'))


@dp.callback_query(Text(startswith='kb_candy_change_'))
async def change_total_candy(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    data = callback.data.split('_')
    action = data[-2]
    value = int(data[-1])
    await callback.message.answer(f'Ты выбрал изменить {action} на {value}.')
    db_dict[user_id]['candy'][action] = value
    print(db_dict)
