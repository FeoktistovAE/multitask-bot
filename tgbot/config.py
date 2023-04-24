from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str
    admin_ids: list
    use_redis: bool


@dataclass
class Miscellaneous:
    weather_token: str
    exchange_rates_token: str
    animal_pictures_token: str


@dataclass
class Config:
    tg_bot: TgBot
    misc: Miscellaneous


def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            token=env.str("BOT_TOKEN"),
            admin_ids=list(map(int, env.list("ADMINS"))),
            use_redis=env.bool("USE_REDIS"),
        ),
        misc=Miscellaneous(
            weather_token=env.str("WEATHER_TOKEN"),
            exchange_rates_token=env.str("EXCHANGE_RATES_TOKEN"),
            animal_pictures_token=env.str("ANIMAL_PICTURES_TOKEN"),
        )
    )
