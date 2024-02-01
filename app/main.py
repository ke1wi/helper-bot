import logging
from app.bot.api.factory import create_app
from app.factory import create_bot, create_dispatcher
from app.settings import settings

bot = create_bot(token=settings.TOKEN.get_secret_value())
dispatcher = create_dispatcher()
app = create_app(
    bot=bot,
    dispatcher=dispatcher,
    webhook_secret=settings.TELEGRAM_SECRET.get_secret_value(),
)
logging.basicConfig(level="DEBUG")

# async def rm():
#     os.remove("table/table_for_bot.csv")


# @App.dp.message_handler(commands=['checkdr'], commands_prefix=['~'])
# async def check_dr(msg: types.Message):
#     await App.bot.send_message(Settings.ADMIN_ID, Logic.check())


# @App.dp.message_handler(commands=['sendcong'], commands_prefix=['~'])
# async def congrats(msg: types.Message):
#     await App.bot.send_message(Settings.CHAT_ID, Logic.send_congrats())

# logging.basicConfig(level=logging.INFO)


# async def main() -> None:
#     await App.dp.start_polling(App.bot, drop_pending_updates=True)
# if __name__ == "__main__":
#     asyncio.run(main())
