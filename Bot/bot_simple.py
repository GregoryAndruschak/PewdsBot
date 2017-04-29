import Bot.config as config
import telebot

bot = telebot.TeleBot(config.token)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(msg):  # Название функции не играет никакой роли, в принципе
    bot.send_message(msg.chat.id, msg.text)


if __name__ == '__main__':
    bot.polling(none_stop=True)
