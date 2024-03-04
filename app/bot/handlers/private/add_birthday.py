from aiogram.types import Message
from aiogram import Bot
from aiogram.filters import CommandObject
from app.services.database_api import DatabaseAPI
from uuid import uuid4, UUID
from typing import Union, Dict
from app.bot.messages.add_bd import FORMAT_MSG, ALREADY_IN_DB_MSG
from app.utils.date_service import DateService
from aiogram.types import CallbackQuery
from app.settings import settings


async def add_birthday(message: Message, command: CommandObject) -> None:
    if not command.args:
        await message.answer(
            await FORMAT_MSG.render_async()
        )
        return

    args = command.args.split()

    if len(args) != 2:
        await message.answer(
            await FORMAT_MSG.render_async()
        )
        return

    async with DatabaseAPI() as client:
        response: Dict[Union[UUID, str], Dict[str, str]] = await client.json().get("Students")
        if response:
            if next(filter(lambda value: value.get("user_id") == message.from_user.id, response.values()), None):
                await message.answer(
                    await ALREADY_IN_DB_MSG.render_async()
                )
                return

    if date:= DateService.validate_date(args[0]):
        await message.answer(f"Your bd: {date}\nYour alias: {args[1]}\nREPLY_MARKUP")
    else:
        await message.answer("Date is invalid")
        return

    await client.json().set("Students", f"$.{uuid4()}", {"user_id": message.from_user.id, "username": message.from_user.username, "birthday": args[0], "alias": args[1]})


async def send_congrats(callback: CallbackQuery, bot: Bot):
    await bot.send_message(
        settings.CHAT_ID,
        text="Вітаю"
    )
    await callback.message.edit_text(
        "Привітав"
    )
    await callback.answer()
