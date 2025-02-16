import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters.command import Command
from aiogram.types import Message
from dotenv import dotenv_values
from users.users import read_user_config, write_user_config

config = dotenv_values()
bot = Bot(token=config["BOT_TOKEN"])
dp = Dispatcher()

@dp.message(Command('start'))
async def cmd_start(message):
    user = message.from_user
    user_id = user.id
    user_config = {
        'first_name': user.first_name,
        'adresses': [],
        'cashback_points': 0,
    }

    write_user_config(user_id=user_id, config=user_config)
    await message.reply(f'Добро пожаловать в магазин обуви "Кефтеме"!', {user.first_name})

async def main():
    print('Polling started')
    await dp.start_polling(bot)



asyncio.run(main())