from aiogram.dispatcher.filters.state import StatesGroup, State


class WeatherStatesGroup(StatesGroup):
    send_weather = State()