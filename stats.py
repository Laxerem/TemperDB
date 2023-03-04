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

    if len(rows) == 0:
        query = "SELECT * FROM (SELECT time, value FROM data WHERE date=? and time<? ORDER BY id DESC LIMIT 1) UNION " + \
                "SELECT * FROM (SELECT time, value FROM data WHERE date=? and time>? ORDER BY 'date' DESC LIMIT 1)"
        rows = db.fetchall(query, date, time, date, time)

        for row in rows:
            result += f"*{row[0]}, {row[1]}*\n"
    else:
        for row in rows:
            result += f"{row[0]}\n"

    if result == "":
        result = "нет записей, удовлетворяющих условию"

        return result

    return result


def get_last_temp():
    rows = db.fetchall(f"SELECT value, date, time  FROM data ORDER BY id DESC LIMIT 1")
    result = f"*{rows[0][0]}*\n\n _{rows[0][1]} {rows[0][2]}_"
    return result


def stats_temp(date):
    rows = db.fetchall(f"SELECT time, value FROM data WHERE date=? ORDER BY value ASC", date)
    result = str()

    for row in rows:
        result += f"{row[0]}, {row[1]}"
        result += "\n"

    return result


def last_stats_temp():
    rows = db.fetchall(f"SELECT date, time, value FROM data ORDER BY date DESC, value ASC")
