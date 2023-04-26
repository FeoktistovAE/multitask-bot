from tgbot.config import load_config
import requests


config = load_config(".env")
weather_token = config.misc.weather_token


def get_weather_data(city_from_user: str) -> str:
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city_from_user}&lang=ru&appid={weather_token}&units=metric"
    )
    weather_data = requests.get(url).json()
    return weather_data

