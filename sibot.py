import asyncio
from telegram import Bot
from dotenv import load_dotenv
import os


async def send_message(bot, chat_id):
    await bot.send_message(chat_id=chat_id, text='Hello, greetings!', parse_mode='Markdown')
    print('Message sent')


async def main():
    load_dotenv()
    token = os.environ['TG_BOT_TOKEN']
    chat_id = os.environ['TG_CHAT_ID']

    bot = Bot(token=token)
    await send_message(bot, chat_id)


if __name__ == '__main__':
    asyncio.run(main())