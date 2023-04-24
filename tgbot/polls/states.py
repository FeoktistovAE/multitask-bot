from aiogram.dispatcher.filters.state import StatesGroup, State


class PollStatesGroup(StatesGroup):
    get_chat_id = State()
    get_question = State()
    get_options = State()
    send_poll = State()