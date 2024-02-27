import asyncio
import logging

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from routers.router import router


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(bot=bot)
    dp.include_router(router)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
