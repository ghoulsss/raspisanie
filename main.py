import telebot
from vremya import *


bot = telebot.TeleBot('6765117292:AAEDJttvGWNjCSYyZhAXzzERR1579sKtA_E')


def main():
    @bot.message_handler()
    def start(message):
        if message.text.lower().startswith('р'):
            TypeWeek.check_type_week()
            bot.send_message(message.chat.id, f'сегодня {TypeWeek.translate_type_week},'
                                              f' {TypeWeek.current_day} день недели')
        elif message.text.lower() in ('чет', 'нечет', 'неделя',):
            bot.send_message(message.chat.id, TypeWeek.translate_type_week)
    bot.infinity_polling()


if __name__ == '__main__':
    main()