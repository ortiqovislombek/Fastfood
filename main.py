from aiogram import Bot,Dispatcher,F
from environs import Env
import asyncio
import logging
dp=Dispatcher()
env=Env()
env.read_env()

async def main():
    TOKEN=env.str("TOKEN")
    bot=Bot(TOKEN)
    await dp.start_polling(bot)
if __name__=="__main__":
        logging.basicConfig(level=logging.INFO)
        try:
            asyncio.run(main())
        except Exception as err:
            print(err)    