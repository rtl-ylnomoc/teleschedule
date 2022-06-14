from models import SetGroupSchedule
from keyboards import get_rkm, state_changing_rkm
from database import sql_set_group
from helpers import BOT, DEFAULT_GROUP_PASSWORD
from aiogram.types import Message
from aiogram.dispatcher import FSMContext


async def set_group(msg: Message):
    id = msg.from_user.id
    await BOT.send_message(id, 'Для текста по умолчанию пишите "ы"')
    await BOT.send_message(id, f'Пароль от расписания группы(пароль "{DEFAULT_GROUP_PASSWORD}" по умолчанию): ', reply_markup=state_changing_rkm)
    await SetGroupSchedule.group.set()


async def load_group_finish(msg: Message, state: FSMContext):
    id = msg.from_user.id
    password = msg.text if msg.text != 'ы' else DEFAULT_GROUP_PASSWORD
    await BOT.send_message(id, f'''Группа задана в соответствии с паролем: "{password}"''', reply_markup=get_rkm(id))
    await sql_set_group(id, password)
    print(id, password)
    await state.finish()