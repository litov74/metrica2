from datetime import datetime

from aiogram import Dispatcher
from utils.dp_api.database import *


# fixme
async def on_day_notify(dp: Dispatcher):
    users = db_list_user()
    while True:
        if datetime.now().strftime("%H:%M:%S") == "12:00:00":
            for user_item in users:
                await dp.bot.send_message(user_item[1], "Здравствуйте!\nВаш баланс на сегодня:\nЯндекс.Директ: {}\nВК: {}")
