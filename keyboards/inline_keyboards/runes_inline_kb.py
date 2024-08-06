from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from enum import Enum

from keyboards.inline_keyboards.north_mythology_inline_kb import StepOnTheGuideCD
from main_classes.constant import Constant
from main_classes.guide_to_norse_mythology import GuideToNorseMythologyEnum
from main_classes.rune import Rune


class ActionCurrentRuneBtnText(Enum):
    full_description = "Полное описание"
    short_description = "Краткое описание"
    return_to_all_atts = "Все атты"
    hide_full_desc = "Скрыть"
    return_to_runes = "Назад"


class CurrentRuneActionCbDate(CallbackData, prefix="current_rune"):
    current_rune: ActionCurrentRuneBtnText


class AllAttsCbDate(CallbackData, prefix="all_atts"):
    all_atts: ActionCurrentRuneBtnText


class RuneCbData(CallbackData, prefix="selected_rune"):
    selected_rune: str


class OneOfAllRunesAttsCbData(CallbackData, prefix="selected_att_runes"):
    selected_runes_att: int


def get_all_runes_atts_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    all_runes_att = Rune.get_only_all_att_from_db()
    if len(all_runes_att) != 0:
        for key, value in all_runes_att.items():
            builder.button(
                text=value,
                callback_data=OneOfAllRunesAttsCbData(selected_runes_att=key).pack()
            )
        builder.button(
            text=GuideToNorseMythologyEnum.return_to_main_menu.value,
            callback_data=StepOnTheGuideCD(selected_section=GuideToNorseMythologyEnum.return_to_main_menu)
        )
    else:
        builder.button(
            text=Constant.IF_NUMBER_OF_ATTS_IS_ZERO,
            callback_data=StepOnTheGuideCD(selected_section=GuideToNorseMythologyEnum.return_to_main_menu)
        )
    builder.adjust(3)
    return builder.as_markup()


def get_back_to_all_atts_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.button(
        text=ActionCurrentRuneBtnText.return_to_all_atts.value,
        callback_data=CurrentRuneActionCbDate(current_rune=ActionCurrentRuneBtnText.return_to_all_atts)
    )
    return builder.as_markup()


def get_selected_rune_att(att: int) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    all_names_of_runes = Rune.get_names_of_all_runes_of_current_att(att)
    for name in all_names_of_runes:
        builder.button(
            text=name,
            callback_data=RuneCbData(selected_rune=name)
        )
    builder.button(
        text=ActionCurrentRuneBtnText.return_to_all_atts.value,
        callback_data=AllAttsCbDate(all_atts=ActionCurrentRuneBtnText.return_to_all_atts)
    )
    builder.adjust(4)
    return builder.as_markup()


def get_rune_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text=ActionCurrentRuneBtnText.full_description.value,
        callback_data=CurrentRuneActionCbDate(current_rune=ActionCurrentRuneBtnText.full_description)
    )
    builder.button(
        text=ActionCurrentRuneBtnText.return_to_runes.value,
        callback_data=CurrentRuneActionCbDate(current_rune=ActionCurrentRuneBtnText.return_to_runes)
    )
    builder.adjust(2)
    return builder.as_markup()


def get_hide_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.button(
        text=ActionCurrentRuneBtnText.hide_full_desc.value,
        callback_data=CurrentRuneActionCbDate(current_rune=ActionCurrentRuneBtnText.hide_full_desc).pack(),
    )
    builder.adjust(1)
    return builder.as_markup()


def get_current_rune_from_first_att_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text=ActionCurrentRuneBtnText.full_description.value,
        callback_data=CurrentRuneActionCbDate(current_rune=ActionCurrentRuneBtnText.full_description)
    )
    builder.button(
        text=ActionCurrentRuneBtnText.return_to_runes.value,
        callback_data=CurrentRuneActionCbDate(current_rune=ActionCurrentRuneBtnText.return_to_runes)
    )
    builder.adjust(2)
    return builder.as_markup()


def get_return_back_to_short_desc_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.button(
        text=ActionCurrentRuneBtnText.short_description.value,
        callback_data=CurrentRuneActionCbDate(current_rune=ActionCurrentRuneBtnText.short_description).pack(),
    )

    builder.adjust(1)
    return builder.as_markup()



