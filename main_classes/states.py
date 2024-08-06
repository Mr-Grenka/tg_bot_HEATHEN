from aiogram.fsm.state import StatesGroup, State


class NorthMythSectionState(StatesGroup):
    selected_section = State()


class RunicState(StatesGroup):
    selected_att = State()
    selected_rune = State()


class GodsState(StatesGroup):
    all_gods = State()
    selected_type_gods = State()
    selected_god = State()
