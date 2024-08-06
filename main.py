import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from routers import router as main_router

import config
from config import settings


async def main():

    logging.basicConfig(level=logging.INFO)

    dp = Dispatcher()
    dp.include_router(main_router)
    bot = Bot(
        token=config.settings.bot_token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
