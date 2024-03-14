from aiogram.types import Message, CallbackQuery
from app.services.database_api import DatabaseAPI
from aiogram.fsm.context import FSMContext
from app.utils.date_service import DateService
from app.bot.states.todo import Todo
from aiogram.enums.content_type import ContentType
from app.bot.keyboard.todo_type_keyboard import get_todo_type_keyboard
from app.bot.keyboard.approve_keyboards import get_approve_todo_keyboard
from app.bot.keyboard.types.todo import SelectTodoType
from app.bot.keyboard.types.approves import TodoApprove
from app.bot.keyboard.types.clock import ChangeTime, SelectTime
from app.bot.keyboard.clock import get_clock
from datetime import datetime, timedelta


async def todo_command(message: Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer(f"Напиши, що треба зробити)")
    await state.set_data({"telegram_id": message.from_user.id})
    await state.set_state(Todo.description)


async def todo_description(message: Message, state: FSMContext) -> None:
    if message.content_type != ContentType.TEXT:
        await message.answer(f"Дякую, що поділився, але мені треба текст)")
        await state.clear()
        return

    await state.update_data({"description": message.text})
    await message.answer("Супер, тепер дедлайн в форматі дд.мм.рррр")
    await state.set_state(Todo.deadline)


async def todo_deadline(message: Message, state: FSMContext):
    if message.content_type != ContentType.TEXT:
        await message.answer(f"Дякую, що поділився, але мені треба текст)")
        await state.clear()
        return

    if date := DateService.validate_date(message.text):
        await state.update_data({"deadline": date})
        data = await state.get_data()
        await message.answer(
            f"Вибери тип: \nText: {data.get('description')}\nDeadline: {data.get('deadline')}",
            reply_markup=get_todo_type_keyboard()
        )
    else:
        await message.answer("Дата неправильна!")
        await state.clear()
        return


async def todo_type(callback: CallbackQuery, callback_data: SelectTodoType, state: FSMContext):
    await state.update_data({"todo_type": callback_data.todo_type})
    await state.update_data({"remind_in": datetime.now() - timedelta(hours=3)})
    data = await state.get_data()
    await callback.message.edit_text(
        "За скільки Тобі нагдати" if callback_data == "REMIDER" else "За скільки Тобі нагадати про дедлайн",
        reply_markup=get_clock(data.get('remind_in'))
    )


async def refresh_clock(callback: CallbackQuery, callback_data: ChangeTime, state: FSMContext):
    data = await state.get_data()
    dt: datetime = data.get('remind_in') + callback_data.time
    await callback.message.edit_reply_markup(
        reply_markup=get_clock(dt)
    )
    await state.update_data({"remind_in": dt})
    await callback.answer()


async def select_time(callback: CallbackQuery, callback_data: SelectTime, state: FSMContext):
    await state.update_data({"remind_in": callback_data.time})
    await callback.message.edit_text(
        "Якщо все окей, Тицяй!",
        reply_markup=get_approve_todo_keyboard()
    )


async def todo_status(callback: CallbackQuery, callback_data: TodoApprove, state: FSMContext):
    if callback_data.done:
        await state.set_state(Todo.migrate)
    await callback.answer()


async def todo_migrate(state: FSMContext) -> None:
    data = await state.get_data()

    async with DatabaseAPI() as client:
        collection = client.get_database("HelperBot").get_collection("TODO")
        if collection.find_one({"telegram_id": f"{data.get('telegram_id')}"}):
            new_task = {
                "type": data.get('todo_type'),
                "description": data.get('description'),
                "deadline": data.get('deadline'),
                "remind_in": data.get('remind_in')
            }
            collection.update_one({"telegram_id": f"{data.get('telegram_id')}"},
                                  {"$push": {"tasks": new_task}})
        else:
            collection.insert_one({
                "telegram_id": f"{data.get('telegram_id')}",
                "tasks": [
                    {
                        "type": data.get('todo_type'),
                        "description": data.get('description'),
                        "deadline": data.get('deadline'),
                        "remind_in": data.get('remind_in')
                    }
                ]
            })
    await state.clear()
