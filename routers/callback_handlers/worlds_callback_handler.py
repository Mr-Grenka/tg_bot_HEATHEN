from aiogram import Router, F
from aiogram.utils import markdown
from aiogram.types import CallbackQuery, InputMediaPhoto

from keyboards.inline_keyboards.worlds_inline_kb import WorldsSlideCbData, get_worlds_slide_kb
from main_classes.basic_model import BasicModel
from main_classes.constant import Constant
from main_classes.worlds import World
router = Router(name=__name__)


@router.callback_query(WorldsSlideCbData.filter())
async def show_the_world(call: CallbackQuery, callback_data: WorldsSlideCbData):
    page = callback_data.page
    dictionary_of_worlds = World.get_dictionary_of_worlds_names()

    world = World.select_world_from_db(dictionary_of_worlds[page])
    img = InputMediaPhoto(media=world.tg_img_id)

    await call.message.edit_media(img)

    text = f"{markdown.hbold(world.name)}\n{world.full_description}"
    if len(text) <= Constant.MAX_SIZE_OF_CAPTION_TEXT_IN_TELEGRAM:
        await call.message.edit_caption(
            caption=BasicModel.check_the_allowed_caption_length(text),
            reply_markup=get_worlds_slide_kb(page)
        )
    else:
        text = "Превышен максимальный объём текста"
        await call.message.edit_caption(
            caption=BasicModel.check_the_allowed_caption_length(text),
            reply_markup=get_worlds_slide_kb(page)
        )


