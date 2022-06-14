from keyboards import get_rkm
from helpers import BOT
from aiogram.types import Message
from aiogram.dispatcher import FSMContext


async def cancel_state(msg: Message, state: FSMContext):
    id = msg.from_user.id
    cur_state = await state.get_state()
    if cur_state is None:
        print('Canceled None')
        return
    await state.finish()
    await BOT.send_message(id, f"Операция отменена успешно.", reply_markup=get_rkm(id))


# async def bot_stopping_message(id, is_admin):
#     await BOT.send_message(id, f"Бот выключается.", reply_markup=get_rkm(id, is_admin))


# async def bot_starting_message(id, is_admin):
#     await BOT.send_message(id, f"Бот включается.", reply_markup=get_rkm(id, is_admin))