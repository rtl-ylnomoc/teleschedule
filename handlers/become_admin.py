from database import sql_add_admin, sql_get_admins
from keyboards import admin_rkm, state_changing_rkm, client_rkm
from helpers import BOT, PASSWORD
from aiogram.types import Message
from models import AddAdmin
from aiogram.dispatcher import FSMContext


# for bot group
async def become_admin(msg: Message):
    id = msg.from_user.id
    if id in sql_get_admins():
        await BOT.send_message(id, 'Уже админ.', reply_markup=admin_rkm)
        return
    print(f'BEADMIN {id}')
    await BOT.send_message(id, 'Введите пароль.', reply_markup=state_changing_rkm)
    await AddAdmin.password.set()


async def load_admin_finish(msg: Message, state: FSMContext):
    id = msg.from_user.id
    if msg.text == PASSWORD:
        sql_add_admin(id)
        await BOT.send_message(id, 'Админуй.', reply_markup=admin_rkm)
    else:
        await BOT.send_message(id, 'Неверный пароль.', reply_markup=client_rkm)
    await state.finish()