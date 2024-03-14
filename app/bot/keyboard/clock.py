from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup
from datetime import timedelta, datetime
from app.bot.keyboard.types.clock import SelectTime, ChangeTime


def get_clock(dt: datetime) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    clock_states: dict[str, timedelta] = {
        "+5 хв": timedelta(minutes=5), 
        "+10 хв": timedelta(minutes=10), 
        "+30 хв": timedelta(minutes=30), 
        "+1 год": timedelta(hours=1),
        "+1 день": timedelta(days=1),
        "-1 хв": timedelta(minutes=-1), 
        "-10 хв": timedelta(minutes=-10), 
        "-30 хв": timedelta(minutes=-30), 
        "-1 год": timedelta(hours=-1),
        "-1 день": timedelta(days=-1)
    }
    index: int = 1
    for text, timedlt in clock_states.items():
        builder.button(text=text, callback_data=ChangeTime(time=timedlt))
        if index == 5:
                builder.button(text=(dt).strftime("%d.%m.%Y, %H:%M:%S"), callback_data=SelectTime(time=dt))
        index += 1

    builder.adjust(5, 1, 5)
    return builder.as_markup()
