import asyncio
import logging
import os
from app.bot import App
from app.settings import Settings
from aiogram import types
from app.logic import Logic


async def rm():
    os.remove("table/table_for_bot.csv")


@App.dp.message_handler(commands=['checkdr'], commands_prefix=['~'])
async def check_dr(msg: types.Message):
    await App.bot.send_message(Settings.ADMIN_ID, Logic.check())


@App.dp.message_handler(commands=['sendcong'], commands_prefix=['~'])
async def congrats(msg: types.Message):
    await App.bot.send_message(Settings.CHAT_ID, Logic.send_congrats())

logging.basicConfig(level=logging.INFO)


async def main() -> None:
    await App.dp.start_polling(App.bot, drop_pending_updates=True)
if __name__ == "__main__":
    asyncio.run(main())
