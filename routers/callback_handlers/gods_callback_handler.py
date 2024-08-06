from aiogram import Router, F
from aiogram.types import InputMediaPhoto, CallbackQuery
from aiogram.filters.callback_data import CallbackData
from aiogram.fsm.context import FSMContext
from aiogram.utils import markdown

from main_classes.basic_model import BasicModel
from main_classes.guide_to_norse_mythology import GuideToNorseMythology, GuideToNorseMythologyEnum
from main_classes.states import GodsState
from main_classes.gods import Gods
from keyboards.inline_keyboards.gods_inline_kb import (ActionCurrentGodBtnText, TypeOfGodsCbData, GodsCbData,
                                                       CurrentGodCbDate, AllTypesOfGodsCbDate,
                                                       get_types_of_gods_kb, get_selected_type_of_gods_kd,
                                                       get_back_to_types_of_gods_kb, get_return_back_to_short_desc_kb,
                                                       get_hide_kb, get_book_menu_kb, GodSlideCbData,
                                                       CurrentTypesOfGodsCbDate)


router = Router(name=__name__)


@router.callback_query(TypeOfGodsCbData.filter(F.selected_type_god))
async def return_gods_from_selected_type_god(call: CallbackQuery, callback_data: TypeOfGodsCbData, state: FSMContext):
    await state.set_state(GodsState.selected_type_gods)
    await state.update_data(selected_type_gods=callback_data.selected_type_god)
    await call.message.edit_caption(
        caption=callback_data.selected_type_god,
        reply_markup=get_selected_type_of_gods_kd(callback_data.selected_type_god)
    )


@router.callback_query(CurrentTypesOfGodsCbDate.filter(F.current_types_of_gods))
async def return_to_selected_type_of_gods(call: CallbackQuery, state: FSMContext):
    data = await state.update_data()
    gods = GuideToNorseMythology.select_menu_section_from_db(GuideToNorseMythologyEnum.gods.value)
    img = InputMediaPhoto(media=gods.tg_img_id)

    await call.message.edit_media(img)
    await call.message.edit_caption(
        caption=BasicModel.check_the_allowed_caption_length(data["selected_type_gods"]),
        reply_markup=get_selected_type_of_gods_kd(data["selected_type_gods"])
    )


@router.callback_query(AllTypesOfGodsCbDate.filter(
    F.all_types_of_gods == ActionCurrentGodBtnText.return_to_type_of_gods))
async def return_all_type_of_gods(call: CallbackQuery, callback_data: AllTypesOfGodsCbDate, state: FSMContext):
    await state.set_state(GodsState.all_gods)
    await state.update_data(all_gods=callback_data.all_types_of_gods)

    gods = GuideToNorseMythology.select_menu_section_from_db(GuideToNorseMythologyEnum.gods.value)

    img = InputMediaPhoto(media=gods.tg_img_id)

    await call.message.edit_media(img)
    await call.message.edit_caption(
        caption=BasicModel.check_the_allowed_caption_length(gods.description),
        reply_markup=get_types_of_gods_kb()
    )


@router.callback_query(GodsCbData.filter(F.selected_gods))
async def return_god(call: CallbackQuery, callback_data: GodsCbData, state: FSMContext):
    god = Gods.get_god_from_db(callback_data.selected_gods)

    await state.set_state(GodsState.selected_god)
    await state.update_data(selected_god=callback_data.selected_gods)
    img = InputMediaPhoto(media=god.tg_img_id)

    await call.message.edit_media(media=img)
    await call.message.edit_caption(
        caption=BasicModel.check_the_allowed_caption_length(f"{markdown.hbold(god.name)}\n{god.short_description}"),
        reply_markup=get_book_menu_kb()
    )


@router.callback_query(GodSlideCbData.filter(F.slide))
async def return_info_of_god(call: CallbackQuery, callback_data: GodSlideCbData, state: FSMContext):
    slide = callback_data.slide
    data = await state.update_data()
    god = Gods.get_god_from_db(data["selected_god"])
    main_info_of_god = Gods.get_main_info_of_god_for_creating_book_menu(data["selected_god"])
    text = f"{markdown.hbold(god.name)}\n{main_info_of_god[slide]}"

    if slide == 0:

        await call.message.edit_caption(
            caption=BasicModel.check_the_allowed_caption_length(f"{markdown.hbold(god.name)}\n{god.short_description}"),
            reply_markup=get_book_menu_kb(slide)
        )
    else:
        await call.message.edit_caption(
            caption=BasicModel.check_the_allowed_caption_length(text),
            reply_markup=get_book_menu_kb(slide)
        )

