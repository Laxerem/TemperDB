import datetime
import time
from threading import Thread

from db import DataBase


def read_temp():
    file = open(open("configs/path_to_temp").readline().strip())
    return int(file.readline())


class TempWriter(Thread):

    def __init__(self):
        super().__init__(daemon=True)
        self.db = DataBase()

    def run(self):
        while True:
            value = read_temp() / 1000
            date = datetime.datetime.now()
            if value < 50:
                self.db.query(f"INSERT INTO data (date, time, value) VALUES ('{date.strftime('%d.%m.%Y')}', '{date.strftime('%H:%M')}', {value})")
                time.sleep(1800)
            else:
                time.sleep(30)
