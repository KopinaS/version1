import telebot
from menu import Menu
from telebot import types
import random

bot = telebot.TeleBot('5278792568:AAFt3lJxrghz3F7WiMCKXxsQsfOQ3FC0Lqo')

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
                        'http://sun9-21.userapi.com/impf/NvmvYzObrNy_qhd7cPiyUhHvP_IAPQYl39m4Ig/o6NnXP6Qumw.jpg?size=604x396&quality=96&sign=d1ac3e60d59c5a15db2b2c205d18acaa&type=album')
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
            bot.send_photo(chat_id, 'http://rasfokus.ru/images/photos/medium/b60c4d0f97027fa150f7415ef8ae3724.jpg')
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
            bot.send_photo(chat_id, 'http://www.rgexp.ru/foto/photo/Piter/b12.jpg')
            bot.send_message(chat_id, text="набережная Кутузова, 2 \n"
                                                "Сайт: https://rusmuseum.ru/summer-garden/history/")
        elif nplace == "Строгановский дворец":
            bot.send_photo(chat_id, 'http://top5-top10.ru/wp-content/uploads/2019/07/Строгановский-дворец.jpg')
            bot.send_message(chat_id, text="Невский просп., 17 \n"
                                                "Сайт: https://rusmuseum.ru/stroganov-palace/")
        elif nplace == "Арт-Центр в Перинных Рядах":
            bot.send_photo(chat_id, 'https://перинные.рф/images/1.jpg')
            bot.send_message(chat_id, text="Думская ул., 4")
        elif nplace == "Граффити Виктор Цой":
            bot.send_photo(chat_id, 'https://ic.pics.livejournal.com/classiks/23976823/512704/512704_original.jpg')
            bot.send_message(chat_id, text="ул. Восстания, 8Г")
        elif nplace == "Набережная канала Грибоедова":
            bot.send_photo(chat_id, 'http://s3.fotokto.ru/photo/full/222/2222539.jpg')
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
            bot.send_photo(chat_id, 'http://s4.fotokto.ru/photo/full/97/972284.jpg?r125')
            bot.send_message(chat_id, text="Крестовский просп., 23 \n"
                                                "Сайт: http://pppark.ru/")
        elif pplace == "Петровская набережная":
            bot.send_photo(chat_id,
                               'https://korona-severa.ru/wp-content/uploads/c/5/b/c5ba1c822cac2a2a851b8432c2838ece.jpeg')
        elif pplace == "Лопухинский сад":
            bot.send_photo(chat_id, 'http://s2.fotokto.ru/photo/full/562/5628002.jpg')
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
