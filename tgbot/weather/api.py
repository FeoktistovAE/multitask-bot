from tgbot.config import load_config


config = load_config(".env")
weather_token = config.misc.weather_token


def get_request_link(city_from_user: str) -> str:
    return (f"https://api.openweathermap.org/data/2.5/weather"
            f"?q={city_from_user}&lang=ru&appid={weather_token}&units=metric")