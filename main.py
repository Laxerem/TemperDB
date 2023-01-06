from threading import Thread

from bot import bot
from thread import TempWriter
from db import DataBase

db = DataBase()
db.query("CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT, time TEXT, value DOUBLE)")

t1 = TempWriter()
t1.start()

t2 = Thread(target=bot.polling, daemon=True, kwargs={'none_stop': True, 'interval': 0})
t2.start()

t1.join()
t2.join()
