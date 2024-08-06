from enum import Enum

from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from keyboards.inline_keyboards.north_mythology_inline_kb import StepOnTheGuideCD
from main_classes.constant import Constant
from main_classes.guide_to_norse_mythology import GuideToNorseMythologyEnum
from main_classes.stories import Story


class ActionCurrentStoryBtnText(Enum):
    hide_full_desc = "Скрыть"


class SelectedStoryCD(CallbackData, prefix="selected_story"):
    selected_story: str


def get_all_stories_kd() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    story_list = Story.select_all_story_names_from_db()
    if story_list != 0:
        for story in story_list:
            builder.button(
                text=story,
                callback_data=SelectedStoryCD(selected_story=story).pack()
            )
        builder.button(
            text=GuideToNorseMythologyEnum.return_to_main_menu.value,
            callback_data=StepOnTheGuideCD(selected_section=GuideToNorseMythologyEnum.return_to_main_menu)
        )
    builder.adjust(1)
    return builder.as_markup()


def get_hide_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text=ActionCurrentStoryBtnText.hide_full_desc.value,
        callback_data=SelectedStoryCD(selected_story=ActionCurrentStoryBtnText.hide_full_desc).pack(),
    )
    return builder.as_markup()

