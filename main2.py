
from thread import TempWriter
from db import DataBase

db = DataBase()
db.query("CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT, time TEXT, value DOUBLE)")

t1 = TempWriter()
t1.start()

print("Введите дату и время")
print("К примеру: 02.01.2023, 22:40")

date2 = str(input())
time2 = str(input())


