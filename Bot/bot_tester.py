import Bot.config as config
import telebot

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def a(msg):
    bot.send_message(msg.chat.id, 'Your name: {0}\nYour id: {1}'.format(msg.chat.first_name, msg.chat.id))
    print(msg.chat.first_name)


@bot.message_handler(commands=['help'])
def help_message(msg):
    bot.send_message(msg.chat.id, config.help_)


if __name__ == '__main__':
    bot.polling(none_stop=True)