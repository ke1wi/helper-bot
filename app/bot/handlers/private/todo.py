from aiogram.types import Message
from app.services.database_api import DatabaseAPI
from aiogram.fsm.context import FSMContext
from app.utils.date_service import DateService
from app.bot.states.todo import Todo
from aiogram.enums.content_type import ContentType


async def todo_command(message: Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer(f"Напиши, що треба зробити)")
    await state.set_state(Todo.text)



async def todo_text(message: Message, state: FSMContext) -> None:
    if message.content_type != ContentType.TEXT:
        await message.answer(f"Дякую, що поділився, але мені треба текст)")
        await state.clear()
        return
    
    await state.set_data({"todo_text": message.text})
    await message.answer("Супер, тепер дедлайн в форматі дд.мм.рррр")
    await state.set_state(Todo.deadline)


async def todo_deadline(message: Message, state: FSMContext) -> None:
    if message.content_type != ContentType.TEXT:
        await message.answer(f"Дякую, що поділився, але мені треба текст)")
        return
    
    if date:= DateService.validate_date(message.text):
        await state.update_data({"deadline": date})
    else:
        await message.answer("Date is invalid")
        await state.clear()
        return
    
    data = await state.get_data()
    await message.answer(f"Full data: \nText: {data.get('todo_text')}\nDeadline: {data.get('deadline')}")




    # async with DatabaseAPI() as collection:
    #     await collection.insert_one({
    #         "name": "Vova"
    #     })
