import sqlite3
from dataclasses import dataclass
from enum import Enum
from data_base.data_base import DataBase
from main_classes.basic_model import BasicModel
from main_classes.constant import Constant


class BasicPhrasesEnum(Enum):
    starting_greeting = "приветствие"
    help = "помощь"
    info = "информация"


# Выборка из таблицы basic_phrases в бд захардкодена посредством Enum, так как не подразумевает добавления новых данных
# допустимо только редактирование существующих
@dataclass(kw_only=True)
class BasicPhrases:
    __tg_img_id: str
    __keyword: str
    __phrase: str

    def __init__(self, tg_img_id, keyword, phrase):
        self.verify_tg_img_id(tg_img_id)
        self.verify_keyword(keyword)
        self.verify_phrase(phrase)

    @classmethod
    def verify_tg_img_id(cls, tg_img_id):
        if BasicModel.check_for_emptiness_or_only_spaces(tg_img_id):
            cls.__tg_img_id = Constant.IF_IMG_IS_EMPTY
        else:
            cls.__tg_img_id = tg_img_id

    @classmethod
    def verify_keyword(cls, keyword):
        if BasicPhrasesEnum.__contains__(keyword):
            cls.__keyword = keyword
        else:
            cls.__keyword = Constant.IF_NAME_IS_EMPTY

    @classmethod
    def verify_phrase(cls, phrase):
        if BasicModel.check_for_emptiness_or_only_spaces(phrase):
            cls.__phrase = Constant.IF_TEXT_IS_EMPTY
        else:
            cls.__phrase = phrase

    @property
    def tg_img_id(self):
        return self.__tg_img_id

    @tg_img_id.setter
    def tg_img_id(self, tg_img_id):
        self.verify_tg_img_id(tg_img_id)

    @property
    def keyword(self):
        return self.__keyword

    @keyword.setter
    def keyword(self, keyword):
        self.verify_keyword(keyword)

    @property
    def phrase(self):
        return self.__phrase

    @phrase.setter
    def phrase(self, phrase):
        self.verify_phrase(phrase)

    @classmethod
    def select_phrase_from_db(cls, phrase: BasicPhrasesEnum) -> 'BasicPhrases':
        try:
            cur = DataBase.connect_to_db()
            cur.execute(f"SELECT * FROM basic_phrases WHERE key_word = '{phrase.value}'")
            from_db = cur.fetchone()
            phrase_from_db = cls(tg_img_id=from_db[0], keyword=from_db[1], phrase=from_db[2])
            return phrase_from_db

        except sqlite3.OperationalError as sql:
            print(sql)



