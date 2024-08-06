from enum import Enum

from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from keyboards.inline_keyboards.north_mythology_inline_kb import StepOnTheGuideCD
from main_classes.constant import Constant
from main_classes.gods import Gods
from main_classes.guide_to_norse_mythology import GuideToNorseMythologyEnum


class ActionBookMenuBtnText(Enum):
    back = "⬅️"
    forward = "➡️"


class ActionCurrentGodBtnText(Enum):
    short_description = "Краткое описание"
    full_description = "Полное описание"
    capabilities = "Способности"
    return_to_selected_type_of_gods = "Назад к божествам"
    return_to_type_of_gods = "Назад к разделам"
    hide_full_desc = "Скрыть"
    return_to_gods = "Назад"


class TypeOfGodsCbData(CallbackData, prefix="selected_type_god"):
    selected_type_god: str


class GodsCbData(CallbackData, prefix="selected_gods"):
    selected_gods: str


class AllTypesOfGodsCbDate(CallbackData, prefix="all_types_of_gods"):
    all_types_of_gods: ActionCurrentGodBtnText


class CurrentTypesOfGodsCbDate(CallbackData, prefix="current_types_of_gods"):
    current_types_of_gods: ActionCurrentGodBtnText


class CurrentGodCbDate(CallbackData, prefix="selected_god"):
    selected_god: ActionCurrentGodBtnText


class GodSlideCbData(CallbackData, prefix="slide"):
    slide: int


def get_types_of_gods_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    types_of_gods = Gods.get_only_types_of_gods_db()
    if len(types_of_gods) != 0:
        for type_ in types_of_gods:
            builder.button(
                text=type_,
                callback_data=TypeOfGodsCbData(selected_type_god=type_).pack()
            )
        builder.button(
            text=GuideToNorseMythologyEnum.return_to_main_menu.value,
            callback_data=StepOnTheGuideCD(selected_section=GuideToNorseMythologyEnum.return_to_main_menu)
        )
    else:
        builder.button(
            text=Constant.IF_TYPES_OF_GODS_IS_EMPTY,
            callback_data=StepOnTheGuideCD(selected_section=GuideToNorseMythologyEnum.return_to_main_menu)
        )
    builder.adjust(2)
    return builder.as_markup()


def return_to_selected_type_of_gods_kd() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.button(
        text=ActionCurrentGodBtnText.return_to_selected_type_of_gods.value,
        callback_data=CurrentTypesOfGodsCbDate(
            current_types_of_gods=ActionCurrentGodBtnText.return_to_selected_type_of_gods)
    )

    builder.adjust(3)
    return builder.as_markup()


def get_selected_type_of_gods_kd(type_of_god) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    names_of_gods = Gods.get_gods_from_db(type_of_god)
    if names_of_gods != 0:
        for name in names_of_gods:
            builder.button(
                text=name,
                callback_data=GodsCbData(selected_gods=name)
            )
        builder.button(
            text=ActionCurrentGodBtnText.return_to_type_of_gods.value,
            callback_data=AllTypesOfGodsCbDate(all_types_of_gods=ActionCurrentGodBtnText.return_to_type_of_gods)
        )

    builder.adjust(3)
    return builder.as_markup()


def get_book_menu_kb(slide: int = 1) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    # 3 - this is short, full desc + capabilities
    has_next_page = 3 > slide

    if slide != 1:
        builder.button(
            text=ActionBookMenuBtnText.back.value,
            callback_data=GodSlideCbData(slide=slide-1)
        )

    if has_next_page:
        builder.button(
            text=ActionBookMenuBtnText.forward.value,
            callback_data=GodSlideCbData(slide=slide + 1)
        )
    builder.button(
        text=ActionCurrentGodBtnText.return_to_selected_type_of_gods.value,
        callback_data=CurrentTypesOfGodsCbDate(
            current_types_of_gods=ActionCurrentGodBtnText.return_to_selected_type_of_gods)
    )
    builder.adjust(2)
    return builder.as_markup()


def get_back_to_types_of_gods_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.button(
        text=ActionCurrentGodBtnText.return_to_type_of_gods.value,
        callback_data=CurrentGodCbDate(selected_god=ActionCurrentGodBtnText.return_to_type_of_gods)
    )
    return builder.as_markup()


def get_return_back_to_short_desc_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.button(
        text=ActionCurrentGodBtnText.short_description.value,
        callback_data=CurrentGodCbDate(current_rune=ActionCurrentGodBtnText.short_description).pack(),
    )

    builder.adjust(1)
    return builder.as_markup()


def get_hide_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.button(
        text=ActionCurrentGodBtnText.hide_full_desc.value,
        callback_data=CurrentGodCbDate(current_rune=ActionCurrentGodBtnText.hide_full_desc).pack(),
    )
    builder.adjust(1)
    return builder.as_markup()


