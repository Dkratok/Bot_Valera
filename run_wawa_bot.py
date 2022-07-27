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
        elif ('то' in req) | ('регламент' in req) | ('обслуживание' in req):
            bot.send_photo(message.from_user.id, open('media/to.jpg', 'rb'))
        elif ('дилер' in req) | ('dealer' in req):
            bot.send_message(message.from_user.id, rfl.read_whole_file('data/dealers.txt'), parse_mode='Markdown')
        elif ('инструкция' in req) | ('мануал' in req) | ('manual' in req):
            bot.send_document(message.from_user.id, open('media/cruze_manual.pdf', 'rb').read())
        elif ('клуб' in req) | ('чат' in req) | ('chat' in req):
            bot.send_message(message.from_user.id, 'https://t.me/cruzefamily_minsk')
        elif 'габарит' in req:
            bot.send_photo(message.from_user.id, open('media/dimensions.jpg', 'rb'))
        elif 'дворник' in req:
            bot.send_message(message.from_user.id, rfl.read_whole_file('data/wipers.txt'), parse_mode='Markdown')
        elif ('колес' in req) | ('колёс' in req) | ('диски' in req):
            bot.send_message(message.from_user.id, rfl.read_whole_file('data/wheels.txt'), parse_mode='Markdown')
        else:
            bot.send_message(message.from_user.id,"Моя твоя не понимать. Список вопросов, на которые я могу ответить ты найдёшь по запросу 'help'.")
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
