from aiogram.types import Message

from helpers import BOT, TZ
from database import sql_get_user, sql_read_day, get_user_group, sql_set_group
from keyboards import get_rkm, state_changing_rkm

import datetime as d
import calendar as cal

from models import SetGroupSchedule


async def start_command(msg: Message):
    id = msg.from_user.id
    if not sql_get_user(id):
        await BOT.send_message(id, f'Пароль от расписания группы: ', reply_markup=state_changing_rkm)
        await SetGroupSchedule.group.set()
        return
    await BOT.send_message(id, 'Вы разбудили бота.', reply_markup=get_rkm(id))


async def client_kb_command(msg: Message):
    id = msg.from_user.id
    await BOT.send_message(id, 'Клиентская панель.', reply_markup=get_rkm(id))


async def day_schedule(msg: Message):
    id = msg.from_user.id
    group = get_user_group(id)
    day = d.datetime.now(tz=TZ)
    print(id, group, day.strftime('%Y-%m-%d, %H:%M:%S'))
    scheday = sql_read_day(group, day.strftime('%Y-%m-%d'))
    if scheday:
        scheday_string = '\n'
        for cl in scheday:
            scheday_string += f'{cl[0]} {cl[1]} {cl[4]} ({cl[2]})\n'
    else:
        print(scheday)
        scheday_string = 'ы'
    await BOT.send_message(id, f"День: {day.strftime('%Y-%m-%d, %A')},\nрасписание: {scheday_string}", reply_markup=get_rkm(id))


async def week_schedule(msg: Message):
    id = msg.from_user.id
    now = d.datetime.now(tz=TZ)
    group = get_user_group(id)
    for i in range(7):
        day = now-d.timedelta(days=now.weekday()-i)
        print(id, group, day.strftime('%Y-%m-%d, %H:%M:%S'))
        scheday = sql_read_day(group, day.strftime('%Y-%m-%d'))
        if scheday:
            scheday_string = '\n'
            for cl in scheday:
                scheday_string += f'{cl[0]} {cl[1]} {cl[4]} ({cl[2]})\n'
        else:
            print(scheday)
            scheday_string = 'ы'
        await BOT.send_message(id, f"День: {day.strftime('%Y-%m-%d, %A')},\nрасписание: {scheday_string}", reply_markup=get_rkm(id))


async def month_schedule(msg: Message):
    id = msg.from_user.id
    now = d.datetime.now(tz=TZ)
    group = get_user_group(id)
    _, days_in_month = cal.monthrange(now.year, now.month)
    print(days_in_month, type(days_in_month))
    for i in range(days_in_month):
        day = now-d.timedelta(days=now.day-i-1)
        print(day.strftime('%Y-%m-%d, %H:%M:%S'), days_in_month)
        scheday = sql_read_day(group, day.strftime('%Y-%m-%d'))
        if scheday:
            scheday_string = '\n'
            for cl in scheday:
                scheday_string += f'{cl[0]} {cl[1]} {cl[4]} ({cl[2]})\n'
        else:
            print(scheday)
            scheday_string = 'ы'
        await BOT.send_message(id, f"День: {day.strftime('%Y-%m-%d, %A')},\nрасписание: {scheday_string}", reply_markup=get_rkm(id))