import sqlite3
from dataclasses import dataclass, field
from enum import Enum, IntEnum
from data_base.data_base import DataBase
from main_classes.basic_model import BasicModel
from main_classes.constant import Constant


# ás - singular asir - plural по русски Ас и Ассы
# vanr  singular vanir - plural по русски ван и ваны

@dataclass
class Gods(BasicModel):
    _type_of_god: str
    _capabilities: str

    def __init__(self, tg_img_id, name, short_description, full_description, type_of_god, capabilities):
        super().__init__(tg_img_id=tg_img_id, name=name, short_description=short_description,
                         full_description=full_description)
        self._verify_type_of_god(type_of_god)
        self._verify_capabilities(capabilities)

    @classmethod
    def _verify_type_of_god(cls, type_of_god):
        if cls.check_for_emptiness_or_only_spaces(type_of_god):
            cls._type_of_god = Constant.IF_TEXT_IS_EMPTY
        else:
            cls._type_of_god = type_of_god

    @classmethod
    def _verify_capabilities(cls, capabilities):
        if cls.check_for_emptiness_or_only_spaces(capabilities):
            cls._capabilities = Constant.IF_CAPABILITIES_IS_EMPTY
        else:
            cls._capabilities = capabilities

    @property
    def type_of_god(self):
        return self._type_of_god

    @type_of_god.setter
    def type_of_god(self, type_of_god):
        self._verify_type_of_god(type_of_god)

    @property
    def capabilities(self):
        return self._capabilities

    @capabilities.setter
    def capabilities(self, capabilities):
        self._verify_capabilities(capabilities)

    @classmethod
    def get_only_types_of_gods_db(cls) -> list:
        all_types_of_gods = []
        cur = DataBase.connect_to_db()
        cur.execute(f"SELECT DISTINCT type_of_god From gods")
        temp_types_of_gods_tuple = cur.fetchall()
        for types in temp_types_of_gods_tuple:
            for type_ in types:
                if cls.check_for_emptiness_or_only_spaces(type_) is False:
                    all_types_of_gods.append(type_)
                else:
                    print(f"Тип: '{type_}' не добавляется в список аттов")
        return list(sorted(all_types_of_gods))

    @classmethod
    def get_gods_from_db(cls, type_of_god) -> list:
        names_of_gods = []
        cur = DataBase.connect_to_db()
        cur.execute(f"SELECT name from gods WHERE type_of_god = '{type_of_god}'")
        temp_gods_tuple = cur.fetchall()
        for gods in temp_gods_tuple:
            for god in gods:
                names_of_gods.append(god)

        return names_of_gods

    @classmethod
    def get_god_from_db(cls, gods_name) -> 'Gods':
        try:
            cur = DataBase.connect_to_db()
            cur.execute(f"SELECT * FROM gods WHERE name = '{gods_name}'")
            from_db = cur.fetchone()
            god_from_db = cls(tg_img_id=from_db[0], name=from_db[1], short_description=from_db[2],
                              full_description=from_db[3], type_of_god=from_db[4], capabilities=from_db[5])
            return god_from_db

        except sqlite3.OperationalError as sql:
            print(sql)

    @classmethod
    def get_main_info_of_god_for_creating_book_menu(cls, gods_name) -> dict:
        main_info_of_god = {}
        god_info = cls.get_god_from_db(gods_name)
        main_info_of_god[1] = god_info.short_description
        main_info_of_god[2] = god_info.full_description
        main_info_of_god[3] = god_info.capabilities
        return main_info_of_god
