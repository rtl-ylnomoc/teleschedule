from aiogram.dispatcher.filters.state import State, StatesGroup


class CreateDaySchedule(StatesGroup):
    group = State()
    day = State()
    lesson_num = State()
    schedule = State()


class DeleteDaySchedule(StatesGroup):
    group = State()
    day = State()
    

class SetGroupSchedule(StatesGroup):
    group = State()


class AddAdmin(StatesGroup):
    password = State()