from aiogram import Router, types, F
from aiogram.filters import CommandStart, Command
from aiogram.types import FSInputFile, InputMediaPhoto
from aiogram.utils import markdown
from aiogram.enums import ChatAction

from main_classes.basic_model import BasicModel
from main_classes.basic_phrase import BasicPhrases, BasicPhrasesEnum
from keyboards.inline_keyboards.north_mythology_inline_kb import get_all_sections_of_north_mythology_kb, \
    get_all_sections_of_north_mythology_kb

router = Router(name=__name__)


@router.message(CommandStart())
async def start(message: types.Message):
    greeting_phrase = BasicPhrases.select_phrase_from_db(BasicPhrasesEnum.starting_greeting)
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.TYPING
    )
    await message.answer_photo(
        photo=greeting_phrase.tg_img_id,
        caption=BasicModel.check_the_allowed_caption_length(
            markdown.text(f"{markdown.hbold(message.from_user.full_name)}, ",
                          markdown.text(greeting_phrase.phrase))),
        reply_markup=get_all_sections_of_north_mythology_kb()
    )


@router.message(Command("help"))
async def get_help(message: types.Message):
    help_phrase = BasicPhrases.select_phrase_from_db(BasicPhrasesEnum.help)
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.TYPING
    )
    await message.answer_photo(
        photo=help_phrase.tg_img_id,
        caption=BasicModel.check_the_allowed_caption_length(
            markdown.text(f"{markdown.hbold(message.from_user.full_name)}, ",
                          markdown.text(help_phrase.phrase))),
        reply_markup=get_all_sections_of_north_mythology_kb()
    )


@router.message(Command("info"))
async def get_info(message: types.Message):
    info_phrase = BasicPhrases.select_phrase_from_db(BasicPhrasesEnum.info)
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.TYPING
    )
    await message.answer_photo(
        photo=info_phrase.tg_img_id,
        caption=BasicModel.check_the_allowed_caption_length(
            markdown.text(f"{markdown.hbold(message.from_user.full_name)}, ",
                          markdown.text(info_phrase.phrase))),
        reply_markup=get_all_sections_of_north_mythology_kb()
    )


# просто, чтоб ловить tg id фотографии
# just to catch tg img id
@router.message(F.photo)
async def catch_photo(message: types.Message):
    print(message.photo[-1].file_id)


@router.message(F.text)
async def handle_random_message(message: types.Message):
    await message.answer("Нахуй ты пишешь, нажимай на кнопки")