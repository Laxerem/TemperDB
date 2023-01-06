import telebot
import stats

bot = telebot.TeleBot(open("configs/token").readlines()[0])


@bot.message_handler(commands=['start'])
def activate(message):
    bot.send_message(message.chat.id, "Привет, я робот помошник")
    bot.send_message(message.chat.id, "Ты можешь получить статистику за любой день и время, используя команду /stats")
    bot.send_message(message.chat.id, "Например: \n\n*Получить текущую температуру:*\n/stats\n\n*Получить температуру за конкретный день и время:*\n /stats "
                                      "06.01.2023 20:54\n\n*Получить статистику за весь день:*\n/stats 06.01.2023", parse_mode="markdown")


@bot.message_handler(commands=['stats'])
def process_stats(message):

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


@bot.message_handler(content_types=['text'])
def process_message(message):

    stats_data = stats.get_records_by_day(message.text)

    if stats_data == "":
        bot.send_message(message.chat.id, "Вы ввели несуществующую дату")
    else:
        bot.send_message(message.chat.id, stats_data)
