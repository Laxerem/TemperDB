from db import DataBase

db = DataBase()


def get_records_by_day(date):
    rows = db.fetchall(f"SELECT time, value FROM data WHERE date = ?", date)
    result = str()

    for row in rows:
        result += f"{row[0]} - {row[1]}"
        result += "\n"

    return result


def get_records_by_datetime(date, time):
    rows = db.fetchall(f"SELECT value FROM data WHERE time = ? and date = ?", time, date)
    result = str()

    for row in rows:
        result += f"{row[0]}\n"

    return result


def get_last_temp():
    rows = db.fetchall(f"SELECT value, date, time  FROM data ORDER BY date DESC, time DESC LIMIT 1")
    result = f"*{rows[0][0]}*\n\n _{rows[0][1]} {rows[0][2]}_"
    return result
