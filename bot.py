import telebot
from telebot import types
from telebot.types import ReplyKeyboardRemove

import stats

bot = telebot.TeleBot(open("configs/token").readline().strip())


@bot.message_handler(commands=['start'])
def activate(message):
    bot.send_message(message.chat.id, "Привет, я робот помошник")
    bot.send_message(message.chat.id, "Ты можешь получить температуру или статистику за любой день и время, используя "
                                      "команды /temp или /stats")
    bot.send_message(message.chat.id, "Например: \n\n*Получить текущую температуру:*\n/temp\n\n*Получить температуру "
                                      "за конкретный день и время:*\n /temp "
                                      "06.01.2023 20:54\n\n*Получить температуру за весь день:*\n/temp 06.01.2023\n\n"
                                      "*Получить статистику за конкретный день (от меньшего значения к "
                                      "большему):*\n/stats "
                                      "06.01.2023\n\n*Получить статистику за сегодняшний день:*\n/stats", parse_mode="markdown")
    bot.send_message(message.chat.id, "*Узнать последнее изменение в боте:*\n/bot", parse_mode="markdown")

    # markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # btn1 = types.KeyboardButton("Последняя Температура")
    # markup.add(btn1)


@bot.message_handler(commands=['bot'])
def process_bot(message):
    bot.send_message(message.chat.id, "Вот последнее изменение в боте:")
    bot.send_message(message.chat.id, "Добавление простой команды в статистику, теперь, чтобы узнать статистику за "
                                      "сегодняшний день, вам не нужно вводить текущую дату, просто введите команду "
                                      "*/stats*", parse_mode="markdown")
    bot.send_message(message.chat.id, "Дата изменения(ий): 18.04.2023")


@bot.message_handler(commands=['temp'])
def process_temp(message):
    array = message.text.split()

    result = None

    if len(array) == 3:
        result = stats.get_records_by_datetime(array[1], array[2])
    elif len(array) == 2:
        result = stats.get_records_by_day(array[1])
    elif len(array) == 1:
        result = stats.get_last_temp()
    else:
        result = "Данные введены не верно"

    bot.send_message(message.chat.id, result, parse_mode="markdown")


@bot.message_handler(commands=['stats'])
def process_stats(message):
    array = message.text.split()

    result = None

    if len(array) == 2:
        result = stats.stats_temp(array[1])
    elif len(array) == 1:
        result = stats.last_stats_temp()
    else:
        result = "Данные введены не верно"

    bot.send_message(message.chat.id, result, parse_mode="markdown")


@bot.message_handler(content_types=['text'])
def process_message(message):
    stats_data = stats.get_records_by_day(message.text)

    if stats_data == "":
        bot.send_message(message.chat.id, "Вы ввели несуществующую дату")
    else:
        bot.send_message(message.chat.id, stats_data)
