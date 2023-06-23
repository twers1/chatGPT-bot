import os
import openai

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
openai.api_key = os.getenv("OPENAI_API_KEY")

bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
  await message.answer('🖥Привет! Я chatGPT\n\nДля того, чтобы начать чат со мной - отправь мне запрос и я тебе отвечу')


@dp.message_handler()
async def start(message: types.Message):
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=message.text,
      temperature=0,
      max_tokens=1400,
      top_p=1,
      frequency_penalty=0.0,
      presence_penalty=0.0,
      stop=["You"]
    )

    await message.answer(response['choices'][0]['text'])


if __name__ == '__main__':
    print(
        "                                                      ████ \n ░░███                                               ░░███ \n ███████   █████ ███ █████  ██████  ████████   █████  ░███ \n░░░███░   ░░███ ░███░░███  ███░░███░░███░░███ ███░░   ░███ \n  ░███     ░███ ░███ ░███ ░███████  ░███ ░░░ ░░█████  ░███ \n  ░███ ███ ░░███████████  ░███░░░   ░███      ░░░░███ ░███ \n  ░░█████   ░░████░████   ░░██████  ░███████  ██████  █████\n   ░░░░░     ░░░░ ░░░░     ░░░░░░  ░░░░░     ░░░░░░  ░░░░░ \n                                                           \n                                                           \n                                                           \nBot started successfully")
    executor.start_polling(dp)
    print("Bot stopped")
