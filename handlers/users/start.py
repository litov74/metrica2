from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from flask import request
from data.config import admins
from middlewares.loader import dp
from utils.dp_api.database import *


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer("Привет, " + message.from_user.full_name.split()[0])
    user_id = message.from_user.id
    user_name = message.from_user.full_name

    if user_id in admins:
        await message.answer("Добро пожаловать! Вы вошли как администратор")
        return
    else:
        if not db_search_user_by_fullname(user_name):
            db_fill_user_table(user_id, user_name)
            await message.answer("Вы успешно добавлены в базу данных.")
        else:
            await message.answer("Вы уже в БД.")
        return

