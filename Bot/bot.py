import Bot.config as config
import Bot.hparser as hp
import Bot.tkn as token
import telebot

bot = telebot.TeleBot(token.token)

users = {}


class User(object):
    num_of_users = 0

    def __init__(self, id_, first_name, username, last_name=None):
        self.id_ = id_
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        User.num_of_users += 1
        u = open('../users.txt', 'a')
        u.write(self.to_string())
        u.close()

    def to_string(self):
        return config.user_info.format(self.first_name, self.last_name, self.username, self.id_)


@bot.message_handler(commands=['start'])
def start_message(msg):
    global users
    if msg.chat.id not in users:
        users.update({msg.chat.id: User(msg.chat.id, msg.chat.first_name, msg.chat.username, msg.chat.last_name)})
        user = users.get(msg.chat.id)

        # bot.send_message(user.id_, config.user_info.format(user.first_name, user.last_name, user.username, user.id_))

        bot.send_message(user.id_, config.start.format(user.first_name))
        bot.send_message(user.id_, config.help_)
    else:
        user = users.get(msg.chat.id)

        # bot.send_message(user.id_, config.user_info.format(user.first_name, user.last_name, user.username, user.id_))
        # bot.send_photo(user_id, config.triforse)
        bot.send_message(user.id_, config.start.format(user.first_name))
        bot.send_message(user.id_, config.help_)


@bot.message_handler(commands=['help'])
def help_message(msg):
    bot.send_message(msg.chat.id, config.help_)


@bot.message_handler(commands=['videos'])
def list_videos(msg):
    videos = hp.get_titles()
    result = ''
    counter = 0
    for v in videos:
        counter += 1
        temp = config.videos.format(counter, v.title, v.link)
        result += temp
    bot.send_message(msg.chat.id, result, disable_web_page_preview=True)


@bot.message_handler(commands=['new'])
def new_video(msg):
    video = hp.get_new()
    result = config.new_video.format(video.title, video.link)
    bot.send_message(msg.chat.id, result)

if __name__ == '__main__':
    bot.polling(none_stop=True)
