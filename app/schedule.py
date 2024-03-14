from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import Bot
from app.services.database_api import DatabaseAPI
from app.services.types.student import Students, Student
from typing import List
from datetime import datetime
from app.settings import settings
from app.bot.messages.admin import CELEBRANTS_MSG
import logging
from app.bot.keyboard.approve_keyboards import get_approve_birthday_keyboard


class Schedule:

    def __init__(self, bot: Bot):
        self._bot = bot
        self._scheduler = AsyncIOScheduler()

    def start(self) -> None:
        # self._scheduler.add_job(self.schedule, trigger="cron", day="*", hour=9)
        # self._scheduler.add_job(self.schedule, trigger="interval", seconds=20)
        self._scheduler.start()

        
