from aiogram.types import Message
from aiogram.filters import CommandObject
from app.services.database_api import DatabaseAPI
from app.bot.messages.add_bd import FORMAT_MSG
from app.utils.date_service import DateService


async def add_birthday_admin(message: Message, command: CommandObject) -> None:
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

    if DateService.validate_date(args[0]):
        await message.answer(f"Your bd: {args[0]}\nYour alias: {args[1]}\nREPLY_MARKUP")
    else:
        await message.answer("Date is invalid")
        return

    async with DatabaseAPI() as client:
        await client.json().set("Students", "$.admin2", {"user_id": 1, "username": "cybuni", "birthday": args[0], "alias": args[1]})
