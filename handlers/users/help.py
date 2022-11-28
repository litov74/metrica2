from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from middlewares.loader import dp
from utils.misc import rate_limit


@rate_limit(5, 'help')
@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = [
        'Список команд: ',
        '/start - Начать диалог',
        '/help - Получить справку',
        '/frequency - Частота отправки сообщений',
        '\n\nчтобы добавить задачу пользователю, пиши',
        'Задача для {Полное имя как в Мессенджере}',
        'Номер: {Номер, если есть}',
        'текст задачи',
    ]
    await message.answer('\n'.join(text))
