from handlers import dp
from create_bot import bot_start


async def on_start(_):
    print('Bot started')


if __name__ == '__main__':
    bot_start()
