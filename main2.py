
from thread import TempWriter
from db import DataBase

db = DataBase()
db.query("CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT, time TEXT, value DOUBLE)")

t1 = TempWriter()
t1.start()
t1.join()

# print("Введите дату и время")
# print("К примеру: 02.01.2023, 22:40")
#
# date2 = str(input())
# time2 = str(input())
#
# r = db.fetchall(f"SELECT value FROM data WHERE date = '{date2}' and time = '{time2}'")
# print(r)