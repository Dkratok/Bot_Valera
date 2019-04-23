import telebot
from src.get_rate import *
import datetime
import codecs
from src.logging_module import *

bot = telebot.TeleBot('829206256:AAFfv3BzwQ2uhM2Z_567fNWmcOOUowRj-pg');

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    req = message.text.lower();
    today_date = datetime.date.today();
    today_date_str = str(datetime.date.today());
    tomorrow_date_str = str(today_date + datetime.timedelta(days=1));
    dol = 145;
    euro = 292;
    rub = 298;
    logger.info('Input request: '+message.text+' UserID: '+str(message.from_user.id)+' Firstname: '+str(message.from_user.first_name)+' Lastname: '+str(message.from_user.last_name)+' Username: '+str(message.from_user.username)+' LanguageCode: '+str(message.from_user.language_code));

    try:
        if req == 'привет':
            bot.send_message(message.from_user.id, 'Привет! Я - бот Валера. Чем могу тебе помочь?')
        elif req == 'help':
            help = codecs.open('help.txt', encoding='cp1251');
            bot.send_message(message.from_user.id, help.read(), parse_mode='Markdown')
        elif ('онлайнер' in req) | ('onliner' in req):
            bot.send_message(message.from_user.id, 'https://forum.onliner.by/viewtopic.php?t=21842932')
        elif 'шахматк' in req:
            bot.send_message(message.from_user.id,'https://docs.google.com/spreadsheets/d/1FsztyEWDpmoSrjY22AUcwoa3aGqOZDeli8W-PnEcugA/edit?usp=drivesdk')
        elif ('паспорт объекта' in req) | ('паспорт' in req):
            bot.send_photo(message.from_user.id, open('media/Passport.jpg', 'rb'))
        elif ('документация' in req) | ('доки' in req):
            bot.send_message(message.from_user.id,'https://www.dropbox.com/sh/ga6sp5xdezfpr4h/AADFQYoOrjf2yVK9YjSldEmNa?dl=0')
        elif 'скетч' in req:
            bot.send_photo(message.from_user.id, open('media/Sketch.jpeg', 'rb'))
        elif ('стяжка' in req) | ('схема стяжки' in req):
            bot.send_photo(message.from_user.id, open('media/Floor.jpg', 'rb'))
        elif 'мдк' in req:
            bot.send_message(message.from_user.id,'ОАО «Минский домостроительный комбинат», 220015, г. Минск, ул. Пономаренко, 43. Отдел инвестиций (долевое строительство): (017)207-20-60, (044)7771158, обед с 12 до 12-45. http://minskdsk.by/')
        elif ('рубль' or 'курс рубля') in req:
            bot.send_message(message.from_user.id,'Курс рос. рубля на сегодня ' + today_date_str + ' (за 100 рос. рублей) - ' + str(get_rate_from_json(get_rate_responce(rub))));
            bot.send_message(message.from_user.id,' Курс рос. рубля на завтра ' + tomorrow_date_str + '(за 100 рос. рублей) - ' + str(get_rate_from_json(get_rate_responce(rub, tomorrow_date_str))));
        elif ('доллар' or 'курс доллара') in req:
            bot.send_message(message.from_user.id, 'Курс доллара на сегодня ' + today_date_str + ' - ' + str(get_rate_from_json(get_rate_responce(dol))));
            bot.send_message(message.from_user.id, ' Курс доллара на завтра ' + tomorrow_date_str + ' - ' + str(get_rate_from_json(get_rate_responce(dol, tomorrow_date_str))));
        elif ('евро' or 'курс евро') in req:
            bot.send_message(message.from_user.id, 'Курс евро на сегодня ' + today_date_str + ' - ' + str(get_rate_from_json(get_rate_responce(euro))));
            bot.send_message(message.from_user.id, ' Курс евро на завтра ' + tomorrow_date_str + ' - ' + str(get_rate_from_json(get_rate_responce(euro, tomorrow_date_str))));
        elif ('курсы' or 'курсы валют') in req:
            bot.send_message(message.from_user.id, 'Курс доллара на сегодня ' + today_date_str + ' - ' + str(get_rate_from_json(get_rate_responce(dol))));
            bot.send_message(message.from_user.id, ' Курс доллара на завтра ' + tomorrow_date_str + ' - ' + str(get_rate_from_json(get_rate_responce(dol, tomorrow_date_str))));
            bot.send_message(message.from_user.id, 'Курс евро на сегодня ' + today_date_str + ' - ' + str(get_rate_from_json(get_rate_responce(euro))));
            bot.send_message(message.from_user.id, ' Курс евро на завтра ' + tomorrow_date_str + ' - ' + str(get_rate_from_json(get_rate_responce(euro, tomorrow_date_str))));
            bot.send_message(message.from_user.id, 'Курс рос. рубля на сегодня ' + today_date_str + ' (за 100 рос. рублей) - ' + str(get_rate_from_json(get_rate_responce(rub))));
            bot.send_message(message.from_user.id, ' Курс рос. рубля на завтра ' + tomorrow_date_str + ' (за 100 рос. рублей) - ' + str(get_rate_from_json(get_rate_responce(rub, tomorrow_date_str))));
        else:
            bot.send_message(message.from_user.id,"Моя твоя не понимать. Список вопросов, на которые я могу ответить ты найдёшь по запросу 'help'.")
    except Exception as e:
        logger.info(e);


bot.polling(none_stop=True, interval=0)
