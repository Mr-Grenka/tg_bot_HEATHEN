from aiogram import Router
from aiogram.enums import ChatAction
from aiogram.types import InputMediaPhoto, CallbackQuery
from aiogram.filters.callback_data import CallbackData
from aiogram.utils import markdown

from keyboards.inline_keyboards.symbolism_inline_kb import SymbolismCbData, get_symbolism_kb
from main_classes.basic_model import BasicModel
from main_classes.symbolism import Symbolism
router = Router(name=__name__)


@router.callback_query(SymbolismCbData.filter())
async def show_the_world(call: CallbackQuery, callback_data: SymbolismCbData):
    data = callback_data.symbol

    symbol = Symbolism.select_symbol_from_db(data)
    img = InputMediaPhoto(media=symbol.tg_img_id)

    await call.message.edit_media(img)
    text = f"{markdown.hbold(symbol.name)}\n{symbol.full_description}"
    await call.message.edit_caption(
        caption=BasicModel.check_the_allowed_caption_length(text),
        reply_markup=get_symbolism_kb(data)
    )
