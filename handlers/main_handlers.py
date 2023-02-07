from create_bot import dp, bot
from aiogram import types
from keyboards import candy_grab_candy, yes_no_kb, change_total_candy_kb


@dp.message(Command(commands=['start', 'старт']))
async def start(message: types.Message):
    await message.answer('Да да, я тут.')


@dp.message(commands='help')
async def start(message: types.Message):
    kak_by_random = [123, 234, 1001]
    await message.answer('Тут будет помощь.', reply_markup=change_total_candy_kb.get_kb(kak_by_random))


@dp.callback_query(contains='kb_change_total_candy_')
async def change_total_candy(callback: types.CallbackQuery):
    await callback.message.answer('Тут будет помощь.')
    print(callback)