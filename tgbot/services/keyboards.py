from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_actions_keyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton("Узнать погоду"))
    kb.add(KeyboardButton("Узнать курс"))
    kb.add(KeyboardButton("Получить милую фотографию животного"))
    kb.add(KeyboardButton("Создать опрос"))
    return kb


def get_cancel_cmd() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton("/cancel"))
    return kb


def get_currency_keyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    rub_button = KeyboardButton("RUB")
    usd_button = KeyboardButton("USD")
    try_button = KeyboardButton("TRY")
    kzt_button = KeyboardButton("KZT")
    gbp_button = KeyboardButton("GBP")
    eur_button = KeyboardButton("EUR")
    amd_button = KeyboardButton("AMD")
    byr_button = KeyboardButton("BYR")
    cny_button = KeyboardButton("CNY")
    cancel_button = KeyboardButton("/cancel")
    kb.row(
        rub_button,
        usd_button,
        try_button,
    )
    kb.row(
        kzt_button,
        gbp_button,
        eur_button
    )
    kb.row(
        byr_button,
        amd_button,
        cny_button
    )
    kb.add(cancel_button)
    return kb