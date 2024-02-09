
from aiogram import Bot
from aiogram.types import (
    BotCommand,
)


async def set_bot_commands(bot: Bot) -> None:
    commands = [
        BotCommand(command='start', description="Start command"),
        BotCommand(command='help', description="Help command"),
    ]
    await bot.set_my_commands(commands=commands)
