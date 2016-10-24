import telebot
from telebot import types
import course
import config

bot = telebot.TeleBot(config.token)

user_current_step={}

manual = course.build_course()


@bot.message_handler(commands=['start'])
def handle_updates(command):
    reset_user_progress(get_user_id(command))
    bot.send_message(command.chat.id, "Restarting!")
    next_step(command)


@bot.message_handler(content_types=['text'])
def handle_updates(message):
    next_step(message)


def reset_user_progress(user_id):
    user_current_step[user_id] = 'intro'


def get_next_step(user_id, input):
    if not user_id in user_current_step:
        user_current_step[user_id] = 'intro'
    user_current_step[user_id] = manual[user_current_step[user_id]].next_step(input)
    return user_current_step[user_id]


def get_user_id(message):
    return message.chat.id


def next_step(message):
    user_id = get_user_id(message)
    current_step = get_next_step(user_id, message.text)

    bot_response = manual[current_step].show()

    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
    for option in bot_response.reply_options:
        markup.add(types.KeyboardButton(option))
    bot.send_message(message.chat.id, bot_response.text, reply_markup=markup)


bot.polling(none_stop=True, interval=0)

