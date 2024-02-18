import telebot

bot = telebot.TeleBot('6765117292:AAEDJttvGWNjCSYyZhAXzzERR1579sKtA_E')


@bot.message_handler(commands=['расп'])
def main(message):
    bot.send_message(message.chat.id, 'кгасу не \'_\', сиди кайфуй')


bot.infinity_polling()