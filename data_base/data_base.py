import sqlite3 as sq
import os


class DataBase:
    PATH_TO_DB = "C:/Programming/Python/TgBot_HEATHEN/Heathen/norse.sqlite3"

    @classmethod
    def find_db(cls) -> bool:
        return os.path.exists(cls.PATH_TO_DB)

    @classmethod
    def connect_to_db(cls):
        if cls.find_db():
            with sq.connect(cls.PATH_TO_DB) as con:
                cur = con.cursor()
                return cur
        else:
            print("DataBase not found")


