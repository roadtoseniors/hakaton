from aiogram.types import(
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

main_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='help', callback_data='help'),
            InlineKeyboardButton(text='form', callback_data='form')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

reset_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Пройти опрос заново', callback_data='reset'),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)