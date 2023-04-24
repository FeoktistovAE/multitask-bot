from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

from tgbot.cute_animals.api import get_animal_url


async def start_animal_picture(message: types.Message) -> None:
    animal_photo_url = get_animal_url()
    await message.answer_photo(animal_photo_url)


def register_start_animal_picture(dp: Dispatcher):
    dp.register_message_handler(start_animal_picture, Text(equals="Получить милую фотографию животного"), state=None),