from aiogram.types import Message, CallbackQuery
from app.bot.messages.general import START_MSG
from aiogram import Bot
from aiogram.fsm.context import FSMContext



async def start(message: Message, state: FSMContext) -> None:
    await message.answer(
        await START_MSG.render_async()
    )
    

async def ignore(callback: CallbackQuery):
    await callback.message.edit_text("Ігнорую")
    await callback.answer()