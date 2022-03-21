from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from loader import dp
from utils.dp_api.database import *


@dp.message_handler(Text(contains="Добавить пользователя яндекс"))
async def add_yandex_user(message: Message):
    msg = list(message.text.split(sep=" ")[3:])
    if len(msg) < 3:
        await message.answer("Недостаточно данных. Команда должна быть в виде 'Добавить пользователя яндекс полное_имя логин пароль'.")
        return
    name = ""
    search = False
    try:
        res = ""
        for i in range(0, len(msg)-2):
            res += msg[i]
            search = db_search_user_by_fullname(name=res)
            name = res
            res += " "
    except IndexError:
        print("Error at add_yandex_user. not enough args")
        search = False
    if(search):
        db_add_yandex_user(id=db_get_user_id_by_name(name=name), login=msg[len(msg)-2], password=msg[len(msg)-1])
        await message.answer("Пользователь яндекс добавлен успешно!")
    else:
        db_add_yandex_user(id=0, login=msg[len(msg)-2], password=msg[len(msg)-1])
        await message.answer("Пользователь добавлен, но нужно привязать его к БД, т.к. пользователь всё ещё не писал боту")


@dp.message_handler(Text(contains="Добавить пользователя вк"))
async def add_vk_user(message: Message):
    msg = list(message.text.split(sep=" ")[3:])
    if len(msg) < 3:
        await message.answer("Недостаточно данных. Команда должна быть в виде 'Добавить пользователя вк полное_имя логин пароль'.")
        return
    name = ""
    search = False
    try:
        res = ""
        for i in range(0, len(msg) - 2):
            res += msg[i]
            search = db_search_user_by_fullname(name=res)
            name = res
            res += " "
    except IndexError:
        print("Error at add_vk_user. not enough args")
        search = False
    if (search):
        db_add_vk_user(id=db_get_user_id_by_name(name=name), login=msg[len(msg) - 2], password=msg[len(msg) - 1])
        await message.answer("Пользователь VK добавлен успешно!")
    else:
        db_add_vk_user(id=0, login=msg[len(msg) - 2], password=msg[len(msg) - 1])
        await message.answer(
            "Пользователь добавлен, но нужно привязать его к БД, т.к. пользователь всё ещё не писал боту")


@dp.message_handler(Text(contains="Удалить пользователя яндекс"))
async def remove_yandex_user(message: Message):
    credentials = list(message.text.split(sep=" ")[3:])
    if len(credentials) == 2:
        db_remove_yandex_user(user_login=str(credentials[0]), user_pass=str(credentials[1]))
        await message.answer(f"Пользователь {credentials[0]} {credentials[1]} удален!")
    else:
        await message.answer("Недостаточно данных. Команда должна быть в виде 'Удалить пользователя яндекс логин пароль'.")


@dp.message_handler(Text(contains="Удалить пользователя вк"))
async def remove_vk_user(message: Message):
    credentials = list(message.text.split(sep=" ")[3:])
    if len(credentials) == 2:
        db_remove_vk_user(user_login=str(credentials[0]), user_pass=str(credentials[1]))
        await message.answer(f"Пользователь {credentials[0]} {credentials[1]} удален!")
    else:
        await message.answer("Недостаточно данных. Команда должна быть в виде 'Удалить пользователя вк логин пароль'.")


@dp.message_handler(Text(equals="Список пользователей"))
async def user_list(message: Message):
    users = db_list_user()
    generator = ""
    for i in range(0, len(users)):
        generator += str(users[i][1]) + " " + str(users[i][2]) + "\n"
    await message.answer(generator)


@dp.message_handler(Text(contains="Привязать пользователя к учетке"))
async def link_user(message: Message):
    data = list(message.text.split(sep=" ")[4:])
    # 0 - service, 1 - user TG id (from list users), 2 - login, 3 - password
    if len(data) == 4:
        db_link_user(service=data[0], id=int(data[1]), login=data[2], password=data[3])
        if db_get_data_id_by_id(data[0]):
            await message.answer("Привязан успешно!")
        else:
            await message.answer("Произошла ошибка, попробуйте еще раз.")
    else:
        await message.answer("Недостаточно данных. Команда должна быть в виде 'Привязать пользователя к учетке сервис id(из списка пользователей) логин пароль'.")