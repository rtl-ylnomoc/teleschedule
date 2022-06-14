from handlers import register_handlers
# from handlers.other import bot_starting_message
from helpers import BOT, DP
from database import sql_get_user_ids, sql_start, sql_stop
from aiogram.utils.executor import start_polling
import locale


async def startup(_):
    print(f'[BOT STARTS] from {__name__}')
    sql_start()
    sql_get_user_ids()
    # for user_id, is_admin in sql_get_user_ids(): # uncomment in prod
    #     await bot_starting_message(user_id, is_admin)
    # # await BOT.close_bot()


async def shutdown(_):
    sql_stop()
    print('[BOT STOPS]')


if __name__ == 'source':
    locale.setlocale(locale.LC_ALL, 'ru_RU.UTF8')
    register_handlers(DP)
    start_polling(DP, skip_updates=True, on_startup=startup, on_shutdown=shutdown)

