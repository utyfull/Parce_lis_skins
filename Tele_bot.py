
import json
import time

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hbold, hlink

from main import collect_data

Token = '6178547206:AAGJuUA6qxzKH9ejmZsK4dtKG10tiytBHXU'

bot = Bot(token=Token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands='start')
async def start_handler(message: types.Message):
    start_button = ['Pages: 1', 'Pages: 2', 'Pages: 5', 'Pages: 10']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_button)

    await message.reply('How much pages?', reply_markup=keyboard)

    @dp.message_handler(Text(equals='Pages: 1'))
    async def get_discount_skins(message: types.Message):
        await message.answer('Please waiting...')
        pages = 1

        collect_data(pages)

        with open('result.json') as file:
            data = json.load(file)

        for index, item in enumerate(data):
            card = f'{hlink(item.get("name"), item.get("href"))}\n' \
                   f'{hlink(item.get("name"), item.get("link"))}\n' \
                   f'{hbold("Discount: ")}{item.get("discount")}\n' \
                   f'{hbold("Price_first: ")}{item.get("price_first")}\n' \
                   f'{hbold("Price_second: ")}{item.get("price_second")}'

            if index % 1 == 0:
                time.sleep(5)

            await message.answer(card)

    @dp.message_handler(Text(equals='Pages: 2'))
    async def get_discount_skins(message: types.Message):
        await message.answer('Please waiting...')
        pages = 2

        collect_data(pages)

        with open('result.json') as file:
            data = json.load(file)

        for index, item in enumerate(data):
            card = f'{hlink(item.get("name"), item.get("href"))}\n' \
                   f'{hlink(item.get("name"), item.get("link"))}\n' \
                   f'{hbold("Discount: ")}{item.get("discount")}\n' \
                   f'{hbold("Price_first: ")}{item.get("price_first")}\n' \
                   f'{hbold("Price_second: ")}{item.get("price_second")}'

            if index % 1 == 0:
                time.sleep(5)

            await message.answer(card)

    @dp.message_handler(Text(equals='Pages: 5'))
    async def get_discount_skins(message: types.Message):
        await message.answer('Please waiting...')
        pages = 5

        collect_data(pages)

        with open('result.json') as file:
            data = json.load(file)

        for index, item in enumerate(data):
            card = f'{hlink(item.get("name"), item.get("href"))}\n' \
                   f'{hlink(item.get("name"), item.get("link"))}\n' \
                   f'{hbold("Discount: ")}{item.get("discount")}\n' \
                   f'{hbold("Price_first: ")}{item.get("price_first")}\n' \
                   f'{hbold("Price_second: ")}{item.get("price_second")}'

            if index % 1 == 0:
                time.sleep(5)

            await message.answer(card)

    @dp.message_handler(Text(equals='Pages: 10'))
    async def get_discount_skins(message: types.Message):
        await message.answer('Please waiting...')
        pages = 10

        collect_data(pages)

        with open('result.json') as file:
            data = json.load(file)

        for index, item in enumerate(data):
            card = f'{hlink(item.get("name"), item.get("href"))}\n' \
                   f'{hlink(item.get("name"), item.get("link"))}\n' \
                   f'{hbold("Discount: ")}{item.get("discount")}\n' \
                   f'{hbold("Price_first: ")}{item.get("price_first")}\n' \
                   f'{hbold("Price_second: ")}{item.get("price_second")}'

            if index % 20 == 0:
                time.sleep(5)

            await message.answer(card)

executor.start_polling(dp)
