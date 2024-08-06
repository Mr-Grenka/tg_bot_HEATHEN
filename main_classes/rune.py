import sqlite3
from dataclasses import dataclass, field
from data_base.data_base import DataBase
from main_classes.basic_model import BasicModel
from main_classes.constant import Constant


@dataclass(kw_only=True, slots=False)
class Rune(BasicModel):
    _att: int

    def __init__(self, tg_img_id, name, short_description, full_description, att):
        super().__init__(tg_img_id=tg_img_id, name=name, short_description=short_description,
                         full_description=full_description)
        self.verify_att(att)

    @classmethod
    def verify_att(cls, att):
        if str(att).isdigit() and cls.check_for_emptiness_or_only_spaces(att) is False:
            cls._att = int(att)
        else:
            raise TypeError("Атт должен иметь числовое значение и не должен состоять из пробелов или быть Null/None")

    @property
    def att(self):
        return self._att

    @att.setter
    def att(self, att):
        self.verify_att(att)

    @classmethod
    def select_rune_from_db(cls, rune: str) -> 'Rune':
        try:
            cur = DataBase.connect_to_db()
            cur.execute(f"SELECT * FROM runes WHERE name = '{rune}'")
            from_db = cur.fetchone()
            rune_from_db = cls(tg_img_id=from_db[0], name=from_db[1], short_description=from_db[2],
                               full_description=from_db[3], att=from_db[4])
            return rune_from_db

        except sqlite3.OperationalError as sql:
            print(sql)

    # if the field 'att' is empty or str or = 0 in the database, then it is not added
    @staticmethod
    def get_only_all_att_from_db() -> dict:
        all_runes_att = {}
        try:
            cur = DataBase.connect_to_db()
            cur.execute(f"SELECT DISTINCT att From runes")
            temp_atts_tuple = cur.fetchall()
            for atts in temp_atts_tuple:
                for att in atts:
                    if str(att).isdigit() and att != 0:
                        all_runes_att[att] = f"Руны {att} атта"
                    else:
                        print(f"Атт: '{att}' не добавляется в список аттов")
            return dict(sorted(all_runes_att.items()))
        except sqlite3.OperationalError as sql:
            print(sql)

    @staticmethod
    def get_names_of_all_runes_of_current_att(att: int) -> list:
        names_of_runes = []
        try:
            cur = DataBase.connect_to_db()
            cur.execute(f"SELECT name from runes WHERE att = {att}")
            temp_runes_tuple = cur.fetchall()
            for item in temp_runes_tuple:
                for runes_name in item:
                    names_of_runes.append(runes_name)
            return names_of_runes
        except sqlite3.OperationalError as sql:
            print(sql)


