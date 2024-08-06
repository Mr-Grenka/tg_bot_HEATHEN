import sqlite3
from dataclasses import dataclass, field
from enum import Enum, IntEnum
from data_base.data_base import DataBase
from main_classes.basic_model import BasicModel
from main_classes.constant import Constant


@dataclass(kw_only=True, slots=False)
class World(BasicModel):

    def __init__(self, tg_img_id, name, short_description, full_description):
        super().__init__(tg_img_id=tg_img_id, name=name, short_description=short_description,
                         full_description=full_description)

    @classmethod
    def select_world_from_db(cls, world: str) -> 'World':
        try:
            cur = DataBase.connect_to_db()
            cur.execute(f"SELECT * FROM worlds WHERE name = '{world}'")
            from_db = cur.fetchone()
            world_from_db = cls(tg_img_id=from_db[0], name=from_db[1], short_description=from_db[2],
                                full_description=from_db[3])
            return world_from_db
        except sqlite3.OperationalError as sql:
            print(sql)

    @staticmethod
    def get_dictionary_of_worlds_names() -> dict:
        dictionary_of_worlds = {}
        try:
            cur = DataBase.connect_to_db()
            cur.execute(f"SELECT name FROM worlds")
            temp_tuple = cur.fetchall()
            key = 0
            for item in temp_tuple:
                for i in item:
                    dictionary_of_worlds[key] = i
                    key = key + 1
            return dictionary_of_worlds
        except sqlite3.OperationalError as sql:
            print(sql)


