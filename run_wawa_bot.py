import time
import telebot
from telebot import types
import src.read_from_files as rfl
from src.logging_module import *

bot = telebot.TeleBot(rfl.read_whole_file('token.txt'))
markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
markup.add('Нашы рэгулярныя забегi', 'Масавыя забегі ў Варшаве', 'Набыць экіпіроўку', 'Карысныя спасылкі', 'Кнiгi', 'Падкасты')


@bot.message_handler(commands=['start'])
def get_start_messages(message):
    bot.send_message(message.from_user.id, rfl.read_whole_file('data/help.txt'), reply_markup=markup, parse_mode='Markdown')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    req = message.text.lower()
    logger.info('Input request: '+message.text+' UserID: '+str(message.from_user.id)+' Firstname: '
                +str(message.from_user.first_name)+' Lastname: '+str(message.from_user.last_name)+' Username: '
                +str(message.from_user.username)+' LanguageCode: '+str(message.from_user.language_code))

    try:
        if ('дапамога' in req) | ('помощь' in req) | ('help' in req) | ('вiтаю' in req) | ('прывiтанне' in req) | ('привет' in req):
            bot.send_message(message.from_user.id, rfl.read_whole_file('data/help.txt'), reply_markup=markup, parse_mode='Markdown')
        elif ('нашы рэгулярныя забегi' in req):
            bot.send_message(message.from_user.id, rfl.read_whole_file('data/reg_runs.txt'), parse_mode='HTML')
        elif ('масавыя забегі ў варшаве' in req):
            bot.send_message(message.from_user.id, rfl.read_whole_file('data/mass_run.txt'), parse_mode='Markdown')
        elif ('набыць экіпіроўку' in req):
            bot.send_message(message.from_user.id, rfl.read_whole_file('data/shops.txt'), parse_mode='Markdown')
        elif ('карысныя спасылкі' in req):
            bot.send_message(message.from_user.id, rfl.read_whole_file("data/links.txt"), parse_mode='HTML')
        elif ('кнiгi' in req):
            bot.send_message(message.from_user.id, rfl.read_whole_file("data/books.txt"), parse_mode='Markdown')
        elif ('падкасты' in req):
            bot.send_message(message.from_user.id, rfl.read_whole_file("data/podcasts.txt"), parse_mode='Markdown')
        else:
            bot.send_message(message.from_user.id,"Мая твая не разумець. Спіс пытанняў, на якія я магу адказаць, "
                                                  "ты знойдзеш па запыце 'help'.",  reply_markup=markup, parse_mode='Markdown')
    except Exception as e:
        logger.info(e)


if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            time.sleep(3)
            logger.error(f'error: {e}')
            print(str(e))
