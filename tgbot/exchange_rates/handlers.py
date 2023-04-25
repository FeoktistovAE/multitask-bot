import json
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext

from tgbot.exchange_rates.states import CurrencyStatesGroup
from tgbot.services.keyboards import get_cancel_cmd, get_currency_keyboard, get_actions_keyboard
from tgbot.exchange_rates.api import get_convertation_data


async def start_exchange_rates(message: types.Message) -> None:
    await CurrencyStatesGroup.convert_from_state.set()
    await message.answer(
        'Выберите валюту, которую вы хотите конвертировать',
        reply_markup=get_currency_keyboard()
    )


def register_start_exchange_rates(dp: Dispatcher):
    dp.register_message_handler(start_exchange_rates, Text(equals="Узнать курс валют"), state=None),


async def get_convert_from_value(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["from_currency"] = message.text

    await CurrencyStatesGroup.next()
    await message.reply(
        "Выберите валюту, в которую вы хотите конвертировать",
        reply_markup=get_currency_keyboard(),
    )


def register_get_convert_from_value(dp: Dispatcher):
    dp.register_message_handler(
        get_convert_from_value,
        state=CurrencyStatesGroup.convert_from_state,
    )


async def get_convert_to_value(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["to_currency"] = message.text

    await CurrencyStatesGroup.next()
    await message.reply(
        "Теперь введите сумму",
        reply_markup=get_cancel_cmd()
    )


def register_get_convert_to_value(dp: Dispatcher):
    dp.register_message_handler(get_convert_to_value, state=CurrencyStatesGroup.convert_to_state)


async def get_count(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        amount = message.text
        to_currency = data["to_currency"]
        from_currency = data["from_currency"]

    convertation_data = json.loads(
        get_convertation_data(to_currency=to_currency, from_currency=from_currency, amount=amount)
    )
    exchange_rate = convertation_data["info"]["rate"]
    result = convertation_data['result']

    await message.answer(
        f"Сумма конвертации {amount} {from_currency} в {to_currency} "
        f"составит: {result} {to_currency}\n"
        f"Текущий обменный курс валют составляет 1 {from_currency} = {exchange_rate} {to_currency}",
        reply_markup=get_actions_keyboard()
    )
    await state.finish()


def register_get_count(dp: Dispatcher):
    dp.register_message_handler(get_count, state=CurrencyStatesGroup.final_state)
