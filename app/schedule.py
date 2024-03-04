from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import Bot
from app.services.database_api import DatabaseAPI
from app.services.types.student import Students, Student
from typing import List
from datetime import datetime
from app.settings import settings
from app.bot.messages.admin import CELEBRANTS_MSG
import logging
from app.bot.keyboard.types.approve_birthday_keyboard import get_approve_birthday_keyboard


class Schedule:

    def __init__(self, bot: Bot):
        self._bot = bot
        self._scheduler = AsyncIOScheduler()

    def start(self) -> None:
        # self._scheduler.add_job(self.schedule, trigger="cron", day="*", hour=9)
        self._scheduler.add_job(self.schedule, trigger="interval", seconds=20)
        self._scheduler.start()

    async def schedule(self):
        celebrants: List[Student] = []
        async with DatabaseAPI() as client:
            students: Students = await client.json().get("Students")
            for student in students.values():
                date = datetime.strptime(student.get("birthday"), "%d.%m.%Y")
                logging.info(f"\nDay: {date.day}\nMonth {date.month}\n"+"---"*10)
                if date.day == datetime.now().day and date.month == datetime.now().month:
                    celebrants.append(student)

        logging.info(celebrants)
        if celebrants:
            await self._bot.send_message(
                settings.CHAT_ID,
                await CELEBRANTS_MSG.render_async(celebrants=celebrants), 
                reply_markup=get_approve_birthday_keyboard()
            )
