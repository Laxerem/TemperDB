import sqlite3


class DataBase:

    def query(self, query):
        db = sqlite3.connect("temper.db")
        cursor = db.cursor()
        cursor.execute(query)
        db.commit()
        cursor.close()

    def fetchall(self, query, *args):
        db = sqlite3.connect("temper.db")
        cursor = db.cursor()
        cursor.execute(query, args)
        db.commit()
        return cursor.fetchall()
