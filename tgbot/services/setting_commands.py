from aiogram import Bot
from aiogram.types import BotCommand


async def set_default_commands(bot: Bot):
    return await bot.set_my_commands(
        commands=[BotCommand("start", "Запуск приветствия"),]
    )
