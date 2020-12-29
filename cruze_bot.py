import time
import telebot
from src.get_rate import *
import datetime
import src.read_from_files as rfl
from src.logging_module import *

bot = telebot.TeleBot('1490395742:AAFONIhyk_it0_o1mnyKaE3fM_bS2AqD4fE')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    req = message.text.lower()
    today_date = datetime.date.today()
    today_date_str = str(datetime.date.today())
    tomorrow_date_str = str(today_date + datetime.timedelta(days=1))
    dol = 145
    euro = 292
    rub = 298
    logger.info('Input request: '+message.text+' UserID: '+str(message.from_user.id)+' Firstname: '+str(message.from_user.first_name)+' Lastname: '+str(message.from_user.last_name)+' Username: '+str(message.from_user.username)+' LanguageCode: '+str(message.from_user.language_code))

    try:
        if req == 'привет':
            bot.send_message(message.from_user.id, "Привет! Я - бот Кузя. Если нужна помощь пищи 'помощь' или 'help'. Чем могу тебе помочь?")
        elif ('помощь' in req) | ('help' in req):
            bot.send_message(message.from_user.id, rfl.read_whole_file('data/help.txt'), parse_mode='Markdown')
        elif ('то' in req) | ('регламент' in req) | ('обслуживание' in req):
            bot.send_photo(message.from_user.id, open('media/to.jpg', 'rb'))
        elif ('дилер' in req) | ('dealer' in req):
            bot.send_message(message.from_user.id, rfl.read_whole_file('data/dealers.txt'), parse_mode='Markdown')
        elif ('инструкция' in req) | ('мануал' in req) | ('manual' in req):
            bot.send_document(message.from_user.id, open('media/cruze_manual.pdf', 'rb').read())
        elif ('клуб' in req) | ('чат' in req) | ('chat' in req):
            bot.send_message(message.from_user.id, 'https://t.me/cruzefamily_minsk')
        elif 'дворник' in req:
            bot.send_message(message.from_user.id, rfl.read_whole_file('data/wipers.txt'), parse_mode='Markdown')
        elif ('колес' in req) | ('колёс' in req) | ('диски' in req):
            bot.send_message(message.from_user.id, rfl.read_whole_file('data/wheels.txt'), parse_mode='Markdown')
        elif ('рубль' or 'курс рубля') in req:
            bot.send_message(message.from_user.id, 'Курс рос. рубля на сегодня ' + today_date_str + ' (за 100 рос. рублей) - ' + str(get_rate_from_json(get_rate_response(rub))))
            bot.send_message(message.from_user.id, ' Курс рос. рубля на завтра ' + tomorrow_date_str + '(за 100 рос. рублей) - ' + str(get_rate_from_json(get_rate_response(rub, tomorrow_date_str))))
        elif ('доллар' or 'курс доллара') in req:
            bot.send_message(message.from_user.id, 'Курс доллара на сегодня ' + today_date_str + ' - ' + str(get_rate_from_json(get_rate_response(dol))))
            bot.send_message(message.from_user.id, ' Курс доллара на завтра ' + tomorrow_date_str + ' - ' + str(get_rate_from_json(get_rate_response(dol, tomorrow_date_str))))
        elif ('евро' or 'курс евро') in req:
            bot.send_message(message.from_user.id, 'Курс евро на сегодня ' + today_date_str + ' - ' + str(get_rate_from_json(get_rate_response(euro))))
            bot.send_message(message.from_user.id, ' Курс евро на завтра ' + tomorrow_date_str + ' - ' + str(get_rate_from_json(get_rate_response(euro, tomorrow_date_str))))
        elif ('курсы' or 'курсы валют') in req:
            bot.send_message(message.from_user.id, 'Курс доллара на сегодня ' + today_date_str + ' - ' + str(get_rate_from_json(get_rate_response(dol))))
            bot.send_message(message.from_user.id, ' Курс доллара на завтра ' + tomorrow_date_str + ' - ' + str(get_rate_from_json(get_rate_response(dol, tomorrow_date_str))))
            bot.send_message(message.from_user.id, 'Курс евро на сегодня ' + today_date_str + ' - ' + str(get_rate_from_json(get_rate_response(euro))))
            bot.send_message(message.from_user.id, ' Курс евро на завтра ' + tomorrow_date_str + ' - ' + str(get_rate_from_json(get_rate_response(euro, tomorrow_date_str))))
            bot.send_message(message.from_user.id, 'Курс рос. рубля на сегодня ' + today_date_str + ' (за 100 рос. рублей) - ' + str(get_rate_from_json(get_rate_response(rub))))
            bot.send_message(message.from_user.id, ' Курс рос. рубля на завтра ' + tomorrow_date_str + ' (за 100 рос. рублей) - ' + str(get_rate_from_json(get_rate_response(rub, tomorrow_date_str))))
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
