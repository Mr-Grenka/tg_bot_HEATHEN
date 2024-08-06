import sqlite3
from dataclasses import dataclass
from data_base.data_base import DataBase
from main_classes.basic_model import BasicModel


@dataclass(kw_only=True, slots=False)
class Story(BasicModel):

    def __init__(self, tg_img_id, name, short_description, full_description):
        super().__init__(tg_img_id=tg_img_id, name=name, short_description=short_description,
                         full_description=full_description)

    @classmethod
    def select_story_from_db(cls, story: str) -> 'Story':
        try:
            cur = DataBase.connect_to_db()
            cur.execute(f"SELECT * FROM stories WHERE name = '{story}'")
            from_db = cur.fetchone()
            story_from_db = cls(tg_img_id=from_db[0], name=from_db[1], short_description=from_db[2],
                                full_description=from_db[3])
            return story_from_db

        except sqlite3.OperationalError as sql:
            print(sql)

    @staticmethod
    def select_all_story_names_from_db() -> list:
        all_stories_list = []
        try:
            cur = DataBase.connect_to_db()
            cur.execute(f"SELECT name FROM stories")
            temp_tuple = cur.fetchall()
            for item in temp_tuple:
                for i in item:
                    all_stories_list.append(i)
            return all_stories_list

        except sqlite3.OperationalError as sql:
            print(sql)


