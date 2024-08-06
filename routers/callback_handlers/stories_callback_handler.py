from aiogram import Router, F
from aiogram.utils import markdown
from aiogram.types import CallbackQuery, InputMediaPhoto
from keyboards.inline_keyboards.stories_kb import (get_all_stories_kd, get_hide_kb, SelectedStoryCD,
                                                   ActionCurrentStoryBtnText)
from main_classes.stories import Story

router = Router(name=__name__)


@router.callback_query(SelectedStoryCD.filter(F.selected_story == str(ActionCurrentStoryBtnText.hide_full_desc.value)))
async def hide_story_full_desc(call: CallbackQuery):
    await call.answer()
    await call.message.delete()


@router.callback_query(SelectedStoryCD.filter(F.selected_story))
async def return_story(call: CallbackQuery, callback_data: SelectedStoryCD):

    story_from_db = Story.select_story_from_db(callback_data.selected_story)

    img = InputMediaPhoto(media=story_from_db.tg_img_id)
    text = markdown.text(f"{markdown.hbold(story_from_db.name)}\n{story_from_db.full_description}")
    await call.message.edit_media(img)
    await call.message.edit_reply_markup(
        reply_markup=get_all_stories_kd()
    )
    await call.message.answer(
        text=text,
        reply_markup=get_hide_kb()
    )



