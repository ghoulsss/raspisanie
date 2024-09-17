import telebot
from vremya import *
import time
import threading
import schedule

bot = telebot.TeleBot('6765117292:AAEDJttvGWNjCSYyZhAXzzERR1579sKtA_E')


def send_scheduled_message():
    chat_id = "-1002026154974"
    message = Raspisanie.pull_raspisanie()
    bot.send_message(chat_id, message)


# def send_scheduled_message_tomorrow():
#     chat_id = "-1002026154974"
#     message = Raspisanie.pull_raspisanie()
#     bot.send_message(chat_id, message)


def scheduled_task():
    # Запускаем задачу каждый день в 7 и в 8 утра
    schedule.every().day.at("04:00").do(send_scheduled_message)
    # schedule.every().day.at("17:00").do(send_scheduled_message_tomorrow)
    while True:
        schedule.run_pending()
        time.sleep(1)


def main():
    @bot.message_handler(commands=['today'])
    def start(message):
        bot.send_message(message.chat.id, Raspisanie.pull_raspisanie())
        print(1)

    @bot.message_handler(commands=['tomorrow'])
    def start(message):
        # bot.send_message(message.chat.id, Raspisanie.pull_raspisanie())
        bot.send_message(message.chat.id, 'пока не настроил')
        print(1)

    @bot.message_handler(commands=['week'])
    def start(message):
        # bot.send_message(message.chat.id, Raspisanie.pull_raspisanie_nedelya())
        bot.send_message(message.chat.id, 'пока не настроил')
        print(1)

    @bot.message_handler(commands=['next_week'])
    def start(message):
        # bot.send_message(message.chat.id, Raspisanie.pull_raspisanie_next_nedelya(TypeWeek.is_even_week()))
        bot.send_message(message.chat.id, 'пока не настроил')
        print(1)

    thread = threading.Thread(target=scheduled_task)
    thread.start()

    bot.infinity_polling()


if __name__ == '__main__':
    main()
