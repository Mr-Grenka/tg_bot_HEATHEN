from enum import Enum
from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from keyboards.inline_keyboards.north_mythology_inline_kb import StepOnTheGuideCD
from main_classes.guide_to_norse_mythology import GuideToNorseMythologyEnum
from main_classes.symbolism import Symbolism


class ActionBtnText(Enum):
    back = "⬅️"
    forward = "➡️"


class SymbolismCbData(CallbackData, prefix="symbol"):
    symbol: str


def get_symbolism_kb(deleted: str = "") -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    symbolism_dict = Symbolism.get_dictionary_of_symbols_names()

    for key, value in symbolism_dict.items():
        if value == deleted:
            continue
        else:
            builder.button(
                text=value,
                callback_data=SymbolismCbData(symbol=value)
            )
    builder.button(
        text=GuideToNorseMythologyEnum.return_to_main_menu.value,
        callback_data=StepOnTheGuideCD(selected_section=GuideToNorseMythologyEnum.return_to_main_menu)
    )
    builder.adjust(2)
    return builder.as_markup()

