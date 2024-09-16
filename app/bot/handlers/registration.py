from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from app.utils.callbacks.registration import Approve
from app.utils.database.models.user import User
import re
from app.bot.keyboards.registration import (
    registration_cancel_keyboard,
    registration_keyboard,
)

from app.utils.states.registration import Registration
from app.utils.callbacks.registration import Cancel
from app.bot.messages.registration import REGISTRATION_MSG
from app.utils.database.api import create_user, get_user_by_email


async def reg(message: Message, state: FSMContext) -> None:
    await message.answer("Введіть електронну пошту:", reply_markup=registration_cancel_keyboard())
    await state.set_state(Registration.email)
    await state.update_data(
        {"telegram_id": message.from_user.id, "name": message.text, "first_message_id": message.message_id}
    )


async def cancel(
    callback: CallbackQuery,
    callback_data: Cancel,
    state: FSMContext,
) -> None:
    data = await state.get_data()
    last_message_id: int = callback.message.message_id
    first_message_id: int = data.get("first_message_id")
    await callback.bot.delete_messages(
        callback.message.chat.id, [i for i in range(first_message_id, last_message_id)]
    )
    await callback.message.edit_text("Відміняю ❌")
    await state.clear()
    await callback.answer()

async def email(message: Message, state: FSMContext) -> None:
    email = message.text
    if re.fullmatch(
        r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b", email
    ):
        if not await get_user_by_email(email):
            await state.update_data({"email": email})
            await message.answer(
                "Введіть імʼя:",
                reply_markup=registration_cancel_keyboard(),
            )
            await state.set_state(Registration.name)
        else:
            data = await state.get_data()
            last_message_id: int = message.message_id
            first_message_id: int = data.get("first_message_id")
            await message.bot.delete_messages(
                message.chat.id, [i for i in range(first_message_id + 1, last_message_id + 1)]
            )
            await message.answer("Вже є в базі")
            await state.clear()
    else:
        await message.answer(
            "Електронна пошта неправильна\nВведіть електронну пошту ще раз:",
            reply_markup=registration_cancel_keyboard(),
        )


async def name(message: Message, state: FSMContext) -> None:
    await state.update_data({"name": message.text})
    await message.answer(
        "Введіть прізвище:", reply_markup=registration_cancel_keyboard()
    )
    await state.set_state(Registration.surname)


async def surname(message: Message, state: FSMContext) -> None:
    await state.update_data({"surname": message.text})
    await message.answer(
        "Введіть телефон:\nПриклад: <b>0501234567</b>", reply_markup=registration_cancel_keyboard()
    )
    await state.set_state(Registration.number)


async def number(message: Message, state: FSMContext) -> None:
    number: str = message.text
    await message.answer(number)
    if "+38" not in number:
        number = "+38" + number
    if re.fullmatch(r"^\+?38\s?0\d{2}\s?\d{3}\s?\d{2}\s?\d{2}$", number):
        await state.update_data({"number": number})
        data = await state.get_data()
        await message.answer(
            await REGISTRATION_MSG.render_async(
                name=data.get("name"),
                surname=data.get("surname"),
                email=data.get("email"),
                number=data.get("number")
                ),
            reply_markup=registration_keyboard()
        )
    else:

        await message.answer(
            "Номер телефону неправильний\nВведіть телефон ще раз:",
            reply_markup=registration_cancel_keyboard(),
        )


async def approve(
    callback: CallbackQuery, callback_data: Approve, state: FSMContext
) -> None:
    data = await state.get_data()
    await create_user(
        User(
            telegram_id=data.get("telegram_id"),
            name=data.get("name"),
            surname=data.get("surname"),
            email=data.get("email"),
            number=data.get("number")
        )
    )
    data = await state.get_data()
    last_message_id: int = callback.message.message_id
    first_message_id: int = data.get("first_message_id")
    await callback.bot.delete_messages(
        callback.message.chat.id, [i for i in range(first_message_id, last_message_id)]
    )
    await callback.message.edit_text(f"Юзер <b>{data.get("surname")} {data.get("name")}</b> успішно зарєєстрований!")
    await callback.answer()
    await state.clear()
