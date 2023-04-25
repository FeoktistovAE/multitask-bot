from aiogram.dispatcher.filters.state import StatesGroup, State


class CurrencyStatesGroup(StatesGroup):
    convert_from_state = State()
    convert_to_state = State()
    final_state = State()
