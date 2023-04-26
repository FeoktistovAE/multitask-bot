import requests
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

from tgbot.weather.states import WeatherStatesGroup
from tgbot.services.keyboards import get_cancel_cmd
from tgbot.weather.api import get_weather_data
from tgbot.weather.city_case import  change_city_case


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
    weather_data = get_weather_data(message.text)
    try:
        city_name = weather_data['name']
    except KeyError:
        await message.answer(
            'Прости, но я не знаю такого города. Попробуй еще раз!',
            reply_markup=get_cancel_cmd(),
        )
    weather_description = weather_data['weather'][0]['description']
    temp_min = weather_data['main']['temp_min']
    temp_max = weather_data['main']['temp_max']
    feels_like = weather_data['main']['feels_like']
    current_temp = weather_data['main']['temp']
    changed_declension = change_city_case(city_name)
    wind_speed = weather_data['wind']['speed']
    country = weather_data['sys']['country']
    text = (f'На данный момент в {changed_declension} ({country}) {weather_description}. '
            f'Температура воздуха составляет {current_temp} градусов по Цельсию '
            f'(ощущется как {feels_like}{DEGREE_SIGN}C) '
            f'Температура колеблется между {temp_min} и {temp_max}{DEGREE_SIGN}С. '
            f'Скорость ветра составляет {wind_speed} м/c.')
    await message.answer(text, reply_markup=get_cancel_cmd())


def register_send_weather(dp: Dispatcher):
    dp.register_message_handler(send_weather, state=WeatherStatesGroup.send_weather)
