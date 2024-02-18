import telebot
import vremya

bot = telebot.TeleBot('6765117292:AAEDJttvGWNjCSYyZhAXzzERR1579sKtA_E')


def main():
    @bot.message_handler(commands=['расп'])
    def main(message):
        vremya.change_week()
        bot.send_message(message.chat.id, f'сегодня {vremya.type_week}, {vremya.current_day}')

    bot.infinity_polling()


if __name__ == '__main__':
    main()