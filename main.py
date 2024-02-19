import telebot
from vremya import *

bot = telebot.TeleBot('6765117292:AAEDJttvGWNjCSYyZhAXzzERR1579sKtA_E')


def main():
    @bot.message_handler(commands=['rasp', 'today'])
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

    @bot.message_handler(commands=['next week'])
    def start(message):
        bot.send_message(message.chat.id, ReadRasp.pull_raspisanie_next_nedelya(TypeWeek.is_even_week()))

    # @bot.message_handler()
    # def start(message):
    #     if message.text.lower().startswith('расп') or message.text.lower().startswith('rasp'):
    #         bot.send_message(message.chat.id, ReadRasp.pull_raspisanie(TypeWeek.is_even_week(), TypeWeek.current_day))
    #     elif (message.text.lower() == 'неделя' or message.text.lower().startswith('нед')
    #           or message.text.lower() == 'week'):
    #         bot.send_message(message.chat.id, ReadRasp.pull_raspisanie_nedelya(TypeWeek.is_even_week()))
    #     elif message.text.lower() == 'завтра' or message.text.lower() == 'tomorrow':
    #         bot.send_message(message.chat.id, ReadRasp.pull_raspisanie(TypeWeek.is_even_week(TypeWeek.tomorrow_date),
    #                                                                    TypeWeek.days[datetime.now(pytz.timezone(
    #                                                                        'Europe/Moscow')).weekday() + 2]))

    bot.infinity_polling()


if __name__ == '__main__':
    main()
