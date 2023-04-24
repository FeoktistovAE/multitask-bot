from aiogram.dispatcher import FSMContext
from aiogram import types, Dispatcher

from tgbot.services.keyboards import get_actions_keyboard


async def greet_user(message: types.Message):
    await message.reply(
        f"Привет, {message.from_user['first_name']} "
        f"Выбери одно из действий на клавиатуре",
        reply_markup=get_actions_keyboard()
    )


def register_greet_user(dp: Dispatcher):
    dp.register_message_handler(greet_user, commands=["start"], state="*")


async def cancel_cmd(message: types.Message, state: FSMContext) -> None:
    await message.reply(
        "Действие отменено",
        reply_markup=get_actions_keyboard(),
    )
    await state.finish()


def register_cancel_cmd(dp: Dispatcher):
    dp.register_message_handler(cancel_cmd, commands=["cancel"], state=["*"])