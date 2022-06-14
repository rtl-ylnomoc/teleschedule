from aiogram import Dispatcher

from handlers.other import cancel_state
from handlers.admin import admin_panel
from handlers.become_admin import become_admin, load_admin_finish
from handlers.client import client_kb_command, day_schedule, start_command, week_schedule, month_schedule
from handlers.client_group import load_group_finish, set_group

from models import AddAdmin, CreateDaySchedule, DeleteDaySchedule, SetGroupSchedule

from helpers import REGEXP_MAP


def register_handlers(dispatcher: Dispatcher):
    # other
    dispatcher.register_message_handler(
        cancel_state, state='*', regexp=REGEXP_MAP['cancel'])
    # become admin
    dispatcher.register_message_handler(
        become_admin, commands=['beadmin'], state=None)
    dispatcher.register_message_handler(
        load_admin_finish, state=AddAdmin.password)
    # client group
    dispatcher.register_message_handler(
        set_group, regexp=REGEXP_MAP['set_group'], state=None)
    dispatcher.register_message_handler(
        load_group_finish, state=SetGroupSchedule.group)
    # admin
    dispatcher.register_message_handler(
        admin_panel, commands=['admin'])
    # dispatcher.register_message_handler(
    #     admin_shutdown, commands=['shutdown'])
    # client
    dispatcher.register_message_handler(start_command, commands=['start'])
    dispatcher.register_message_handler(
        client_kb_command, commands=['client', 'help', 'kb'])
    dispatcher.register_message_handler(
        week_schedule, regexp=REGEXP_MAP['week_schedule'])
    dispatcher.register_message_handler(
        day_schedule, regexp=REGEXP_MAP['day_schedule'])
    dispatcher.register_message_handler(
        month_schedule, regexp=REGEXP_MAP['month_schedule'])
