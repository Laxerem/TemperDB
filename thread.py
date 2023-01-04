import datetime
import time
from threading import Thread

from db import DataBase


def read_temp():
    file = open(r"C:\Users\dreamer\Documents\TEST\TEST_FILE.txt")
    return int(file.readline())


class TempWriter(Thread):

    def __init__(self):
        super().__init__()
        self.db = DataBase()

    def run(self):
        while True:
            value = read_temp()
            self.db.query(f"INSERT INTO data (date, time, value) VALUES ('{datetime.datetime.now().date()}', '{datetime.datetime.now().time()}', {value})")
            time.sleep(60)
