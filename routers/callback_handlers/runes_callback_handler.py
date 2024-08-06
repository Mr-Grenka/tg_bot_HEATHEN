from aiogram import Router, F
from aiogram.types import InputMediaPhoto, CallbackQuery
from aiogram.filters.callback_data import CallbackData
from aiogram.fsm.context import FSMContext

from main_classes.basic_model import BasicModel
from main_classes.rune import Rune
from main_classes.states import RunicState
from keyboards.inline_keyboards.runes_inline_kb import (OneOfAllRunesAttsCbData, CurrentRuneActionCbDate,
                                                        ActionCurrentRuneBtnText, get_selected_rune_att,
                                                        get_all_runes_atts_kb, get_hide_kb, RuneCbData,
                                                        AllAttsCbDate, get_rune_kb)

router = Router(name=__name__)


@router.callback_query(AllAttsCbDate.filter(F.all_atts))
async def return_all_atts(call: CallbackQuery):

    rune_menu = Rune.select_rune_from_db("Меню")

    await call.message.edit_caption(
        caption=BasicModel.check_the_allowed_caption_length(rune_menu.short_description),
        reply_markup=get_all_runes_atts_kb()
    )


@router.callback_query(OneOfAllRunesAttsCbData.filter(F.selected_runes_att))
async def return_runes_of_the_first_att111(call: CallbackQuery, callback_data: OneOfAllRunesAttsCbData, state: FSMContext):

    att = callback_data.selected_runes_att
    all_runes_att = Rune.get_only_all_att_from_db()

    await state.set_state(RunicState.selected_att)
    await state.update_data(selected_att=att)

    await call.message.edit_caption(
        caption=BasicModel.check_the_allowed_caption_length(all_runes_att[att]),
        reply_markup=get_selected_rune_att(att)
    )


@router.callback_query(CurrentRuneActionCbDate.filter(F.current_rune == ActionCurrentRuneBtnText.return_to_all_atts))
async def return_all_atts(call: CallbackQuery):

    rune_menu = Rune.select_rune_from_db("Меню")

    await call.message.edit_caption(
        caption=BasicModel.check_the_allowed_caption_length(rune_menu.short_description),
        reply_markup=get_all_runes_atts_kb()
    )


@router.callback_query(RuneCbData.filter(F.selected_rune))
async def return_rune_all_info(call: CallbackQuery, callback_data: RuneCbData, state: FSMContext):

    rune = Rune.select_rune_from_db(callback_data.selected_rune)
    img = InputMediaPhoto(media=rune.tg_img_id)

    await state.set_state(RunicState.selected_rune)
    await state.update_data(selected_rune=rune.name)

    await call.message.edit_media(media=img)
    await call.message.edit_caption(
        caption=BasicModel.check_the_allowed_caption_length(rune.short_description),
        reply_markup=get_rune_kb()
    )


@router.callback_query(CurrentRuneActionCbDate.filter(F.current_rune == ActionCurrentRuneBtnText.full_description))
async def return_rune_short_desc(call: CallbackQuery, state: FSMContext):

    data = await state.update_data()

    rune = Rune.select_rune_from_db(data["selected_rune"])

    await call.message.answer(
        text=rune.full_description,
        reply_markup=get_hide_kb()
    )


@router.callback_query(CurrentRuneActionCbDate.filter(F.current_rune == ActionCurrentRuneBtnText.return_to_runes))
async def return_rune_short_desc(call: CallbackQuery, state: FSMContext):

    data = await state.update_data()

    all_runes_att = Rune.get_only_all_att_from_db()
    menu_rune = Rune.select_rune_from_db("Меню")
    img = InputMediaPhoto(media=menu_rune.tg_img_id)

    await call.message.edit_media(media=img)
    await call.message.edit_caption(
        caption=BasicModel.check_the_allowed_caption_length(all_runes_att[data["selected_att"]]),
        reply_markup=get_selected_rune_att(data["selected_att"])
    )


@router.callback_query(CurrentRuneActionCbDate.filter(F.current_rune == ActionCurrentRuneBtnText.hide_full_desc))
async def hide_rune_full_desc(call: CallbackQuery):

    await call.answer()
    await call.message.delete()


























