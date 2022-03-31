import telebot
from telebot import types
import random

bot = telebot.TeleBot('5278792568:AAFt3lJxrghz3F7WiMCKXxsQsfOQ3FC0Lqo')

@bot.message_handler(commands=["start"])
def start(message, res=False):
    chat_id = message.chat.id

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Главное меню")
    btn2 = types.KeyboardButton("Помощь")
    markup.add(btn1, btn2)

    bot.send_message(chat_id,
                     text="Привет, {0.first_name}! Я тестовый бот для курса программирования на языке Python".format(
                         message.from_user))
# -----------------------------------------------------------------------
# Получение сообщений от юзера
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    chat_id = message.chat.id
    ms_text = message.text

    if ms_text == "Главное меню" or ms_text == "👋🏻 Главное меню" or ms_text == "Вернуться в главное меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Прогулки")
        btn2 = types.KeyboardButton("Кафе/рестораны")
        back = types.KeyboardButton("Помощь")
        markup.add(btn1, btn2, back)
        bot.send_message(chat_id, text="Вы в главном меню", reply_markup=markup)

    elif ms_text == "Прогулки":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Василеостровский район")
        btn2 = types.KeyboardButton("Адмиралтейский район")
        btn3 = types.KeyboardButton("Московский район")
        btn4 = types.KeyboardButton("Невский район")
        btn5 = types.KeyboardButton("Петроградский район")
        btn6 = types.KeyboardButton("Вернуться в главное меню")
        back = types.KeyboardButton("Помощь")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, back)
        bot.send_message(chat_id, text="Прогулки", reply_markup=markup)

    elif ms_text == "Василеостровский район":
        vplace1 = "Сад Академии художеств"
        vplace2 = "Египетские сфинксы на берегу Невы"
        vplace3 = "Особняк Брусницыных"
        vplace4 = "Музей современного искусства Эрарта"
        vplace5 = "Памятник бомбардиру Василию"
        vplace6 = "Стрелка Васильевского острова"
        vplace7 = "Дворец Меншикова"
        vplace8 = "Улица Репина"
        vplace9 = "Двор духов"
        vplace10 = "Севкабель Порт"
        vplace = random.choice([vplace1, vplace2, vplace3, vplace4, vplace5, vplace6, vplace7, vplace8, vplace9, vplace10])
        bot.send_message(chat_id, text="Можно посетить " + vplace)
        if vplace == "Сад Академии художеств":
            bot.send_photo(chat_id, open('G:\pythonProject\img\SAH.jpg', 'rb'))
            bot.send_message(chat_id, text="Университетская наб., 17, находится между 3 и 4 линиями ВО")
        elif vplace == "Египетские сфинксы на берегу Невы":
            bot.send_photo(chat_id, open('G:\pythonProject\img\sfinks.jpg', 'rb'))
            bot.send_message(chat_id, text="Университетская набережная, 17")
        elif vplace == "Особняк Брусницыных":
            bot.send_photo(chat_id, open('G:\pythonProject\img\osobnyak-brusnitsynykh.jpg', 'rb'))
            bot.send_message(chat_id, text="Кожевенная линия, 27")
        elif vplace == "Музей современного искусства Эрарта":
            bot.send_photo(chat_id, open('G:\pythonProject\img\erarta.jpg', 'rb'))
            bot.send_message(chat_id, text="29-я линия В.О., 2 \n"
                                           "Сайт: https://www.erarta.com/")
        elif vplace == "Памятник бомбардиру Василию":
            bot.send_photo(chat_id, open('G:\pythonProject\img\pamyatnik.jpg', 'rb'))
            bot.send_message(chat_id, text="7-я линия Васильевского острова, 6")
        elif vplace == "Стрелка Васильевского острова":
            bot.send_photo(chat_id, open('G:\pythonProject\img\strelka.jpg', 'rb'))
            bot.send_message(chat_id, text="Биржевая площадь")
        elif vplace == "Дворец Меншикова":
            bot.send_photo(chat_id, open('G:\pythonProject\img\menshikov.jpg', 'rb'))
            bot.send_message(chat_id, text="Университетская наб., 15")
        elif vplace == "Улица Репина":
            bot.send_photo(chat_id, open('G:\pythonProject\img\pepina.jpg', 'rb'))
        elif vplace == "Двор духов":
            bot.send_photo(chat_id, open('G:\pythonProject\img\dvorduxov.jpg', 'rb'))
            bot.send_message(chat_id, text="Большой просп. Васильевского острова, 15")
        elif vplace == "Севкабель Порт":
            bot.send_photo(chat_id, open('G:\pythonProject\img\port.jpg', 'rb'))
            bot.send_message(chat_id, text="Кожевенная линия, 40 \n"
                                           "Сайт: https://sevcableport.ru/ru")

    elif ms_text == "Адмиралтейский район":
        aplace1 = "Государственный Эрмитаж"
        aplace2 = "Исаакиевский собор"
        aplace3 = "Дворцовая площадь"
        aplace4 = "Сенатская площадь"
        aplace5 = "Остров Новая Голландия"
        aplace6 = "Особняк Румянцева"
        aplace7 = "Мраморный дворец (филиал Русского музея)"
        aplace8 = "Владимирский дворец"
        aplace9 = "Адмиралтейство"
        aplace = random.choice([aplace1, aplace2, aplace3, aplace4, aplace5, aplace6, aplace7, aplace8, aplace9])
        bot.send_message(chat_id, text="Можно посетить " + aplace)
        if aplace == "Государственный Эрмитаж":
            bot.send_photo(chat_id, open('G:\pythonProject\img\ermitag.jpg', 'rb'))
            bot.send_message(chat_id, text="Дворцовая набережная, 34 \n"
                                           "Сайт: http://collections.hermitage.ru/")
        elif aplace == "Исаакиевский собор":
            bot.send_photo(chat_id, open('G:\pythonProject\img\isaak.jpg', 'rb'))
            bot.send_message(chat_id, text="Исаакиевская площадь, 4 \n"
                                           "Сайт: https://cathedral.ru/ru")
        elif aplace == "Дворцовая площадь":
            bot.send_photo(chat_id, open('G:\pythonProject\img\dvordsovaya.jpg', 'rb'))
        elif aplace == "Остров Новая Голландия":
            bot.send_photo(chat_id, open('G:\pythonProject\img\gnovaya.jpg', 'rb'))
            bot.send_message(chat_id, text="наб. Адмиралтейского канала, 2 \n"
                                           "Сайт: https://www.newhollandsp.ru/")
        elif aplace == "Мраморный дворец (филиал Русского музея)":
            bot.send_photo(chat_id, open('G:\pythonProject\img\mramor.jpg', 'rb'))
            bot.send_message(chat_id, text="Миллионная ул., 5А \n"
                                           "Сайт: https://rusmuseum.ru/marble-palace/")
        elif aplace == "Владимирский дворец":
            bot.send_photo(chat_id, open('G:\pythonProject\img\du.jpg', 'rb'))
            bot.send_message(chat_id, text="Дворцовая наб., 26 \n"
                                           "Сайт: https://дом-ученых.рф/")
        elif aplace == "Особняк Румянцева":
            bot.send_photo(chat_id, open('G:\pythonProject\img\Румянцева.jpg', 'rb'))
            bot.send_message(chat_id, text="Английская набережная, 44")
        elif aplace == "Сенатская площадь":
            bot.send_photo(chat_id, open('G:\pythonProject\img\ploshad.jpg', 'rb'))
        elif aplace == "Адмиралтейство":
            bot.send_photo(chat_id, open('G:\pythonProject\img\dmir.jpg', 'rb'))
            bot.send_message(chat_id, text="Адмиралтейский пр., 1")

    elif ms_text == "Невский район":
        nplace1 = "Музей Фаберже"
        nplace2 = "Государственный Русский музей - Михайловский дворец"
        nplace3 = "Казанский кафедральный собор"
        nplace4 = "Российский этнографический музей"
        nplace5 = "Михайловский Замок"
        nplace6 = "Летний сад"
        nplace7 = "Строгановский дворец"
        nplace8 = "Арт-Центр в Перинных Рядах"
        nplace9 = "Граффити Виктор Цой"
        nplace10 = "Набережная канала Грибоедова"
        nplace = random.choice([nplace1, nplace2, nplace3, nplace4, nplace5, nplace6, nplace7, nplace8, nplace9, nplace10])
        bot.send_message(chat_id, text="Можно посетить " + nplace)
        if nplace == "Музей Фаберже":
            bot.send_photo(chat_id, open('G:\pythonProject\img\musfab.jpg', 'rb'))
            bot.send_message(chat_id, text="наб. реки Фонтанки, 21 \n"
                                           "Сайт: https://fabergemuseum.ru/")
        elif nplace == "Государственный Русский музей - Михайловский дворец":
            bot.send_photo(chat_id, open('G:\pythonProject\img\grm.jpg', 'rb'))
            bot.send_message(chat_id, text="Инженерная ул., 2-4А \n"
                                           "Сайт: https://rusmuseum.ru/mikhailovsky-palace/")
        elif nplace == "Казанский кафедральный собор":
            bot.send_photo(chat_id, open('G:\pythonProject\img\kks.jpg', 'rb'))
            bot.send_message(chat_id, text="Казанская площадь, 2 \n"
                                           "Сайт: http://kazansky-spb.ru/")
        elif nplace == "Российский этнографический музей":
            bot.send_photo(chat_id, open('G:\pythonProject\img\etnogr.jpg', 'rb'))
            bot.send_message(chat_id, text="ул. Инженерная, д.4/1 \n"
                                           "Сайт: https://ethnomuseum.ru/")
        elif nplace == "Михайловский Замок":
            bot.send_photo(chat_id, open('G:\pythonProject\img\michail.jpg', 'rb'))
            bot.send_message(chat_id, text="Садовая ул., 2 \n"
                                           "Сайт: https://rusmuseum.ru/mikhailovsky-castle/")
        elif nplace == "Летний сад":
            bot.send_photo(chat_id, open('G:\pythonProject\img\letniy.jpg', 'rb'))
            bot.send_message(chat_id, text="набережная Кутузова, 2 \n"
                                           "Сайт: https://rusmuseum.ru/summer-garden/history/")
        elif nplace == "Строгановский дворец":
            bot.send_photo(chat_id, open('G:\pythonProject\img\stroganovsky.jpg', 'rb'))
            bot.send_message(chat_id, text="Невский просп., 17 \n"
                                           "Сайт: https://rusmuseum.ru/stroganov-palace/")
        elif nplace == "Арт-Центр в Перинных Рядах":
            bot.send_photo(chat_id, open('G:\pythonProject\img\centr.jpg', 'rb'))
            bot.send_message(chat_id, text="Думская ул., 4")
        elif nplace == "Граффити Виктор Цой":
            bot.send_photo(chat_id, open('G:\pythonProject\img\graffity.jpg', 'rb'))
            bot.send_message(chat_id, text="ул. Восстания, 8Г")
        elif nplace == "Набережная канала Грибоедова":
            bot.send_photo(chat_id, open('G:\pythonProject\img\kanalgr.jpg', 'rb'))

    elif ms_text == "Московский район":
        mplace1 = "Московские Триумфальные ворота"
        mplace2 = "Пулковская обсерватория"
        mplace3 = "Музей «Гранд Макет Россия»"
        mplace4 = "Площадь Победы"
        mplace5 = "Московской парк Победы"
        mplace6 = "Воскресенский Новодевичий Монастырь"
        mplace7 = "Пулковский парк"
        mplace = random.choice([mplace1, mplace2, mplace3, mplace4, mplace5, mplace6, mplace7])
        bot.send_message(chat_id, text="Можно посетить " + mplace)
        if mplace == "Московские Триумфальные ворота":
            bot.send_photo(chat_id, open('G:\pythonProject\img\mta.jpg', 'rb'))
            bot.send_message(chat_id, text="Площадь Московские Ворота")
        elif mplace == "Пулковская обсерватория":
            bot.send_photo(chat_id, open('G:\pythonProject\img\pulkovskaya.jpg', 'rb'))
            bot.send_message(chat_id, text="Пулковское ш., 65 \n"
                                           "Сайт: http://www.gaoran.ru/")
        elif mplace == "Музей «Гранд Макет Россия»":
            bot.send_photo(chat_id, open('G:\pythonProject\img\grandmaket.jpg', 'rb'))
            bot.send_message(chat_id, text="Цветочная улица, 16Л \n"
                                           "Сайт: https://grandmaket.ru/")
        elif mplace == "Московский парк Победы":
            bot.send_photo(chat_id, open('G:\pythonProject\img\parkpobedi.jpg', 'rb'))
            bot.send_message(chat_id, text="Кузнецовская улица, 25")
        elif mplace == "Пулковский парк":
            bot.send_photo(chat_id, open('G:\pythonProject\img\pulkovpark.jpg', 'rb'))
            bot.send_message(chat_id, text="Московское ш.")
        elif mplace == "Воскресенский Новодевичий Монастырь":
            bot.send_photo(chat_id, open('G:\pythonProject\img\mon.jpg', 'rb'))
            bot.send_message(chat_id, text="Московский просп., 100 \n"
                                           "Сайт: https://вноводевичий.рф/")
        elif mplace == "Площадь Победы":
            bot.send_photo(chat_id, open('G:\pythonProject\img\ploschadpobedy.jpg', 'rb'))

    elif ms_text == "Петроградский район":
        pplace1 = "Петропавловская крепость"
        pplace2 = "Елагин остров"
        pplace3 = "Парк аттракционов Диво Остров"
        pplace4 = "Ботанический сад Петра Великого"
        pplace5 = "Домик Петра I"
        pplace6 = "Александровский Парк"
        pplace7 = "Приморский парк Победы"
        pplace8 = "Петровская набережная"
        pplace9 = "Лопухинский сад"
        pplace10 = "Каменностровский проспект"
        pplace = random.choice([pplace1, pplace2, pplace3, pplace4, pplace5, pplace6, pplace7, pplace8, pplace9, pplace10])
        bot.send_message(chat_id, text="Можно посетить " + pplace)
        if pplace == "Петропавловская крепость":
            bot.send_photo(chat_id, open('G:\pythonProject\img\petropavlovskaya-krepost.jpg', 'rb'))
            bot.send_message(chat_id, text="Сайт: https://petropavlovskaya.org/")
        elif pplace == "Елагин остров":
            bot.send_photo(chat_id, open('G:\pythonProject\img\elagin.jpg', 'rb'))
            bot.send_message(chat_id, text="Сайт: https://elaginpark.org/")
        elif pplace == "Парк аттракционов Диво Остров":
            bot.send_photo(chat_id, open('G:\pythonProject\img\divoostr.jpg', 'rb'))
            bot.send_message(chat_id, text="Сайт: https://www.divo-ostrov.ru/")
        elif pplace == "Ботанический сад Петра Великого":
            bot.send_photo(chat_id, open('G:\pythonProject\img\sadbot.jpg', 'rb'))
            bot.send_message(chat_id, text="ул. Профессора Попова, 2П \n"
                                           "Сайт: https://botsad-spb.com/")
        elif pplace == "Домик Петра I":
            bot.send_photo(chat_id, open('G:\pythonProject\img\domik.jpg', 'rb'))
            bot.send_message(chat_id, text="Петровская наб., 6 \n"
                                           "Сайт: https://rusmuseum.ru/cabin-of-peter-1/")
        elif pplace == "Александровский Парк":
            bot.send_photo(chat_id, open('G:\pythonProject\img\parkalex.jpg', 'rb'))
            bot.send_message(chat_id, text="Кронверкский проспект")
        elif pplace == "Приморский парк Победы":
            bot.send_photo(chat_id, open('G:\pythonProject\img\primpark.jpg', 'rb'))
            bot.send_message(chat_id, text="Крестовский просп., 23 \n"
                                           "Сайт: http://pppark.ru/")
        elif pplace == "Петровская набережная":
            bot.send_photo(chat_id, open('G:\pythonProject\img\petrnab.jpg', 'rb'))
        elif pplace == "Лопухинский сад":
            bot.send_photo(chat_id, open('G:\pythonProject\img\parlop.jpg', 'rb'))
            bot.send_message(chat_id, text="улица Академика Павлова")
        elif pplace == "Каменностровский проспект":
            bot.send_photo(chat_id, open('G:\pythonProject\img\kamen.jpg', 'rb'))

    elif ms_text == "Кафе/рестораны":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Василеостровский р-н")
        btn2 = types.KeyboardButton("Адмиралтейский р-н")
        btn3 = types.KeyboardButton("Московский р-н")
        btn4 = types.KeyboardButton("Невский р-н")
        btn5 = types.KeyboardButton("Петроградский р-н")
        btn6 = types.KeyboardButton("Вернуться в главное меню")
        back = types.KeyboardButton("Помощь")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, back)
        bot.send_message(chat_id, text="Кафе/рестораны", reply_markup=markup)

    elif ms_text == "Василеостровский р-н":
        bot.send_message(chat_id, text="1)Брюгге(Бельгийская кухня, Бар) - Набережная Макарова, 22\n\n"
                                       "2)Мука(Итальянская кухня, Кафе) - ул. Гаванская, 35\n\n"
                                       "3)Маркетплейс(Европейская кухня) - 7-я линия 34\n\n"
                                       "4)ФермА Кафе(Европейская кухня) - 6-ая линия Васильевского острова, д. 13\n\n"
                                       "5)Пельмения на Среднем(Азиатская кухня, Русская кухня) - Средний пр. В.О., 11")

    elif ms_text == "Адмиралтейский р-н":
        bot.send_message(chat_id, text="1)Кофе Бар Бонч(Кафе) - ул. Большая Морская, 16\n\n"
                                       "2)Italy(Итальянская кухня) - ул. Большая Морская, д. 14\n\n"
                                       "3)Буше(Быстрые перекусы, Европейская кухня) - ул. Малая Морская, 7\n\n"
                                       "4)Литературное кафе(Русская кухня) - Невский проспект, д. 18\n\n"
                                       "5)Омманэ(Корейская кухня) - ул. Гороховая, 3")

    elif ms_text == "Московский р-н":
        bot.send_message(chat_id, text="1)Евразия(Вегетарианская кухня, Европейская кухня) - Московский проспект, 195\n\n"
                                       "2)Мамамиа(Итальянская кухня) - Варшавская, 6\n\n"
                                       "3)Кореана(Азиатская кухня) - Варшавская, 23\n\n"
                                       "4)Bona Capona(Итальянская кухня, Европейская кухня, Русская кухня) - Московский проспект, 179\n\n"
                                       "5)Mama Roma(Итальянская кухня) - Московский проспект, 192")

    elif ms_text == "Невский р-н":
        bot.send_message(chat_id, text="1)FULL HOUSE Grill-Bar(Европейская кухня, бар) - Наб. Канала Грибоедова, 27\n\n"
                                       "2)Зум кафе(Европейская кухня, кафе) - Гороховая ул., д. 22\n\n"
                                       "3)Сулико(Грузинская кухня, Кавказская кухня) - ул. Восстания, 7\n\n"
                                       "4)Amo cucinare(Итальянская кухня, Средиземноморская кухня) - ул. Большая Конюшенная 5\n\n"
                                       "5)Вайн Гог(Европейская кухня, винный бар) - Малая Конюшенная, 7")

    elif ms_text == "Петроградский р-н":
        bot.send_message(chat_id, text="1)Капулетти(Итальянская кухня) -Большой проспект П.С., д. 74\n\n"
                                       "2)Пельмения на Кронверкском(Азиатская кухня, Русская кухня, Европейская кухня) - Кронверкский проспект, д. 55\n\n"
                                       "3)Такояки-Мисэ(Быстрые перекусы, Японская кухня) - ул. Лизы Чайкиной, 19Б\n\n"
                                       "4)Ketch Up Burgers(Американская кухня) - Ул. Льва Толстого, 1/3\n\n"
                                       "5)Маннекен Пис(Бельгийская кухня, Европейская кухня) - Каменноостровский проспект, 12")

    elif ms_text == "Помощь" or ms_text == "/help":
        bot.send_message(chat_id, "Автор: Саша Копина")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(chat_id, text="Напишите автору: https://t.me/kopinaS", reply_markup=markup)

    else:
        bot.send_message(chat_id, text="Я тебя слышу!!! Ваше сообщение: " + ms_text)

# -----------------------------------------------------------------------
bot.polling(none_stop=True, interval=0)

print()
