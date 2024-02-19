import telebot
from vremya import *


bot = telebot.TeleBot('6765117292:AAEDJttvGWNjCSYyZhAXzzERR1579sKtA_E')


def main():
    @bot.message_handler()
    def start(message):
        if message.text.lower().startswith('р'):
            bot.send_message(message.chat.id, ReadRasp.pull_raspisanie(TypeWeek.is_even_week(), TypeWeek.current_day))
        elif message.text.lower() in ('чет', 'нечет', 'неделя',):
            bot.send_message(message.chat.id, TypeWeek.is_even_week())
    bot.infinity_polling()


if __name__ == '__main__':
    main()