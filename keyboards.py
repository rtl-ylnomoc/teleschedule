from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from database import sql_check_admin

# client keyboard
client_buttons = [KeyboardButton('За месяц'), KeyboardButton('За неделю'), KeyboardButton(
    'За день'), KeyboardButton('Изменить группу')]
client_rkm = ReplyKeyboardMarkup(resize_keyboard=True).row(*client_buttons)

# admin keyboard
admin_buttons = []
admin_rkm = ReplyKeyboardMarkup(resize_keyboard=True).row(*client_buttons)

# state changing
state_changing_buttons = [KeyboardButton('ы'), KeyboardButton('Отмена')]
state_changing_rkm = ReplyKeyboardMarkup(
    resize_keyboard=True).row(*state_changing_buttons)


def get_rkm(id, is_admin=None):
    if is_admin is not None:
        return admin_rkm if is_admin else client_rkm
    if sql_check_admin(id):
        return admin_rkm
    return client_rkm
