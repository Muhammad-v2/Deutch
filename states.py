from aiogram.fsm.state import State, StatesGroup


class Game(StatesGroup):
    translate = State()
    matching = State()
    quiz = State()
    scramble = State()
