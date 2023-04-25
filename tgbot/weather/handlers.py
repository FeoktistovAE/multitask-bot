import requests
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

from tgbot.weather.states import WeatherStatesGroup
from tgbot.services.keyboards import get_cancel_cmd
from tgbot.weather.api import get_request_link
from tgbot.weather.declension import change_declension


DEGREE_SIGN = u'\N{DEGREE SIGN}'


async def start_weather(message: types.Message) -> None:
    await WeatherStatesGroup.send_weather.set()
    await message.answer(
        'Введите город, чтобы узнать погоду в нем',
        reply_markup=get_cancel_cmd(),
    )


def register_start_weather(dp: Dispatcher):
    dp.register_message_handler(start_weather, Text(equals="Узнать погоду"), state=None)


async def send_weather(message: types.Message):
    request_link = get_request_link(message.text)
    content = requests.get(request_link).json()
    try:
        city_name = content['name']
    except KeyError:
        await message.answer(
            'Прости, но я не знаю такого города. Попробуй еще раз!'
        )
    weather_description = content['weather'][0]['description']
    temp_min = content['main']['temp_min']
    temp_max = content['main']['temp_max']
    feels_like = content['main']['feels_like']
    current_temp = content['main']['temp']
    changed_declension = change_declension(city_name)
    wind_speed = content['wind']['speed']
    country = content['sys']['country']
    text = (f'Сегодня в {changed_declension} ({country}) {weather_description}. '
            f'Температура воздуха составляет {current_temp} градусов по Цельсию '
            f'(ощущется как {feels_like}{DEGREE_SIGN}C) '
            f'Температура колеблется между {temp_min} и {temp_max}{DEGREE_SIGN}С. '
            f'Скорость ветра составляет {wind_speed} м/c.')
    await message.answer(text, reply_markup=get_cancel_cmd())


def register_send_weather(dp: Dispatcher):
    dp.register_message_handler(send_weather, state=WeatherStatesGroup.send_weather)
