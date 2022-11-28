from pathlib import Path

from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, ContentType, File
from middlewares.loader import dp, bot
from utils.dp_api.database import *


#@dp.message_handler(Text(equals="Список пользователей"))
#async def user_list(message: Message):
#    users = db_list_user()
#    generator = ""
#    for i in range(0, len(users)):
#        generator += str(users[i][1]) + " " + str(users[i][2]) + "\n"
#    await message.answer(generator)


@dp.message_handler(commands="users")
async def user_list(message: Message):
    ans = db_list_user()
    lst = ""
    for res in ans:
        lst += str(res) + "\n"
    lst = lst.replace("(", "").replace(")", "").replace("'", "")
    await message.answer(lst)

@dp.message_handler(commands=["newtask", "nt", "ntask", "mk"])
async def new_task(message: Message):
    t = list(message.text.split())
    t.remove(t[0])
    try:
        assignee = t[0] + " " + t[1]
        id = db_get_user_id_by_name(assignee)
        if id == 'None': await message.answer(f"Пользователь {assignee} пока не БД. Для доб-я он должен написать /start"); return
        else:
            if t[2].lower() == "номер:" or t[2].lower() == "код:":
                code = t[3]
            text = ""
            for i in range(4, len(t)):
                text += str(t[i]) + " "
            db_add_task_to_user(id, code, text)
    except Exception:
        print(message.text)
        print(Exception)


@dp.message_handler(commands="my")
async def get_my_tasks(message: Message):
    res = db_get_tasks_by_user_id(message.from_user.id)
    #[(319268009, 'сделать то и то ', 'NNTP22-567'), (319268009, 'сделать что-то и с чем-то ', 'NNTP123-123')]
    text = ""
    task = ""
    title = ""

    for i in range(0, len(res)):
        title = "Номер: " + res[i][2] + "\n"
        task = title + res[i][1] + "\n"
        text += task + "\n"
    await message.reply(text)

async def handle_file(file: File, file_name: str, path: str):
    Path(f"{path}").mkdir(parents=True, exist_ok=True)

    await bot.download_file(file_path=file.file_path, destination=f"{path}/{file_name}")


@dp.message_handler(content_types=[ContentType.VOICE])
async def getVoice(message: Message):
    voice = await message.voice.get_file()
    path = "/files/voices"
    await handle_file(file=voice, file_name=f"{voice.file_id}.oga", path=path)
    await message.answer(str(voice))
    print(voice)
