import sqlite3
from dataclasses import dataclass, field
from enum import Enum

from data_base.data_base import DataBase
from main_classes.basic_model import BasicModel
from main_classes.constant import Constant


# this is structure of bot
# and this is hardcode, don't touch!!!
class GuideToNorseMythologyEnum(Enum):
    runes = "Руны"
    worlds = "Миры"
    gods = "Боги"
    stories = "Истории"
    symbolism = "Символика"
    return_to_main_menu = "Главное меню"


@dataclass
class GuideToNorseMythology:
    __tg_imd_id: str
    __section: str
    __description: str
    MAIN_MENU = "Главное меню"

    def __init__(self, tg_imd_id, section, description):
        self.__verify_tg_img_id(tg_imd_id)
        self.__verify_section(section)
        self.__verify_description(description)

    @classmethod
    def __verify_tg_img_id(cls, tg_img_id):
        if BasicModel.check_for_emptiness_or_only_spaces(tg_img_id):
            cls.__tg_imd_id = Constant.IF_IMG_IS_EMPTY
        else:
            cls.__tg_imd_id = tg_img_id

    @classmethod
    def __verify_section(cls, section):
        if BasicModel.check_for_emptiness_or_only_spaces(section):
            raise TypeError("Раздел меню не может быть пробелом и не должно быть Null/None")
        else:
            cls.__section = section

    @classmethod
    def __verify_description(cls, description):
        if BasicModel.check_for_emptiness_or_only_spaces(description):
            cls.__description = Constant.IF_FULL_DESCRIPTION_IS_EMPTY
        else:
            cls.__description = description

    @classmethod
    def select_menu_section_from_db(cls, section: str) -> 'GuideToNorseMythology':
        cur = DataBase.connect_to_db()
        cur.execute(f"SELECT * FROM guide_to_norse_mythology WHERE section = '{section}'")
        from_db = cur.fetchone()
        menu_section_from_db = cls(tg_imd_id=from_db[0], section=from_db[1], description=from_db[2])
        return menu_section_from_db

    @property
    def tg_img_id(self):
        return self.__tg_imd_id

    @tg_img_id.setter
    def tg_img_id(self, tg_img_id):
        self.__verify_tg_img_id(tg_img_id)

    @property
    def section(self):
        return self.__section

    @section.setter
    def section(self, section):
        self.__verify_section(section)

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__verify_description(description)

    @staticmethod
    def select_all_section_from_db() -> list:
        main_menu_list = []
        cur = DataBase.connect_to_db()
        try:
            cur.execute(f"SELECT section FROM guide_to_norse_mythology")
            temp_tuple = cur.fetchall()
            for item in temp_tuple:
                for i in item:
                    main_menu_list.append(i)
            return main_menu_list
        except sqlite3.OperationalError as sq:
            print(f"{sq}. С базой банных что-то не так")
            return main_menu_list

