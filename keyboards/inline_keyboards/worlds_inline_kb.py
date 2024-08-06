from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from enum import Enum

from keyboards.inline_keyboards.north_mythology_inline_kb import StepOnTheGuideCD
from main_classes.guide_to_norse_mythology import GuideToNorseMythologyEnum
from main_classes.worlds import World


class ActionBtnText(Enum):
    back = "⬅️"
    forward = "➡️"


class WorldsSlideCbData(CallbackData, prefix="page"):
    page: int


def get_worlds_slide_kb(page: int = 0) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    dictionary_of_worlds = World.get_dictionary_of_worlds_names()

    # has_next_page = World.All_WORLDS > page + 1
    has_next_page = len(dictionary_of_worlds) > page + 1

    if page != 0:
        builder.button(
            text=ActionBtnText.back.value,
            callback_data=WorldsSlideCbData(page=page-1)
        )

    if has_next_page:
        builder.button(
            text=ActionBtnText.forward.value,
            callback_data=WorldsSlideCbData(page=page + 1)
        )

    builder.button(
        text=GuideToNorseMythologyEnum.return_to_main_menu.value,
        callback_data=StepOnTheGuideCD(selected_section=GuideToNorseMythologyEnum.return_to_main_menu)
    )

    return builder.as_markup()

