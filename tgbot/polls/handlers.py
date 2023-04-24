from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram import Bot

from tgbot.polls.states import PollStatesGroup
from tgbot.config import load_config
from tgbot.services.keyboards import get_cancel_cmd, get_actions_keyboard


config = load_config(".env")

bot = Bot(
    token = config.tg_bot.token,
    parse_mode='HTML',
)


async def start_poll(message: types.Message) -> None:
    await PollStatesGroup.get_chat_id.set()
    await message.answer(
        "Введите id чата, в который отправится опрос",
        reply_markup=get_cancel_cmd()
    )


def register_start_poll(dp: Dispatcher) -> None:
    dp.register_message_handler(start_poll, Text(equals="Создать опрос"))


async def get_chat_id(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data["chat_id"] = message.text
    await PollStatesGroup.next()
    await message.reply(
        "Введите ваш вопрос",
        reply_markup=get_cancel_cmd()
    )


def register_get_chat_id(dp: Dispatcher):
    dp.register_message_handler(get_chat_id, state=PollStatesGroup.get_chat_id)


async def get_question(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data["question"] = message.text
    await PollStatesGroup.next()
    await message.reply(
        'Введите варианты ответа через запятую.\n Пример: "Да, Нет, Возможно"',
        reply_markup=get_cancel_cmd()
    )


def register_get_question(dp: Dispatcher) -> None:
    dp.register_message_handler(get_question, state=PollStatesGroup.get_question)


async def send_poll(message: types.Message, state: FSMContext) -> None:
    options = [option.strip() for option in message.text.split(',') if option.strip() > 0]
    async with state.proxy() as data:
        chat_id = data["chat_id"]
        question = data["question"]
    
    try:
        await bot.send_poll(
            chat_id=chat_id,
            question=question,
            options=options,
        )
    except:
        message.answer(
            "Что-то пошло не по плану",
            reply_markup=get_actions_keyboard(),
        )
        return
    
    await state.finish()
    await message.answer(
        "Опрос отправлен",
        reply_markup=get_actions_keyboard(),
    )


def register_send_poll(dp: Dispatcher) -> None:
    dp.register_message_handler(send_poll, state = PollStatesGroup.send_poll)