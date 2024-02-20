import telebot
from vremya import *
import schedule
import time
import threading

bot = telebot.TeleBot('6765117292:AAEDJttvGWNjCSYyZhAXzzERR1579sKtA_E')


def send_scheduled_message():
    chat_id = "-1002026154974"
    message = ReadRasp.pull_raspisanie(TypeWeek.is_even_week(), TypeWeek.current_day)
    if TypeWeek.current_day in ('Суббота', 'Воскресенье'):
        message = 'Сегодня выходной'
    bot.send_message(chat_id, message)


def send_scheduled_message_tomorrow():
    chat_id = "-1002026154974"
    message = ReadRasp.pull_raspisanie(TypeWeek.is_even_week(TypeWeek.tomorrow_date),
                                       TypeWeek.days[datetime.now(pytz.timezone(
                                           'Europe/Moscow')).weekday() + 2])
    if TypeWeek.days[datetime.now(pytz.timezone('Europe/Moscow')).weekday() + 2] in ('Суббота', 'Воскресенье'):
        message = 'Завтра выходной'
    bot.send_message(chat_id, message)


def scheduled_task():
    # Запускаем задачу каждый день в 12:00 по времени 'Europe/Moscow'
    schedule.every().day.at("07:00").do(send_scheduled_message)
    schedule.every().day.at("20:00").do(send_scheduled_message_tomorrow)
    while True:
        schedule.run_pending()
        time.sleep(1)


def main():
    @bot.message_handler(commands=['today'])
    def start(message):
        bot.send_message(message.chat.id, ReadRasp.pull_raspisanie(TypeWeek.is_even_week(), TypeWeek.current_day))

    @bot.message_handler(commands=['tomorrow'])
    def start(message):
        bot.send_message(message.chat.id, ReadRasp.pull_raspisanie(TypeWeek.is_even_week(TypeWeek.tomorrow_date),
                                                                   TypeWeek.days[datetime.now(pytz.timezone(
                                                                       'Europe/Moscow')).weekday() + 2]))

    @bot.message_handler(commands=['week'])
    def start(message):
        bot.send_message(message.chat.id, ReadRasp.pull_raspisanie_nedelya(TypeWeek.is_even_week()))

    @bot.message_handler(commands=['next_week'])
    def start(message):
        bot.send_message(message.chat.id, ReadRasp.pull_raspisanie_next_nedelya(TypeWeek.is_even_week()))

    thread = threading.Thread(target=scheduled_task)
    thread.start()

    bot.infinity_polling()


if __name__ == '__main__':
    main()
