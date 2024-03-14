
from aiogram import Bot
from aiogram.types import (
    BotCommand,
)


async def set_bot_commands(bot: Bot) -> None:
    commands = [
        BotCommand(command='start', description="Start command"),
        BotCommand(command='help', description="Help command"),
        BotCommand(command='add', description="<day.month.year> <alias>"),
        BotCommand(command='todo', description="Plan to do smth"),
    ]
    await bot.set_my_commands(commands=commands)
