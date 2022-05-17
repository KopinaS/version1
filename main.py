import telebot
from menu import Menu
from telebot import types
import random
import SECRET

bot = telebot.TeleBot(SECRET.TELEGRAM_TOKEN)

@bot.message_handler(commands="start")
def command(message, res=False):
    txt_message = f"Привет, {message.from_user.first_name}! Я тестовый бот для курса программирования на языке Python"
    bot.send_message(message.chat.id, text=txt_message, reply_markup=Menu.getMenu("Главное меню").markup)
# -----------------------------------------------------------------------
def send_help(chat_id):
    bot.send_message(chat_id, "Автор: Копина Александра\n"
                              "Напишите автору: https://t.me/kopinaS")

@bot.message_handler(func=lambda message: True)
def get_text_message(message):
    chat_id = message.chat.id
    ms_text = message.text

    if Menu.cur_menu != None and ms_text in Menu.cur_menu.buttons:
        if ms_text == "Помощь":
            send_help(chat_id)
        elif ms_text in ["Прогулки", "Кафе/рестораны"]:
            goto_menu(chat_id, ms_text)
        elif ms_text == "Игра":
            goto_menu(chat_id, ms_text)
        elif ms_text == "Выход":
            goto_menu(chat_id, ms_text)

    if ms_text == "Василеостровский район":
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
        vplace = random.choice(
            [vplace1, vplace2, vplace3, vplace4, vplace5, vplace6, vplace7, vplace8, vplace9, vplace10])
        bot.send_message(chat_id, text="Можно посетить " + vplace)
        if vplace == "Сад Академии художеств":
            bot.send_photo(chat_id,
                           'https://avatars.mds.yandex.net/get-altay/2006773/2a0000016dc8b80b8f2435e6f4aadb04e798/XXL')
            bot.send_message(chat_id, text="Университетская наб., 17, находится между 3 и 4 линиями ВО")
        elif vplace == "Египетские сфинксы на берегу Невы":
            bot.send_photo(chat_id, 'https://pp.vk.me/c627417/v627417863/2d6c6/1JUJnG0knaA.jpg')
            bot.send_message(chat_id, text="Университетская набережная, 17")
        elif vplace == "Особняк Брусницыных":
            bot.send_photo(chat_id,
                           'https://topdialog.ru/wp-content/uploads/2019/04/tijgxpam1cw-e1556280752852.jpg')
            bot.send_message(chat_id, text="Кожевенная линия, 27")
        elif vplace == "Музей современного искусства Эрарта":
            bot.send_photo(chat_id, 'https://fortuna-travel.ru/images/erarta-600-1.jpg')
            bot.send_message(chat_id, text="29-я линия В.О., 2 \n"
                                           "Сайт: https://www.erarta.com/")
        elif vplace == "Памятник бомбардиру Василию":
            bot.send_photo(chat_id,
                           'https://petersmonuments.ru/upload/iblock/e6b/e6bd118ce3fa0159d56722c25548fb97.jpg')
            bot.send_message(chat_id, text="7-я линия Васильевского острова, 6")
        elif vplace == "Стрелка Васильевского острова":
            bot.send_photo(chat_id,
                           'https://images.spasibovsem.ru/catalog/original/strelka-vasilevskogo-ostrova-sankt-peterburg-rossiya-otzyvy-1578937511.jpg')
            bot.send_message(chat_id, text="Биржевая площадь")
        elif vplace == "Дворец Меншикова":
            bot.send_photo(chat_id, 'https://www.spbmuzei.ru/wp-content/uploads/2019/12/menshik2-1140x588.jpg')
            bot.send_message(chat_id, text="Университетская наб., 15")
        elif vplace == "Улица Репина":
            bot.send_photo(chat_id, 'https://kayakspb.ru/wp-content/uploads/2016/11/repina_1.jpg')
        elif vplace == "Двор духов":
            bot.send_photo(chat_id, 'https://petersburg24.ru/files/attachment_images/973_image.jpg?1531052667')
            bot.send_message(chat_id, text="Большой просп. Васильевского острова, 15")
        elif vplace == "Севкабель Порт":
            bot.send_photo(chat_id,
                           'https://avatars.mds.yandex.net/get-altay/1545421/2a0000016eeeabe47a56138eeca259321201/XXL')
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
            bot.send_photo(chat_id,
                           'https://n1s1.hsmedia.ru/8b/d9/40/8bd940ad98b075dadf3d57d523bce512/1000x667_0xac120003_15881333861615822925.jpg')
            bot.send_message(chat_id, text="Дворцовая набережная, 34 \n"
                                           "Сайт: http://collections.hermitage.ru/")
        elif aplace == "Исаакиевский собор":
            bot.send_photo(chat_id, 'https://photocentra.ru/images/main77/770044_main.jpg')
            bot.send_message(chat_id, text="Исаакиевская площадь, 4 \n"
                                           "Сайт: https://cathedral.ru/ru")
        elif aplace == "Дворцовая площадь":
            bot.send_photo(chat_id,
                           'https://avatars.mds.yandex.net/get-zen_doc/1861837/pub_5df61efd8f011100ad77a72f_5df66ddf1e8e3f00acffb804/scale_1200')
        elif aplace == "Остров Новая Голландия":
            bot.send_photo(chat_id, 'https://cs12.pikabu.ru/post_img/big/2020/07/13/9/1594652562126321417.jpg')
            bot.send_message(chat_id, text="наб. Адмиралтейского канала, 2 \n"
                                           "Сайт: https://www.newhollandsp.ru/")
        elif aplace == "Мраморный дворец (филиал Русского музея)":
            bot.send_photo(chat_id,
                           'https://peterburg.center/sites/default/files/9._st._petersburg._marble_palace.jpg')
            bot.send_message(chat_id, text="Миллионная ул., 5А \n"
                                           "Сайт: https://rusmuseum.ru/marble-palace/")
        elif aplace == "Владимирский дворец":
            bot.send_photo(chat_id,
                           'https://sun6-23.userapi.com/impg/kiv0cita3Yhxit__OjtjhBD7zf8wReX0No12ew/zqwFzbs5CP4.jpg?size=697x582&quality=96&sign=ed24e08de8ce802047492ce182056ba3&c_uniq_tag=jNSJCSMugm3ZxqFenfkoNRDwPaARGbowdivSuBiq2GI&type=album')
            bot.send_message(chat_id, text="Дворцовая наб., 26 \n"
                                           "Сайт: https://дом-ученых.рф/")
        elif aplace == "Особняк Румянцева":
            bot.send_photo(chat_id, 'https://ksanytch.ru/Piter/OsobnyakRumyantseva.jpg')
            bot.send_message(chat_id, text="Английская набережная, 44")
        elif aplace == "Сенатская площадь":
            bot.send_photo(chat_id, 'https://60wt.ru/upload/iblock/6a9/6a9127c167679bc5cbcd5c89d8af34f2.jpeg')
        elif aplace == "Адмиралтейство":
            bot.send_photo(chat_id, 'https://i02.fotocdn.net/s112/b1274b99ea2162de/public_pin_l/2522608915.jpg')
            bot.send_message(chat_id, text="Адмиралтейский пр., 1")
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
            bot.send_photo(chat_id,
                           'https://rogaine-spb.ru/wp-content/uploads/2019/02/2258695da86e048dce7bd8c62d157175.jpg')
            bot.send_message(chat_id, text="Площадь Московские Ворота")
        elif mplace == "Пулковская обсерватория":
            bot.send_photo(chat_id, 'https://poisknews.ru/wp-content/uploads/2019/05/shutterstock_1098116876.jpg')
            bot.send_message(chat_id, text="Пулковское ш., 65 \n"
                                           "Сайт: http://www.gaoran.ru/")
        elif mplace == "Музей «Гранд Макет Россия»":
            bot.send_photo(chat_id,
                           'https://kikimoraki.ru/wp-content/uploads/2020/08/sovremennye-muzei-v-sankt-peterburge-chto-posetit-i-posmotret-1.jpg')
            bot.send_message(chat_id, text="Цветочная улица, 16Л \n"
                                           "Сайт: https://grandmaket.ru/")
        elif mplace == "Московский парк Победы":
            bot.send_photo(chat_id, 'https://i05.fotocdn.net/s108/5e6d346af19e01fc/public_pin_l/2383686541.jpg')
            bot.send_message(chat_id, text="Кузнецовская улица, 25")
        elif mplace == "Пулковский парк":
            bot.send_photo(chat_id,
                           'https://i.travelapi.com/hotels/15000000/14820000/14815600/14815516/9410461b_z.jpg')
            bot.send_message(chat_id, text="Московское ш.")
        elif mplace == "Воскресенский Новодевичий Монастырь":
            bot.send_photo(chat_id,
                           'https://upload.wikimedia.org/wikipedia/commons/7/7e/5238._St._Petersburg._Resurrection_Cathedral.jpg')
            bot.send_message(chat_id, text="Московский просп., 100 \n"
                                           "Сайт: https://вноводевичий.рф/")
        elif mplace == "Площадь Победы":
            bot.send_photo(chat_id,
                           'https://sdelanounas.ru/i/d/3/d/f_d3d3LmxlbnN2ZXQuc3BiLnJ1L2QvMjY5MDkvZC9wbG9zY2hhZC1wb2JlZHkuanBnP19faWQ9MTM2NDgw.jpeg')
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
        nplace = random.choice(
            [nplace1, nplace2, nplace3, nplace4, nplace5, nplace6, nplace7, nplace8, nplace9, nplace10])
        bot.send_message(chat_id, text="Можно посетить " + nplace)
        if nplace == "Музей Фаберже":
            bot.send_photo(chat_id, 'https://static.tildacdn.com/tild3939-6337-4535-b538-656434316461/faberge1.jpg')
            bot.send_message(chat_id, text="наб. реки Фонтанки, 21 \n"
                                           "Сайт: https://fabergemuseum.ru/")
        elif nplace == "Государственный Русский музей - Михайловский дворец":
            bot.send_photo(chat_id, 'https://www.in4s.net/wp-content/uploads/2020/04/Ruski-muzej.jpg')
            bot.send_message(chat_id, text="Инженерная ул., 2-4А \n"
                                           "Сайт: https://rusmuseum.ru/mikhailovsky-palace/")
        elif nplace == "Казанский кафедральный собор":
            bot.send_photo(chat_id, 'https://traveltimes.ru/wp-content/uploads/2021/08/2734040772.jpg')
            bot.send_message(chat_id, text="Казанская площадь, 2 \n"
                                           "Сайт: http://kazansky-spb.ru/")
        elif nplace == "Российский этнографический музей":
            bot.send_photo(chat_id,
                           'https://sun9-38.userapi.com/impg/bZsnLjj5V9jL9qIjie59W88PdR0X4qvM2pNVbg/czpuVVOQDok.jpg?size=807x538&quality=96&sign=089b8281a0b0dd98e0542932e783aba5&c_uniq_tag=Mhb6xxrSU5JljiTViefoMZb6EUsJ9d149iPbcnfXix4&type=album')
            bot.send_message(chat_id, text="ул. Инженерная, д.4/1 \n"
                                           "Сайт: https://ethnomuseum.ru/")
        elif nplace == "Михайловский Замок":
            bot.send_photo(chat_id, 'https://puzzleit.ru/files/puzzles/207/207272/_original.jpg')
            bot.send_message(chat_id, text="Садовая ул., 2 \n"
                                           "Сайт: https://rusmuseum.ru/mikhailovsky-castle/")
        elif nplace == "Летний сад":
            bot.send_photo(chat_id, 'https://farm2.staticflickr.com/1819/44225802111_71ab67c29e_h.jpg')
            bot.send_message(chat_id, text="набережная Кутузова, 2 \n"
                                           "Сайт: https://rusmuseum.ru/summer-garden/history/")
        elif nplace == "Строгановский дворец":
            bot.send_photo(chat_id, 'https://aif-turkey.ru/800/600/http/s1.fotokto.ru/photo/full/444/4449040.jpg')
            bot.send_message(chat_id, text="Невский просп., 17 \n"
                                           "Сайт: https://rusmuseum.ru/stroganov-palace/")
        elif nplace == "Арт-Центр в Перинных Рядах":
            bot.send_photo(chat_id, 'https://perin-spb.ru/images/1.jpg')
            bot.send_message(chat_id, text="Думская ул., 4")
        elif nplace == "Граффити Виктор Цой":
            bot.send_photo(chat_id, 'https://ic.pics.livejournal.com/classiks/23976823/512704/512704_original.jpg')
            bot.send_message(chat_id, text="ул. Восстания, 8Г")
        elif nplace == "Набережная канала Грибоедова":
            bot.send_photo(chat_id, 'https://weatlas.com/img/landmarks/8dcee87215dcc73d6e3d3a70c1a623b6.jpg')
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
        pplace = random.choice(
            [pplace1, pplace2, pplace3, pplace4, pplace5, pplace6, pplace7, pplace8, pplace9, pplace10])
        bot.send_message(chat_id, text="Можно посетить " + pplace)
        if pplace == "Петропавловская крепость":
            bot.send_photo(chat_id, 'https://np-travel.spb.ru/assets/gallery/68/405.jpg')
            bot.send_message(chat_id, text="Сайт: https://petropavlovskaya.org/")
        elif pplace == "Елагин остров":
            bot.send_photo(chat_id, 'https://i12.fotocdn.net/s105/7e73991d70a1cc11/public_pin_l/2242418389.jpg')
            bot.send_message(chat_id, text="Сайт: https://elaginpark.org/")
        elif pplace == "Парк аттракционов Диво Остров":
            bot.send_photo(chat_id,
                           'https://forpost-sz.ru/sites/default/files/doc/2020/08/09/116906703_718768992297190_4461788238576538092_n.jpg')
            bot.send_message(chat_id, text="Сайт: https://www.divo-ostrov.ru/")
        elif pplace == "Ботанический сад Петра Великого":
            bot.send_photo(chat_id,
                           'https://cdn.spbdnevnik.ru/uploads/block/image/454986/__medium_selN-rfU_yg.jpg.jpg')
            bot.send_message(chat_id, text="ул. Профессора Попова, 2П \n"
                                           "Сайт: https://botsad-spb.com/")
        elif pplace == "Домик Петра I":
            bot.send_photo(chat_id,
                           'https://peterburg-blog.ru/wp-content/uploads/2017/01/домик-петра-первого-в-петербурге.jpg')
            bot.send_message(chat_id, text="Петровская наб., 6 \n"
                                           "Сайт: https://rusmuseum.ru/cabin-of-peter-1/")
        elif pplace == "Александровский Парк":
            bot.send_photo(chat_id, 'https://cat-cat-cat.ru/photo/2015/01/MG_5398-2-.jpg')
            bot.send_message(chat_id, text="Кронверкский проспект")
        elif pplace == "Приморский парк Победы":
            bot.send_photo(chat_id, 'https://www.visit-petersburg.ru/upload/iblock/429/00kwgh5t7ake3i8pg89jppgrb09am35z/1696_cover.jpg')
            bot.send_message(chat_id, text="Крестовский просп., 23 \n"
                                           "Сайт: http://pppark.ru/")
        elif pplace == "Петровская набережная":
            bot.send_photo(chat_id,
                           'https://korona-severa.ru/wp-content/uploads/c/5/b/c5ba1c822cac2a2a851b8432c2838ece.jpeg')
        elif pplace == "Лопухинский сад":
            bot.send_photo(chat_id, 'https://sun9-40.userapi.com/bWQbmy9CcjGfSQ3o_4tKlhJiD5W_jLqaVwC1og/54IESpfAAcw.jpg')
            bot.send_message(chat_id, text="улица Академика Павлова")
        elif pplace == "Каменностровский проспект":
            bot.send_photo(chat_id, 'https://s00.yaplakal.com/pics/pics_original/6/6/1/10239166.jpg')


    elif ms_text == "Василеостровский р-н":
        bot.send_message(chat_id, text="🧇*Брюгге*(Бельгийская кухня, Бар) - Набережная Макарова, 22\n\n"
                                       "🍝*Мука*(Итальянская кухня, Кафе) - ул. Гаванская, 35\n\n"
                                       "🥐*Маркетплейс*(Европейская кухня) - 7-я линия 34\n\n"
                                       "🥐*ФермА Кафе*(Европейская кухня) - 6-ая линия Васильевского острова, д. 13\n\n"
                                       "🍱*Пельмения на Среднем*(Азиатская кухня, Русская кухня) - Средний пр. В.О., 11",
                         parse_mode="Markdown")
    elif ms_text == "Адмиралтейский р-н":
        bot.send_message(chat_id, text="☕*Кофе Бар Бонч*(Кафе) - ул. Большая Морская, 16\n\n"
                                       "🍝*Italy*(Итальянская кухня) - ул. Большая Морская, д. 14\n\n"
                                       "🥐*Буше*(Быстрые перекусы, Европейская кухня) - ул. Малая Морская, 7\n\n"
                                       "🥞*Литературное кафе*(Русская кухня) - Невский проспект, д. 18\n\n"
                                       "🍜*Омманэ*(Корейская кухня) - ул. Гороховая, 3", parse_mode="Markdown")
    elif ms_text == "Московский р-н":
        bot.send_message(chat_id,
                         text="🥐*Евразия*(Вегетарианская кухня, Европейская кухня) - Московский проспект, 195\n\n"
                              "🍝*Мамамиа*(Итальянская кухня) - Варшавская, 6\n\n"
                              "🍱*Кореана*(Азиатская кухня) - Варшавская, 23\n\n"
                              "🍝*Bona Capona*(Итальянская кухня, Европейская кухня, Русская кухня) - Московский проспект, 179\n\n"
                              "🍝*Mama Roma*(Итальянская кухня) - Московский проспект, 192", parse_mode="Markdown")
    elif ms_text == "Невский р-н":
        bot.send_message(chat_id,
                         text="🥐*FULL HOUSE Grill-Bar*(Европейская кухня, бар) - Наб. Канала Грибоедова, 27\n\n"
                              "🥐*Зум кафе*(Европейская кухня, кафе) - Гороховая ул., д. 22\n\n"
                              "🍗*Сулико*(Грузинская кухня, Кавказская кухня) - ул. Восстания, 7\n\n"
                              "🍝*Amo cucinare*(Итальянская кухня, Средиземноморская кухня) - ул. Большая Конюшенная 5\n\n"
                              "🥐*Вайн Гог*(Европейская кухня, винный бар) - Малая Конюшенная, 7",
                         parse_mode="Markdown")
    elif ms_text == "Петроградский р-н":
        bot.send_message(chat_id, text="🍝*Капулетти*(Итальянская кухня) -Большой проспект П.С., д. 74\n\n"
                                       "🥟*Пельмения на Кронверкском*(Азиатская кухня, Русская кухня, Европейская кухня) - Кронверкский проспект, д. 55\n\n"
                                       "🍱*Такояки-Мисэ*(Быстрые перекусы, Японская кухня) - ул. Лизы Чайкиной, 19Б\n\n"
                                       "🍔*Ketch Up Burgers*(Американская кухня) - Ул. Льва Толстого, 1/3\n\n"
                                       "🧇*Маннекен Пис*(Бельгийская кухня, Европейская кухня) - Каменноостровский проспект, 12",
                         parse_mode="Markdown")

    elif ms_text == "Картина":
        place = random.choice(["https://avatars.mds.yandex.net/get-altay/2006773/2a0000016dc8b80b8f2435e6f4aadb04e798/XXL", "https://kayakspb.ru/wp-content/uploads/2016/11/repina_1.jpg", "https://pp.vk.me/c627417/v627417863/2d6c6/1JUJnG0knaA.jpg",
                 "https://topdialog.ru/wp-content/uploads/2019/04/tijgxpam1cw-e1556280752852.jpg", "https://fortuna-travel.ru/images/erarta-600-1.jpg", "https://petersmonuments.ru/upload/iblock/e6b/e6bd118ce3fa0159d56722c25548fb97.jpg",
                 "https://images.spasibovsem.ru/catalog/original/strelka-vasilevskogo-ostrova-sankt-peterburg-rossiya-otzyvy-1578937511.jpg", "https://www.spbmuzei.ru/wp-content/uploads/2019/12/menshik2-1140x588.jpg",
                 "https://petersburg24.ru/files/attachment_images/973_image.jpg?1531052667", "https://avatars.mds.yandex.net/get-altay/1545421/2a0000016eeeabe47a56138eeca259321201/XXL", "https://n1s1.hsmedia.ru/8b/d9/40/8bd940ad98b075dadf3d57d523bce512/1000x667_0xac120003_15881333861615822925.jpg",
                 "https://photocentra.ru/images/main77/770044_main.jpg", "https://avatars.mds.yandex.net/get-zen_doc/1861837/pub_5df61efd8f011100ad77a72f_5df66ddf1e8e3f00acffb804/scale_1200", "https://60wt.ru/upload/iblock/6a9/6a9127c167679bc5cbcd5c89d8af34f2.jpeg",
                 "https://cs12.pikabu.ru/post_img/big/2020/07/13/9/1594652562126321417.jpg", "https://ksanytch.ru/Piter/OsobnyakRumyantseva.jpg", "https://peterburg.center/sites/default/files/9._st._petersburg._marble_palace.jpg",
                 "https://sun6-23.userapi.com/impg/kiv0cita3Yhxit__OjtjhBD7zf8wReX0No12ew/zqwFzbs5CP4.jpg?size=697x582&quality=96&sign=ed24e08de8ce802047492ce182056ba3&c_uniq_tag=jNSJCSMugm3ZxqFenfkoNRDwPaARGbowdivSuBiq2GI&type=album",
                 "https://i02.fotocdn.net/s112/b1274b99ea2162de/public_pin_l/2522608915.jpg", "https://rogaine-spb.ru/wp-content/uploads/2019/02/2258695da86e048dce7bd8c62d157175.jpg", "https://poisknews.ru/wp-content/uploads/2019/05/shutterstock_1098116876.jpg",
                 "https://kikimoraki.ru/wp-content/uploads/2020/08/sovremennye-muzei-v-sankt-peterburge-chto-posetit-i-posmotret-1.jpg", "https://sdelanounas.ru/i/d/3/d/f_d3d3LmxlbnN2ZXQuc3BiLnJ1L2QvMjY5MDkvZC9wbG9zY2hhZC1wb2JlZHkuanBnP19faWQ9MTM2NDgw.jpeg",
                 "https://i05.fotocdn.net/s108/5e6d346af19e01fc/public_pin_l/2383686541.jpg", "https://upload.wikimedia.org/wikipedia/commons/7/7e/5238._St._Petersburg._Resurrection_Cathedral.jpg", "https://i.travelapi.com/hotels/15000000/14820000/14815600/14815516/9410461b_z.jpg",
                 "https://static.tildacdn.com/tild3939-6337-4535-b538-656434316461/faberge1.jpg", "https://www.in4s.net/wp-content/uploads/2020/04/Ruski-muzej.jpg", "https://traveltimes.ru/wp-content/uploads/2021/08/2734040772.jpg",
                 "https://sun9-38.userapi.com/impg/bZsnLjj5V9jL9qIjie59W88PdR0X4qvM2pNVbg/czpuVVOQDok.jpg?size=807x538&quality=96&sign=089b8281a0b0dd98e0542932e783aba5&c_uniq_tag=Mhb6xxrSU5JljiTViefoMZb6EUsJ9d149iPbcnfXix4&type=album",
                 "https://puzzleit.ru/files/puzzles/207/207272/_original.jpg", "https://farm2.staticflickr.com/1819/44225802111_71ab67c29e_h.jpg", "https://aif-turkey.ru/800/600/http/s1.fotokto.ru/photo/full/444/4449040.jpg",
                 "https://perin-spb.ru/images/1.jpg", "https://ic.pics.livejournal.com/classiks/23976823/512704/512704_original.jpg", "https://weatlas.com/img/landmarks/8dcee87215dcc73d6e3d3a70c1a623b6.jpg",
                 "https://np-travel.spb.ru/assets/gallery/68/405.jpg", "https://i12.fotocdn.net/s105/7e73991d70a1cc11/public_pin_l/2242418389.jpg", "https://forpost-sz.ru/sites/default/files/doc/2020/08/09/116906703_718768992297190_4461788238576538092_n.jpg",
                 "https://cdn.spbdnevnik.ru/uploads/block/image/454986/__medium_selN-rfU_yg.jpg.jpg", "https://peterburg-blog.ru/wp-content/uploads/2017/01/домик-петра-первого-в-петербурге.jpg", "https://cat-cat-cat.ru/photo/2015/01/MG_5398-2-.jpg",
                 "https://www.visit-petersburg.ru/upload/iblock/429/00kwgh5t7ake3i8pg89jppgrb09am35z/1696_cover.jpg", "https://korona-severa.ru/wp-content/uploads/c/5/b/c5ba1c822cac2a2a851b8432c2838ece.jpeg",
                 "https://sun9-40.userapi.com/bWQbmy9CcjGfSQ3o_4tKlhJiD5W_jLqaVwC1og/54IESpfAAcw.jpg", "https://s00.yaplakal.com/pics/pics_original/6/6/1/10239166.jpg"])
        bot.send_message(chat_id, text="Что это за место? \n" + place)
        if place == "https://avatars.mds.yandex.net/get-altay/2006773/2a0000016dc8b80b8f2435e6f4aadb04e798/XXL":
            if ms_text == "Сад Академии художеств" or ms_text == "Сад художеств" or ms_text == "сад академии художеств" or ms_text == "сад художеств":
                bot.send_message(chat_id, text="Правильно!")
            else:
                bot.send_message(chat_id, text="Не угадали( \n Это Сад Академии художеств")
        if place == "https://pp.vk.me/c627417/v627417863/2d6c6/1JUJnG0knaA.jpg":
            if ms_text == "Египетские сфинксы" or ms_text == "египетские сфинксы" or ms_text == "сфинксы":
                bot.send_message(chat_id, text="Правильно!")
            else:
                bot.send_message(chat_id, text="Не угадали( \n Это Египетские сфинксы")
        if place == "https://topdialog.ru/wp-content/uploads/2019/04/tijgxpam1cw-e1556280752852.jpg":
            if ms_text == "Особняк Брусницыных" or ms_text == "особняк брусницыных" or ms_text == "особняк Брусницыных":
                bot.send_message(chat_id, text="Правильно!")
            else:
                bot.send_message(chat_id, text="Не угадали( \n Это Особняк Брусницыных")
        if place == "https://fortuna-travel.ru/images/erarta-600-1.jpg":
            if ms_text == "Музей Эрарта" or ms_text == "музей эрарта" or ms_text == "музей Эрарта" or ms_text == "эрарта" or ms_text == "Эрарта":
                bot.send_message(chat_id, text="Правильно!")
            else:
                bot.send_message(chat_id, text="Не угадали( \n Это Музей современного искусства Эрарта")
        if place == "https://petersmonuments.ru/upload/iblock/e6b/e6bd118ce3fa0159d56722c25548fb97.jpg":
            if ms_text == "Памятник бомбардиру Василию" or ms_text == "памятник бомбардиру василию" or ms_text == "памятник бомбардиру Василию" or ms_text == "памятник Василию" or ms_text == "памятник василию" or ms_text == "Памятник Василию" or ms_text == "Памятник василию":
                bot.send_message(chat_id, text="Правильно!")
            else:
                bot.send_message(chat_id, text="Не угадали( \n Это Памятник бомбардиру Василию")
        if place == "https://images.spasibovsem.ru/catalog/original/strelka-vasilevskogo-ostrova-sankt-peterburg-rossiya-otzyvy-1578937511.jpg":
            if ms_text == "Стрелка Васильевского острова" or ms_text == "стрелка васильевского острова" or ms_text == "Стрелка васильевского острова" or ms_text == "стрелка Васильевского острова":
                bot.send_message(chat_id, text="Правильно!")
            else:
                bot.send_message(chat_id, text="Не угадали( \n Это Стрелка Васильевского острова")
        if place == "https://www.spbmuzei.ru/wp-content/uploads/2019/12/menshik2-1140x588.jpg":
            if ms_text == "Дворец Меншикова" or ms_text == "дворец меншикова" or ms_text == "Дворец меншикова" or ms_text == "дворец Меншикова":
                bot.send_message(chat_id, text="Правильно!")
            else:
                bot.send_message(chat_id, text="Не угадали( \n Это Дворец Меншикова")
        if place == "https://kayakspb.ru/wp-content/uploads/2016/11/repina_1.jpg":
            if ms_text == "Улица Репина" or ms_text == "улица Репина" or ms_text == "ул Репина" or ms_text == "Улица репина" or ms_text == "ул. Репина":
                bot.send_message(chat_id, text="Правильно!")
            else:
                bot.send_message(chat_id, text="Не угадали( \n Это Улица Репина")
        if place == "https://petersburg24.ru/files/attachment_images/973_image.jpg?1531052667":
            if ms_text == "Двор духов" or ms_text == "двор духов":
                bot.send_message(chat_id, text="Правильно!")
            else:
                bot.send_message(chat_id, text="Не угадали( \n Это Двор духов")
        if place == "https://avatars.mds.yandex.net/get-altay/1545421/2a0000016eeeabe47a56138eeca259321201/XXL":
            if ms_text == "Севкабель Порт" or ms_text == "Севкабель порт" or ms_text == "севкабель порт" or ms_text == "севкабель" or ms_text == "Севкабель":
                bot.send_message(chat_id, text="Правильно!")
            else:
                bot.send_message(chat_id, text="Не угадали( \n Это Севкабель Порт")
        if place == "https://n1s1.hsmedia.ru/8b/d9/40/8bd940ad98b075dadf3d57d523bce512/1000x667_0xac120003_15881333861615822925.jpg":
            if ms_text == "Государственный Эрмитаж" or ms_text == "государственный эрмитаж" or ms_text == "Эрмитаж" or ms_text == "Государственный эрмитаж" or ms_text == "эрмитаж":
                bot.send_message(chat_id, text="Правильно!")
            else:
                bot.send_message(chat_id, text="Не угадали( \n Это Государственный Эрмитаж")
        if place == "https://photocentra.ru/images/main77/770044_main.jpg":
            if ms_text == "Исаакиевский собор" or ms_text == "исаакиевский собор" or ms_text == "Исаакиевский" or ms_text == "исаакиевский":
                bot.send_message(chat_id, text="Правильно!")
            else:
                bot.send_message(chat_id, text="Не угадали( \n Это Исаакиевский собор")
        if place == "https://avatars.mds.yandex.net/get-zen_doc/1861837/pub_5df61efd8f011100ad77a72f_5df66ddf1e8e3f00acffb804/scale_1200":
            if ms_text == "Дворцовая площадь" or ms_text == "дворцовая площадь" or ms_text == "Дворцовая" or ms_text == "дворцовая":
                bot.send_message(chat_id, text="Правильно!")
            else:
                bot.send_message(chat_id, text="Не угадали( \n Дворцовая площадь")
        if place == "https://60wt.ru/upload/iblock/6a9/6a9127c167679bc5cbcd5c89d8af34f2.jpeg":
            if ms_text == "Сенатская площадь" or ms_text == "сенатская площадь":
                bot.send_message(chat_id, text="Правильно!")
            else:
                bot.send_message(chat_id, text="Не угадали( \n Это Сенатская площадь")
        if place == "https://cs12.pikabu.ru/post_img/big/2020/07/13/9/1594652562126321417.jpg":
            if ms_text == "Остров Новая Голландия" or ms_text == "Новая Голландия" or ms_text == "новая голландия" or ms_text == "Новая голландия" or ms_text == "остров новая голландия":
                bot.send_message(chat_id, text="Правильно!")
            else:
                bot.send_message(chat_id, text="Не угадали( \n Это Остров Новая Голландия")
        if place == "https://ksanytch.ru/Piter/OsobnyakRumyantseva.jpg":
            if ms_text == "Особняк Румянцева" or ms_text == "особняк Румянцева" or ms_text == "особняк Румянцева" or ms_text == "Особняк румянцева":
                bot.send_message(chat_id, text="Правильно!")
            else:
                bot.send_message(chat_id, text="Не угадали( \n Это Особняк Румянцева")
        if place == "https://peterburg.center/sites/default/files/9._st._petersburg._marble_palace.jpg":
            if ms_text == "Мраморный дворец" or ms_text == "мраморный дворец":
                bot.send_message(chat_id, text="Правильно!")
            else:
                bot.send_message(chat_id, text="Не угадали( \n Это Мраморный дворец")
        if place == "https://sun6-23.userapi.com/impg/kiv0cita3Yhxit__OjtjhBD7zf8wReX0No12ew/zqwFzbs5CP4.jpg?size=697x582&quality=96&sign=ed24e08de8ce802047492ce182056ba3&c_uniq_tag=jNSJCSMugm3ZxqFenfkoNRDwPaARGbowdivSuBiq2GI&type=album":
            if ms_text == "Владимирский дворец" or ms_text == "владимирский дворец":
                bot.send_message(chat_id, text="Правильно!")
            else:
                bot.send_message(chat_id, text="Не угадали( \n Это Владимирский дворец")
        if place == "https://i02.fotocdn.net/s112/b1274b99ea2162de/public_pin_l/2522608915.jpg":
            if ms_text == "Адмиралтейство" or ms_text == "адмиралтейство":
                bot.send_message(chat_id, text="Правильно!")
            else:
                bot.send_message(chat_id, text="Не угадали( \n Это Адмиралтейство")
        if place == "https://rogaine-spb.ru/wp-content/uploads/2019/02/2258695da86e048dce7bd8c62d157175.jpg":
            if ms_text == "Московские Триумфальные ворота" or ms_text == "Московские триумфальные ворота" or ms_text == "московские триумфальные ворота" or ms_text == "Триумфальные ворота" or ms_text == "триумфальные ворота":
                bot.send_message(chat_id, text="Правильно!")
            else:
                bot.send_message(chat_id, text="Не угадали( \n Это Московские Триумфальные ворота")
        if place == "https://poisknews.ru/wp-content/uploads/2019/05/shutterstock_1098116876.jpg":
            if ms_text == "Пулковская обсерватория" or ms_text == "пулковская обсерватория":
                bot.send_message(chat_id, text="Правильно!")
            else:
                bot.send_message(chat_id, text="Не угадали( \n Это Пулковская обсерватория")
        if place == "https://kikimoraki.ru/wp-content/uploads/2020/08/sovremennye-muzei-v-sankt-peterburge-chto-posetit-i-posmotret-1.jpg":
            if ms_text == "Музей Гранд Макет Россия" or ms_text == "музей Гранд Макет Россия" or ms_text == "Гранд Макет Россия" or ms_text == "Гранд макет россия" or ms_text == "гранд макет россия":
                bot.send_message(chat_id, text="Правильно!")
            else:
                bot.send_message(chat_id, text="Не угадали( \n Это Музей Гранд Макет Россия")
        if place == "https://sdelanounas.ru/i/d/3/d/f_d3d3LmxlbnN2ZXQuc3BiLnJ1L2QvMjY5MDkvZC9wbG9zY2hhZC1wb2JlZHkuanBnP19faWQ9MTM2NDgw.jpeg":
            if ms_text == "Площадь Победы" or ms_text == "Площадь победы" or ms_text == "площадь победы" or ms_text == "площадь Победы":
                bot.send_message(chat_id, text="Правильно!")
            else:
                bot.send_message(chat_id, text="Не угадали( \n Это Площадь Победы")
        if place == "https://i05.fotocdn.net/s108/5e6d346af19e01fc/public_pin_l/2383686541.jpg":
            if ms_text == "Московский парк Победы" or ms_text == "московский парк победы" or ms_text == "Московский парк победы" or ms_text == "московский парк Победы" or ms_text == "Парк Победы" or ms_text == "Парк победы" or ms_text == "парк победы" or ms_text == "парк Победы":
                bot.send_message(chat_id, text="Правильно!")
            else:
                bot.send_message(chat_id, text="Не угадали( \n Это Московский парк Победы")
        if place == "https://upload.wikimedia.org/wikipedia/commons/7/7e/5238._St._Petersburg._Resurrection_Cathedral.jpg":
            if ms_text == "Воскресенский Новодевичий Монастырь" or ms_text == "Воскресенский новодевичий монастырь" or ms_text == "воскресенский новодевичий монастырь" or ms_text == "Новодевичий монастырь" or ms_text == "новодевичий монастырь" or ms_text == "воскресенский монастырь" or ms_text == "Воскресенский монастырь":
                bot.send_message(chat_id, text="Правильно!")
            else:
                bot.send_message(chat_id, text="Не угадали( \n Это Воскресенский Новодевичий монастырь")
        if place == "https://i.travelapi.com/hotels/15000000/14820000/14815600/14815516/9410461b_z.jpg":
            if ms_text == "Пулковский парк" or ms_text == "пулковский парк":
                bot.send_message(chat_id, text="Правильно!")
            else:
                bot.send_message(chat_id, text="Не угадали( \n Это Пулковский парк")
        if place == "https://static.tildacdn.com/tild3939-6337-4535-b538-656434316461/faberge1.jpg":
            if ms_text == "Музей Фаберже" or ms_text == "Музей фаберже" or ms_text == "музей фаберже" or ms_text == "Фаберже" or ms_text == "фаберже":
                bot.send_message(chat_id, text="Правильно!")
            else:
                bot.send_message(chat_id, text="Не угадали( \n Это Музей Фаберже")
        if place == "https://www.in4s.net/wp-content/uploads/2020/04/Ruski-muzej.jpg":
            if ms_text == "Михайловский дворец" or ms_text == "михайловский дворец":
                bot.send_message(chat_id, text="Правильно!")
            else:
                bot.send_message(chat_id, text="Не угадали( \n Это Михайловский дворец")
        if place == "https://traveltimes.ru/wp-content/uploads/2021/08/2734040772.jpg":
            if ms_text == "Казанский кафедральный собор" or ms_text == "казанский кафедральный собор" or ms_text == "Казанский собор" or ms_text == "казанский собор":
                bot.send_message(chat_id, text="Правильно!")
            else:
                bot.send_message(chat_id, text="Не угадали( \n Это Казанский кафедральный собор")
        if place == "https://sun9-38.userapi.com/impg/bZsnLjj5V9jL9qIjie59W88PdR0X4qvM2pNVbg/czpuVVOQDok.jpg?size=807x538&quality=96&sign=089b8281a0b0dd98e0542932e783aba5&c_uniq_tag=Mhb6xxrSU5JljiTViefoMZb6EUsJ9d149iPbcnfXix4&type=album":
            if ms_text == "Российский этнографический музей" or ms_text == "российский этнографический музей" or ms_text == "Этнографический музей" or ms_text == "этнографический музей":
                bot.send_message(chat_id, text="Правильно!")
            else:
                bot.send_message(chat_id, text="Не угадали( \n Это Российский этнографический музей")
        if place == "https://puzzleit.ru/files/puzzles/207/207272/_original.jpg":
            if ms_text == "Михайловский замок" or ms_text == "Михайловский Замок" or ms_text == "михайловский замок":
                bot.send_message(chat_id, text="Правильно!")
            else:
                bot.send_message(chat_id, text="Не угадали( \n Это Михайловский Замок")
        if place == "https://farm2.staticflickr.com/1819/44225802111_71ab67c29e_h.jpg":
            if ms_text == "Летний сад" or ms_text == "летний сад":
                bot.send_message(chat_id, text="Правильно!")
            else:
                bot.send_message(chat_id, text="Не угадали( \n Это Летний сад")
        if place == "https://aif-turkey.ru/800/600/http/s1.fotokto.ru/photo/full/444/4449040.jpg":
            if ms_text == "Строгановский дворец" or ms_text == "строгановский дворец":
                bot.send_message(chat_id, text="Правильно!")
            else:
                bot.send_message(chat_id, text="Не угадали( \n Это Строгановский дворец")
        if place == "https://perin-spb.ru/images/1.jpg":
            if ms_text == "Перинные ряды" or ms_text == "Арт-Центр в Перинных Рядах" or ms_text == "Арт-центр в перинных рядах" or ms_text == "Арт-центр в Перинных рядах" or ms_text == "арт-центр в перинных рядах" or ms_text == "арт-центр в Перинных рядах":
                bot.send_message(chat_id, text="Правильно!")
            else:
                bot.send_message(chat_id, text="Не угадали( \n Это Перинные Ряды")
        if place == "https://ic.pics.livejournal.com/classiks/23976823/512704/512704_original.jpg":
            if ms_text == "Граффити Виктор Цой" or ms_text == "граффити Виктор Цой" or ms_text == "граффити виктор цой" or ms_text == "Граффити виктор цой":
                bot.send_message(chat_id, text="Правильно!")
            else:
                bot.send_message(chat_id, text="Не угадали( \n Это Граффити Виктор Цой")
        if place == "https://weatlas.com/img/landmarks/8dcee87215dcc73d6e3d3a70c1a623b6.jpg":
            if ms_text == "Набережная канала Грибоедова" or ms_text == "набережная канала Грибоедова" or ms_text == "Набережная канала грибоедова" or ms_text == "набережная канала грибоедова":
                bot.send_message(chat_id, text="Правильно!")
            else:
                bot.send_message(chat_id, text="Не угадали( \n Это Набережная канала Грибоедова")
        if place == "https://np-travel.spb.ru/assets/gallery/68/405.jpg":
            if ms_text == "Петропавловская крепость" or ms_text == "петропавловская крепость":
                bot.send_message(chat_id, text="Правильно!")
            else:
                bot.send_message(chat_id, text="Не угадали( \n Это Петропавловская крепость")
        if place == "https://i12.fotocdn.net/s105/7e73991d70a1cc11/public_pin_l/2242418389.jpg":
            if ms_text == "Елагин остров" or ms_text == "елагин остров":
                bot.send_message(chat_id, text="Правильно!")
            else:
                bot.send_message(chat_id, text="Не угадали( \n Это Елагин остров")
        if place == "https://forpost-sz.ru/sites/default/files/doc/2020/08/09/116906703_718768992297190_4461788238576538092_n.jpg":
            if ms_text == "Парк аттракционов Диво Остров" or ms_text == "парк аттракционов диво остров" or ms_text == "Диво Остров" or ms_text == " Диво остров" or ms_text == "диво остров":
                bot.send_message(chat_id, text="Правильно!")
            else:
                bot.send_message(chat_id, text="Не угадали( \n Это Парк аттракционов Диво Остров")
        if place == "https://cdn.spbdnevnik.ru/uploads/block/image/454986/__medium_selN-rfU_yg.jpg.jpg":
            if ms_text == "Ботанический сад" or ms_text == "ботанический сад":
                bot.send_message(chat_id, text="Правильно!")
            else:
                bot.send_message(chat_id, text="Не угадали( \n Это Ботанический сад Петра Великого")
        if place == "https://peterburg-blog.ru/wp-content/uploads/2017/01/домик-петра-первого-в-петербурге.jpg":
            if ms_text == "Домик Петра 1" or ms_text == "домик петра 1" or ms_text == "Домик петра 1" or ms_text == "домик Петра 1":
                bot.send_message(chat_id, text="Правильно!")
            else:
                bot.send_message(chat_id, text="Не угадали( \n Это Домик Петра 1")
        if place == "https://cat-cat-cat.ru/photo/2015/01/MG_5398-2-.jpg":
            if ms_text == "Александровский парк" or ms_text == "александровский парк" or ms_text == "Александровский Парк":
                bot.send_message(chat_id, text="Правильно!")
            else:
                bot.send_message(chat_id, text="Не угадали( \n Это Александровский парк")
        if place == "https://www.visit-petersburg.ru/upload/iblock/429/00kwgh5t7ake3i8pg89jppgrb09am35z/1696_cover.jpg":
            if ms_text == "Приморский парк Победы" or ms_text == "Приморский парк победы" or ms_text == "приморский парк победы" or ms_text == "приморский парк Победы":
                bot.send_message(chat_id, text="Правильно!")
            else:
                bot.send_message(chat_id, text="Не угадали( \n Это Приморский парк Победы")
        if place == "https://korona-severa.ru/wp-content/uploads/c/5/b/c5ba1c822cac2a2a851b8432c2838ece.jpeg":
            if ms_text == "Петровская набережная" or ms_text == "петровская набережная":
                bot.send_message(chat_id, text="Правильно!")
            else:
                bot.send_message(chat_id, text="Не угадали( \n Это Петровская набережная")
        if place == "https://sun9-40.userapi.com/bWQbmy9CcjGfSQ3o_4tKlhJiD5W_jLqaVwC1og/54IESpfAAcw.jpg":
            if ms_text == "Лопухинский сад" or ms_text == "лопухинский сад":
                bot.send_message(chat_id, text="Правильно!")
            else:
                bot.send_message(chat_id, text="Не угадали( \n Это Лопухинский сад")
        if place == "https://s00.yaplakal.com/pics/pics_original/6/6/1/10239166.jpg":
            if ms_text == "Каменностровский проспект" or ms_text == "каменностровский проспект":
                bot.send_message(chat_id, text="Правильно!")
            else:
                bot.send_message(chat_id, text="Не угадали( \n Это Каменностровский проспект")

def goto_menu(chat_id, name_menu):
    global target_menu
    if name_menu == "Выход" and Menu.cur_menu != None and Menu.cur_menu.parent != None:
        target_menu = Menu.getMenu(Menu.cur_menu.parent.name)
    else:
        target_menu = Menu.getMenu(name_menu)
    if target_menu != None:
        bot.send_message(chat_id, text=target_menu.name, reply_markup=target_menu.markup)

bot.infinity_polling()
print()
