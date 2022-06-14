from database import sql_get_admins
from keyboards import admin_rkm
from helpers import BOT
from aiogram.types import Message


async def admin_panel(msg: Message):
    id = msg.from_user.id
    if msg.from_user.id not in sql_get_admins():
        await BOT.send_message(id, 'Нет прав доступа.')
        return
    await BOT.send_message(id, 'Админская панель.', reply_markup=admin_rkm)


# async def admin_shutdown(msg: Message):
#     id = msg.from_user.id
#     if msg.from_user.id not in sql_get_admins():
#         await BOT.send_message(id, 'Нет прав доступа.')
#         return
#     await BOT.send_message(id, 'Выключаю-с.', reply_markup=admin_rkm)
#     # await dp.wait_closed()
#     dp.stop_polling()
#     await BOT.close_bot()
#     await BOT.close_bot()