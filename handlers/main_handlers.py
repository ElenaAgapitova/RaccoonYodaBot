from create_bot import dp, bot
from aiogram.filters import Command, Text
# from aiogram.types import Message, CallbackQuery
from asyncio import sleep
from aiogram import types

from keyboards import candy_grab_candy, yes_no_kb, change_candy_kb
import games.candy.game as candy_game
import games.candy.candy_text as ct
import games.hangman.hangman_text as ht
from database.db_dict import db_dict, default_for_user


@dp.message(Command(commands=['start', 'старт']))
async def start(message: types.Message):
    user_id = message.from_user.id
    db_dict[user_id] = default_for_user.copy()
    await message.answer('Привет!')


@dp.message(Command(commands=['about_candy']))
async def about_game_candy(message: types.Message):
    user_id = message.from_user.id
    await message.answer(f'{ct.about_candy_game}')
    await sleep(4)
    await bot.send_sticker(chat_id=user_id,
                           sticker=r'CAACAgIAAxkBAAEHoXlj4qq80fU4rvg8dIteBgacu3m2twACUAADR_sJDF_Z_SrDak8lLgQ')
    await message.answer(f'{ct.history_candy}')


@dp.message(Command(commands=['about_hangman']))
async def about_game_candy(message: types.Message):
    user_id = message.from_user.id
    await message.answer(f'{ht.about_game_hangman}')
    # await sleep(3)
    await bot.send_sticker(chat_id=user_id,
                           sticker=r'CAACAgIAAxkBAAEHocZj4rhLY2ni6ZjlSv_M9sOYELz2XAACGm8AAp7OCwAB528yufBoVYkuBA')
    await sleep(3)
    await message.answer(f'{ht.history_hangman}')


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
