from aiogram import Bot, Dispatcher
from os import getenv

# TOKEN = ''
TOKEN = getenv('TOKEN')

dp = Dispatcher()
bot = Bot(token=TOKEN, parse_mode='html')


def bot_start():
    print('Bot started')
    dp.run_polling(bot)
