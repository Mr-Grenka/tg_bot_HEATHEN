from aiogram import Router, F
from aiogram.types import CallbackQuery, InputMediaPhoto
from aiogram.utils import markdown

from keyboards.inline_keyboards.gods_inline_kb import get_types_of_gods_kb
from keyboards.inline_keyboards.runes_inline_kb import get_all_runes_atts_kb
from keyboards.inline_keyboards.north_mythology_inline_kb import (StepOnTheGuideCD,
                                                                  get_all_sections_of_north_mythology_kb)
from keyboards.inline_keyboards.stories_kb import get_all_stories_kd
from keyboards.inline_keyboards.symbolism_inline_kb import get_symbolism_kb

from keyboards.inline_keyboards.worlds_inline_kb import get_worlds_slide_kb
from main_classes.basic_model import BasicModel
from main_classes.basic_phrase import BasicPhrases, BasicPhrasesEnum
from main_classes.guide_to_norse_mythology import GuideToNorseMythologyEnum, GuideToNorseMythology
from main_classes.worlds import World
router = Router(name=__name__)


@router.callback_query(StepOnTheGuideCD.filter(F.selected_section == GuideToNorseMythologyEnum.gods))
async def return_gods_info(call: CallbackQuery):
    gods = GuideToNorseMythology.select_menu_section_from_db(GuideToNorseMythologyEnum.gods.value)

    img = InputMediaPhoto(media=gods.tg_img_id)

    await call.message.edit_media(img)
    await call.message.edit_caption(
        caption=BasicModel.check_the_allowed_caption_length(gods.description),
        reply_markup=get_types_of_gods_kb()
    )


@router.callback_query(StepOnTheGuideCD.filter(F.selected_section == GuideToNorseMythologyEnum.runes))
async def return_runes_info(call: CallbackQuery):

    runes = GuideToNorseMythology.select_menu_section_from_db(GuideToNorseMythologyEnum.runes.value)
    img = InputMediaPhoto(media=runes.tg_img_id)

    await call.message.edit_media(img)
    await call.message.edit_caption(
        caption=BasicModel.check_the_allowed_caption_length(runes.description),
        reply_markup=get_all_runes_atts_kb()
    )


@router.callback_query(StepOnTheGuideCD.filter(F.selected_section == GuideToNorseMythologyEnum.stories))
async def return_worlds_kb(call: CallbackQuery):
    stories = GuideToNorseMythology.select_menu_section_from_db(GuideToNorseMythologyEnum.stories.value)

    img = InputMediaPhoto(media=stories.tg_img_id)

    await call.message.edit_media(img)
    await call.message.edit_caption(
        caption=BasicModel.check_the_allowed_caption_length(stories.description),
        reply_markup=get_all_stories_kd()
    )


@router.callback_query(StepOnTheGuideCD.filter(F.selected_section == GuideToNorseMythologyEnum.worlds))
async def return_worlds_kb(call: CallbackQuery):

    world_dictionary = World.get_dictionary_of_worlds_names()
    world = World.select_world_from_db(world_dictionary[0])

    img = InputMediaPhoto(media=world.tg_img_id)

    await call.message.edit_media(img)
    await call.message.edit_caption(
        caption=BasicModel.check_the_allowed_caption_length(
            markdown.text(f"{markdown.hbold(world.name)}\n{world.full_description}")),
        reply_markup=get_worlds_slide_kb()
    )


@router.callback_query(StepOnTheGuideCD.filter(F.selected_section == GuideToNorseMythologyEnum.symbolism))
async def return_worlds_kb(call: CallbackQuery):
    symbolism = GuideToNorseMythology.select_menu_section_from_db(GuideToNorseMythologyEnum.symbolism.value)

    img = InputMediaPhoto(media=symbolism.tg_img_id)

    await call.message.edit_media(img)
    await call.message.edit_caption(
        caption=BasicModel.check_the_allowed_caption_length(symbolism.description),
        reply_markup=get_symbolism_kb()
    )


@router.callback_query(StepOnTheGuideCD.filter(F.selected_section == GuideToNorseMythologyEnum.return_to_main_menu))
async def return_main_menu(call: CallbackQuery):
    greeting_phrase = BasicPhrases.select_phrase_from_db(BasicPhrasesEnum.starting_greeting)

    img = InputMediaPhoto(media=greeting_phrase.tg_img_id)

    await call.message.edit_media(media=img)
    await call.message.edit_caption(
        caption=BasicModel.check_the_allowed_caption_length(markdown.text(greeting_phrase.phrase)),
        reply_markup=get_all_sections_of_north_mythology_kb()
    )


