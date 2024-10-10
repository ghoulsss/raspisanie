import telebot
from movements import *
import time
import threading
import schedule

bot = telebot.TeleBot('')


def send_scheduled_message():
    chat_id = ""
    message = Raspisanie.pull_raspisanie()
    bot.send_message(chat_id, message)


def send_scheduled_message_tomorrow():
    chat_id = ""
    message = Raspisanie.pull_raspisanie_tomorrow()
    bot.send_message(chat_id, message)


def scheduled_task():
    schedule.every().day.at("04:00").do(send_scheduled_message)
    schedule.every().day.at("17:00").do(send_scheduled_message_tomorrow)
    while True:
        schedule.run_pending()
        time.sleep(1)


def main():
    @bot.message_handler(commands=['today'])
    def start(message):
        bot.send_message(message.chat.id, text=f'{''.join(Raspisanie.pull_raspisanie())}')

    @bot.message_handler(commands=['tomorrow'])
    def start(message):
        bot.send_message(message.chat.id, Raspisanie.pull_raspisanie_tomorrow())

    thread = threading.Thread(target=scheduled_task)
    thread.start()

    bot.infinity_polling()


if __name__ == '__main__':
    main()
