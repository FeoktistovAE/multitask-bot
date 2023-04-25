import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from tgbot.user.handlers import register_greet_user, register_cancel_cmd
from tgbot.weather.handlers import register_start_weather, register_send_weather
from tgbot.exchange_rates.handlers import register_start_exchange_rates, \
    register_get_convert_to_value, register_get_convert_from_value, register_get_count
from tgbot.cute_animals.handlers import register_start_animal_picture
from tgbot.polls.handlers import register_start_poll, register_get_chat_id, \
    register_get_question, register_send_poll
from tgbot.config import load_config
from tgbot.services.setting_commands import set_default_commands


logger = logging.getLogger(__name__)


def register_all_handlers(dp):
    register_greet_user(dp)
    register_cancel_cmd(dp)
    register_start_weather(dp)
    register_send_weather(dp)
    register_start_exchange_rates(dp)
    register_get_convert_from_value(dp)
    register_get_convert_to_value(dp)
    register_get_count(dp)
    register_start_animal_picture(dp)
    register_start_poll(dp)
    register_get_chat_id(dp)
    register_get_question(dp)
    register_send_poll(dp)


async def set_all_default_commands(bot: Bot):
    await set_default_commands(bot)


config = load_config(".env")

bot = Bot(
    token=config.tg_bot.token,
    parse_mode='HTML',
)

storage = MemoryStorage()


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info("Starting bot")

    dp = Dispatcher(bot, storage=storage)

    register_all_handlers(dp)

    await set_default_commands(bot)

    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
