from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import Bot
from app.services.database_api import DatabaseAPI
from app.services.types.student import Students, Student
from typing import List
from datetime import datetime
from app.settings import settings
from app.bot.messages.admin import CELEBRANTS_MSG


class Schedule:

    def __init__(self, bot: Bot):
        self._bot = bot
        self._scheduler = AsyncIOScheduler()

    def start(self) -> None:
        self._scheduler.add_job(self.schedule, trigger="cron", day="*", hour=9)
        self._scheduler.start()

    async def schedule(self):
        celebrants: List[Student] = []
        async with DatabaseAPI() as client:
            students: Students = await client.json().get("Students")
            for student in students.values():
                date = datetime.strptime(student.get("birthday"), "%d.%m.%Y")
                if date.day == datetime.now().day and date.month == datetime.now().month:
                    celebrants.append(student)

        if celebrants:
            await self._bot.send_message(settings.CHAT_ID, await CELEBRANTS_MSG.render_async(celebrants=celebrants))
