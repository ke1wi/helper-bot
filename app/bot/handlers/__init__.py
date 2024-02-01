from aiogram import Router

from app.bot.handlers.group import router as group_router
from app.bot.handlers.private import router as private_router

router = Router(name=__name__)

router.include_routers(
    private_router,
    group_router,
)
