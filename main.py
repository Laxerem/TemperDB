from threading import Thread

from bot import bot
from thread import TempWriter
from db import DataBase

db = DataBase()
db.query("CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT, time TEXT, value DOUBLE)")

t1 = TempWriter()
t1.start()


def bot_start():
    while True:
        try:
            bot.polling(none_stop=True, interval=0)
        except ZeroDivisionError:
            pass


t2 = Thread(target=bot_start, daemon=True)
t2.start()


t1.join()
t2.join()
