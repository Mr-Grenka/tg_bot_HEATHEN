from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from main_classes.guide_to_norse_mythology import GuideToNorseMythologyEnum, GuideToNorseMythology


class StepOnTheGuideCD(CallbackData, prefix="selected_section"):
    selected_section: GuideToNorseMythologyEnum


def get_all_sections_of_north_mythology_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    sections_list = GuideToNorseMythology.select_all_section_from_db()
    if sections_list != 0:
        for section in sections_list:
            builder.button(
                text=section,
                callback_data=StepOnTheGuideCD(selected_section=section).pack()
            )

    builder.adjust(3)
    return builder.as_markup()


