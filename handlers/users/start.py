from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from flask import request
from data.config import admins
from handlers.users.user_keyboard import *
from loader import dp
from utils.dp_api.database import *
from utils.net.yandex_request import start_server


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer("Привет, " + message.from_user.full_name.split()[0])
    user_id = message.from_user.id
    user_name = message.from_user.full_name
    for admin in admins:
        if user_id == admin:
            func = request.environ.get('werkzeug.server.shutdown')
            if func is None: start_server()
            else: pass
            await message.answer("Добро пожаловать! Вы вошли как администратор", reply_markup=main_menu_admin)

            return
        else:
            db_fill_user_table(user_id, user_name)
            await message.answer("Вы успешно добавлены в базу данных.", reply_markup=main_menu)

            return
