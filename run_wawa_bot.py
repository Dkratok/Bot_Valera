import time
import telebot
import src.read_from_files as rfl
from src.logging_module import *

bot = telebot.TeleBot(rfl.read_whole_file('token.txt'))


@bot.message_handler(commands=['start'])
def get_start_messages(message):
    bot.send_message(message.from_user.id, rfl.read_whole_file('data/help.txt'), parse_mode='Markdown')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    req = message.text.lower()
    logger.info('Input request: '+message.text+' UserID: '+str(message.from_user.id)+' Firstname: '
                +str(message.from_user.first_name)+' Lastname: '+str(message.from_user.last_name)+' Username: '
                +str(message.from_user.username)+' LanguageCode: '+str(message.from_user.language_code))

    try:
        if ('вiтаю' in req) | ('прывiтанне' in req) | ('привет' in req):
            bot.send_message(message.from_user.id, "Вiтаю! Я - RunWawaBot, дапамагу табе з адаптацыяй да нашай тусоўкi"
                                                   " бегуноў, а таксама з пошукам экіпіроўкі для бегуноў. Цiснi кнопку"
                                                   " ў залежнасцi ад таго, якое пытанне цiкавiць.")
        elif ('дапамога' in req) | ('помощь' in req) | ('help' in req):
            bot.send_message(message.from_user.id, rfl.read_whole_file('data/help.txt'), parse_mode='Markdown')
        elif ('нашы рэгулярныя забегi' in req):
            bot.send_photo(message.from_user.id, open('data/reg_runs.txt'))
        elif ('масавыя забегі ў варшаве' in req) | ('mass_run.txt' in req):
            bot.send_message(message.from_user.id, rfl.read_whole_file('data/shops.txt'), parse_mode='Markdown')
        elif ('набыць экіпіроўку' in req):
            bot.send_document(message.from_user.id, open('data/shops.txt'), parse_mode='Markdown')
        elif ('спасылкі' in req):
            bot.send_message(message.from_user.id, open('data/links.txt'), parse_mode='Markdown')
        else:
            bot.send_message(message.from_user.id,"Мая твая не разумець. Спіс пытанняў, на якія я магу адказаць, ты знойдзеш па запыце 'help'.")
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
