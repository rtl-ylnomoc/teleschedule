from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os
import datetime as d


PASSWORD = os.getenv('PASSWORD')

DEFAULT_GROUP_PASSWORD = 'ы' # it won't show any schedules.

REGEXP_MAP = {
    'day_schedule': r'^За день',
    'week_schedule': r'^За неделю',
    'set_group': r'^Изменить группу',
    'month_schedule': r'^За месяц',
    'cancel': r'^[оО]тмена',
}

# ADMINS = [
#     1354732510,
#     748967466
#     ]

BOT = Bot(token=os.getenv('TOKEN'))
ST = MemoryStorage()
DP = Dispatcher(BOT, storage=ST)
clear = lambda: os.system('cls')
OFFSET = d.timedelta(hours=5)
TZ = d.timezone(OFFSET, name='ЕКБ')

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')