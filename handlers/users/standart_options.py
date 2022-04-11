from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from data.config import admins
from loader import dp
from utils.dp_api.database import *


@dp.message_handler(Text(equals="Баланс Яндекс.Директ"))
async def coins_yandex(message: Message):
    if message.from_user.id not in admins:
        if db_get_data_id_by_id(message.from_user.id):
            await message.answer("На вашем балансе Яндекс.Директ столько денег")
        else:
            await message.answer("Ваша учетная запись еще не готова.")


@dp.message_handler(Text(equals="Баланс ВК"))
async def coins_yandex(message: Message):
    if message.from_user.id not in admins:
        if db_get_data_id_by_id(message.from_user.id):
            await message.answer("На вашем балансе ВК столько денег")
        else:
            await message.answer("Ваша учетная запись еще не готова.")
