from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
    [
        KeyboardButton(text="Баланс Яндекс.Директ")
    ],
    [
        KeyboardButton(text="Баланс ВК")
    ],

],
    resize_keyboard=True
)

main_menu_admin = ReplyKeyboardMarkup(
    keyboard=[
    [
        KeyboardButton(text="Добавить пользователя яндекс"),
        KeyboardButton(text="Добавить пользователя вк"),
    ],
    [
        KeyboardButton(text="Удалить пользователя яндекс"),
        KeyboardButton(text="Удалить пользователя вк")
    ],
    [
        KeyboardButton(text="Список пользователей"),
        KeyboardButton(text="Привязать пользователя к учетке")
    ]
],
    resize_keyboard=True
)