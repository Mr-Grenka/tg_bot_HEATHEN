from dataclasses import dataclass

from main_classes.constant import Constant


@dataclass(kw_only=True)
class BasicModel:
    _tg_img_id: str
    _name: str
    _short_description: str
    _full_description: str

    def __init__(self, tg_img_id, name, short_description, full_description):
        self._verify_tg_img_id(tg_img_id)
        self._verify_name(name)
        self._verify_short_description(short_description)
        self._verify_full_description(full_description)

    @classmethod
    def _verify_tg_img_id(cls, tg_img_id):
        if cls.check_for_emptiness_or_only_spaces(tg_img_id):
            cls._tg_img_id = Constant.IF_IMG_IS_EMPTY
        else:
            cls._tg_img_id = tg_img_id

    @classmethod
    def _verify_name(cls, name):
        if cls.check_for_emptiness_or_only_spaces(name):
            raise TypeError("Название не должно быть пробелом и не должно быть Null/None")
        else:
            cls._name = name

    @classmethod
    def _verify_short_description(cls, short_description):
        if cls.check_for_emptiness_or_only_spaces(short_description):
            cls._short_description = Constant.IF_SHORT_DESCRIPTION_IS_EMPTY
        else:
            cls._short_description = short_description

    @classmethod
    def _verify_full_description(cls, full_description):
        if cls.check_for_emptiness_or_only_spaces(full_description):
            cls._full_description = Constant.IF_FULL_DESCRIPTION_IS_EMPTY
        else:
            cls._full_description = full_description

    @property
    def tg_img_id(self):
        return self._tg_img_id

    @tg_img_id.setter
    def tg_img_id(self, tg_img_id):
        self._verify_tg_img_id(tg_img_id)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._verify_name(name)

    @property
    def short_description(self):
        return self._short_description

    @short_description.setter
    def short_description(self, short_description):
        self._verify_short_description(short_description)

    @property
    def full_description(self):
        return self._full_description

    @full_description.setter
    def full_description(self, full_description):
        self._verify_full_description(full_description)

    @staticmethod
    def check_for_emptiness_or_only_spaces(text) -> bool:
        if text is None or str(text).isspace() or str(text) == "":
            return True
        else:
            return False

    @staticmethod
    def check_the_allowed_caption_length(text: str) -> str:
        if len(text) > Constant.MAX_SIZE_OF_CAPTION_TEXT_IN_TELEGRAM:
            print("Заголовок превысил 1024 символа.Текст был обрезан")
            return text[:Constant.MAX_SIZE_OF_CAPTION_TEXT_IN_TELEGRAM]
        else:
            return text
