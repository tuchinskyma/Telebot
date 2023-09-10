import telebot
from telebot import types

bot = telebot.TeleBot('6630584114:AAF26ceUl1n5eytz_6MX3uBhPUmBlkRowmI')

users = [5251334860, 990043425, 990043425]


@bot.message_handler(func=lambda message: message.chat.id not in users)
def some(message):
    bot.send_message(message.chat.id, "Извините, но вы не являетесь сотрудником нашей компании.")


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Стандарты ПО 📚')
    item2 = types.KeyboardButton('Документы 📑')
    item3 = types.KeyboardButton('Вводный инструктаж 📄')
    item4 = types.KeyboardButton('Специалисты/Водители📲')
    item5 = types.KeyboardButton('Менеджеры ☎️')
    item6 = types.KeyboardButton('Отзывы для клиентов 👏')

    markup.add(item1, item2, item3, item4, item5, item6)

    bot.send_message(message.chat.id, 'Привет, {0.first_name}!'.format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Менеджеры ☎️':
            bot.send_message(message.chat.id,  """ 🚚
             Екатерина 8-918-558-96-89 
             Старший координатор КО 💁‍♀️
             
             Юрий 8-918-500-36-44 
             Менеджер КО 💁‍♂️
             
             Максим 8-989-715-66-55 
             Руководитель ОР 🤦‍♂️ 
             
             Алексей 8-988-510-55-10 
             Генеральный директор 🙋‍♂️""")
        elif message.text == 'Документы 📑':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('ARCO')
            item2 = types.KeyboardButton('Интермарк')
            item3 = types.KeyboardButton('Договор Ф/Л')
            item4 = types.KeyboardButton('Договор Ю/Л')
            item5 = types.KeyboardButton('Акт-заявка')
            item6 = types.KeyboardButton('Договор ФИКСА')
            back = types.KeyboardButton('⬅️Назад')
            markup.add(item1, item2, item3, item4, item5, item6, back)

            bot.send_message(message.chat.id, 'Примеры документов 📑', reply_markup=markup)

        elif message.text == '⬅️Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Стандарты ПО 📚')
            item2 = types.KeyboardButton('Документы 📑')
            item3 = types.KeyboardButton('Вводный инструктаж 📄️')
            item4 = types.KeyboardButton('Специалисты/Водители📲')
            item5 = types.KeyboardButton('Менеджеры ☎️')
            item6 = types.KeyboardButton('Отзывы для клиентов 👏')

            markup.add(item1, item2, item3, item4, item5, item6)

            bot.send_message(message.chat.id, '⬅️Назад', reply_markup=markup)

        elif message.text == 'Отзывы для клиентов 👏':
            bot.send_message(message.chat.id, """❗️❗️❗️ВАЖНО Чтобы мы смогли идентифицировать заказ, просите клиента в отзыве указать:
➖➖➖➖➖➖➖➖➖➖➖➖
1. Дату - когда были оказаны услуги. 📅
2. Какие работы были оказаны. 🚚
3. Спасибо старшему специалисту "ИМЯ" 🪪
➖➖➖➖➖➖➖➖➖➖➖➖
❗️❗️❗️ПРИМЕР ❗️❗️❗️
10.08.2023 Перевозили квартиру/офис, все очень понравилось. Спасибо старшему специалисту Кириллу.""")
            bot.send_message(message.chat.id, """*Мы будем Вам очень благодарны, если Вы оставите свой отзыв о нашей работе, он поможем другим сделать правильный выбор!*
☺️ ⭐️⭐️⭐️⭐️⭐️ 
в *Яндексе:* 👇 
https://yandex.ru/profile/153729965812/?add-review=true
в *Google:* 👇
https://g.page/r/CRwTujNvz2mjEB0/review
в *2gis:* 👇
https://2gis.ru/rostov/firm/3378228001817870/tab/reviews?writeReview
🙏 *пожалуйста, указывайте в отзыве дату - когда были оказаны услуги и какие работы были оказаны.*""")

        elif message.text == 'ARCO':
            pdf = open('Arco.jpg', 'rb')
            bot.send_document(message.chat.id, pdf)

        elif message.text == 'Интермарк':
            pdf = open('Arco.jpg', 'rb')
            bot.send_document(message.chat.id, pdf)

        elif message.text == 'Договор Ф/Л':
            pdf = open('Arco.jpg', 'rb')
            bot.send_document(message.chat.id, pdf)

        elif message.text == 'Договор Ю/Л':
            pdf = open('Arco.jpg', 'rb')
            bot.send_document(message.chat.id, pdf)

        elif message.text == 'Акт-заявка':
            pdf = open('Arco.jpg', 'rb')
            bot.send_document(message.chat.id, pdf)

        elif message.text == 'Договор ФИКСА':
            pdf = open('Arco.jpg', 'rb')
            bot.send_document(message.chat.id, pdf)

        elif message.text == 'Вводный инструктаж 📄':
            pdf = open('Вводный инструктаж.pdf', 'rb')
            bot.send_document(message.chat.id, pdf)

        elif message.text == 'Специалисты/Водители📲':
            bot.send_message(message.chat.id, """Водители:
             
Борисов Андрей 8 (928) 213 90 80
---------------------------------------
Лаухин Сергей 8 (918) 594 49 43
--------------------------------------- 
Тришин Алексей 8 (918) 552 10 42
---------------------------------------
Бобылев Евгений 8 (961) 292 99 24
---------------------------------------
Шевченко Михаил 8 (951) 508 68 50
---------------------------------------
Понамарев Дмитрий 8 (928) 145 83 90
---------------------------------------
Малютин Владимир 8 (918) 853 83 26
---------------------------------------
Специалисты:

Денис Татаринов 8 (918) 514 16 69
---------------------------------------
Волошин Игорь 8 (993) 452 62 89
---------------------------------------
Морозов Сергей 8 (980) 705 65 31
---------------------------------------
Науменко Сергей 8 (918) 506 43 22
---------------------------------------
Плюхин Кирилл 8 (951) 844 99 70
---------------------------------------
Авдулов Владислав 8 (951) 519 50 07
---------------------------------------
Федотов Иван 8 (961) 297 83 84
---------------------------------------
Жихарев Артем 8 (961) 309 49 03
---------------------------------------
Цямрюк Дмитрий 8 (904) 440 02 02
---------------------------------------
Хасимов Эдуард 8 (909) 773 38 51
---------------------------------------
Чернышев Павел 8 (929) 974 92 91
---------------------------------------
Овчаренко Максим 8 (960) 461 44 46
---------------------------------------
Чукин Александр 8 (951) 525 95 55
             
             """)


bot.polling(none_stop=True)
