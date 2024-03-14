from datetime import datetime, timedelta

from aiogram.filters.callback_data import CallbackData


class ChangeTime(CallbackData, prefix="change_time"):
    time: timedelta


class SelectTime(CallbackData, prefix="select_time", sep="#"):
    time: datetime
