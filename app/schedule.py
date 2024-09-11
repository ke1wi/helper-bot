from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import Bot


class Schedule:

    def __init__(self, bot: Bot):
        self._bot = bot
        self._scheduler = AsyncIOScheduler()

    def start(self) -> None:
        # self._scheduler.add_job(self.schedule, trigger="cron", day="*", hour=9)
        # self._scheduler.add_job(self.schedule, trigger="interval", seconds=20)
        self._scheduler.start()

        
