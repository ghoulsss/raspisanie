import telebot

bot = telebot.TeleBot('6765117292:AAEDJttvGWNjCSYyZhAXzzERR1579sKtA_E')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'кгасу не \'_\', сиди кайфуй')


@bot.message_handler(commands=['who'])
def who(message):
    bot.send_message(message.chat.id,
                     '')
    bot.send_photo(message.chat.id, )


bot.infinity_polling()
