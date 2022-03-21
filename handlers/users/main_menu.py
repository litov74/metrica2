from loader import dp
from aiogram.types import Message
from aiogram.dispatcher.filters import Text


@dp.message_handler(Text(equals="инфо"))
async def open_information(message: Message):
    await message.answer("Тут скоро будет информация о клубе")


@dp.message_handler(Text(equals="Баланс Яндекс.Директ"))
async def yandex_coin_info(message: Message):
    await message.answer("Вы выбрали яндекс. Запрашиваем информацию...")


@dp.message_handler(Text(equals="Баланс ВК"))
async def vk_coin_info(message: Message):
    await message.answer("вк выбран. Запрашиваем информацию...")

