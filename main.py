import telebot
import types
from telebot import types
import random

bot = telebot.TeleBot('5278792568:AAFt3lJxrghz3F7WiMCKXxsQsfOQ3FC0Lqo')  # Создаем экземпляр бота

@bot.message_handler(commands=["start"])
def start(message, res=False):
    chat_id = message.chat.id

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Главное меню")
    btn2 = types.KeyboardButton("Помощь")
    markup.add(btn1, btn2)

    bot.send_message(chat_id,
                     text="Привет, {0.first_name}! Я тестовый бот для курса программирования на языке Пайтон".format(
                         message.from_user))
# -----------------------------------------------------------------------
# Получение сообщений от юзера
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    chat_id = message.chat.id
    ms_text = message.text

    if ms_text == "Главное меню" or ms_text == "👋🏻 Главное меню" or ms_text == "Вернуться на главное меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Прогулки")
        btn2 = types.KeyboardButton("Кафе/рестораны")
        back = types.KeyboardButton("Помощь")
        markup.add(btn1, btn2, back)
        bot.send_message(chat_id, text="Вы в главном меню", reply_markup=markup)

    elif ms_text == "Прогулки":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Выбрать район")
        back = types.KeyboardButton("Помощь")
        markup.add(btn1, back)
        bot.send_message(chat_id, text="Прогулки", reply_markup=markup)

    elif ms_text == "Выбрать район":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Василеостровский район")
        btn2 = types.KeyboardButton("Адмиралтейский район")
        btn3 = types.KeyboardButton("Московский район")
        btn4 = types.KeyboardButton("Невский район")
        btn5 = types.KeyboardButton("Петроградский район")
        back = types.KeyboardButton("Помощь")
        markup.add(btn1, btn2, btn3, btn4, btn5, back)
        bot.send_message(chat_id, text="Выбрать район", reply_markup=markup)

    elif ms_text == "Василеостровский район":
        vplace1 = "Дворик Академии художеств"
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

    elif ms_text == "Адмиралтейский район":
        aplace1 = "Государственный Эрмитаж"
        aplace2 = "Исаакиевский собор"
        aplace3 = "Дворцовая площадь"
        aplace4 = "Зимний дворец Петра I"
        aplace5 = "Остров Новая Голландия"
        aplace6 = "Летний сад"
        aplace7 = "Мраморный дворец (филиал Русского музея)"
        aplace8 = "Владимирский дворец"
        aplace9 = "Особняк Румянцева"
        aplace10 = "Сенатская площадь"
        aplace = random.choice([aplace1, aplace2, aplace3, aplace4, aplace5, aplace6, aplace7, aplace8, aplace9, aplace10])
        bot.send_message(chat_id, text="Можно посетить " + aplace)

    elif ms_text == "Невский район":
        nplace1 = "Музей Фаберже"
        nplace2 = "Государственный Русский музей"
        nplace3 = "Казанский кафедральный собор"
        nplace4 = "Российский этнографический музей"
        nplace5 = "Михайловский Замок"
        nplace6 = "ТИТИКАКА"
        nplace7 = "Строгановский дворец"
        nplace8 = "Арт-Центр в Перинных Рядах"
        nplace9 = "Граффити Виктор Цой"
        nplace10 = "Набережная канала Грибоедова"
        nplace = random.choice([nplace1, nplace2, nplace3, nplace4, nplace5, nplace6, nplace7, nplace8, nplace9, nplace10])
        bot.send_message(chat_id, text="Можно посетить " + nplace)

    elif ms_text == "Московский район":
        mplace1 = "Московские Триумфальные ворота"
        mplace2 = "Пулковская обсерватория"
        mplace3 = "Музей «Гранд Макет Россия»"
        mplace4 = "Площадь Победы"
        mplace5 = "Московской парк Победы"
        mplace6 = "Монумент “Героическим защитникам Ленинграда”"
        mplace7 = "Пулковский парк"
        mplace8 = "Воскресенский Новодевичий Монастырь"
        mplace = random.choice([mplace1, mplace2, mplace3, mplace4, mplace5, mplace6, mplace7, mplace8])
        bot.send_message(chat_id, text="Можно посетить " + mplace)

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

    #elif ms_text == "/vasileostrovsky":
        #key1 = types.InlineKeyboardMarkup()
        #btn1 = types.InlineKeyboardButton(text = "Место", url="https://kudago.com/spb/list/turisticheskij-marshrut-vokrug-stancii-metro-vasil/" or url="https://www.tripadvisor.ru/Attractions-g298507-Activities-zfn8828764-St_Petersburg_Northwestern_District.html)
        #key1.add(btn1)
        #img = open('vasileostrovsky.jpg', 'rb')
        #bot.send_photo(chat_id, img)

    # elif ms_text == "/admiralty":
    # key1 = types.InlineKeyboardMarkup()
    # btn1 = types.InlineKeyboardButton(text = "Место", url="https://www.tripadvisor.ru/Attractions-g298507-Activities-zfn8828749-St_Petersburg_Northwestern_District.html")
    # key1.add(btn1)
    # img = open('admiralty.jpeg', 'rb')
    # bot.send_photo(chat_id, img)

    # elif ms_text == "/moscow":
    # key1 = types.InlineKeyboardMarkup()
    # btn1 = types.InlineKeyboardButton(text = "Место", url="https://susanintop.com/evropa/rossija/sankt-peterburg/moskovskij-rajon-sankt-peterburga")
    # key1.add(btn1)
    # img = open('moscow.jpg', 'rb')
    # bot.send_photo(chat_id, img)

    # elif ms_text == "/nevsky":
    # key1 = types.InlineKeyboardMarkup()
    # btn1 = types.InlineKeyboardButton(text = "Место", url="https://susanintop.com/evropa/rossija/sankt-peterburg/nevskii-rajon")
    # key1.add(btn1)
    # img = open('nevsky.jpg', 'rb')
    # bot.send_photo(chat_id, img)

    # elif ms_text == "/petrogradsky":
    # key1 = types.InlineKeyboardMarkup()
    # btn1 = types.InlineKeyboardButton(text = "Место", url="https://susanintop.com/evropa/rossija/sankt-peterburg/peterburg-v-petrogradskom-rajone")
    # key1.add(btn1)
    # img = open('petrogradsky.jpg', 'rb')
    # bot.send_photo(chat_id, img)

    elif ms_text == "Кафе/рестораны":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Василеостровский р-н")
        btn2 = types.KeyboardButton("Адмиралтейский р-н")
        btn3 = types.KeyboardButton("Московский р-н")
        btn4 = types.KeyboardButton("Невский р-н")
        btn5 = types.KeyboardButton("Петроградский р-н")
        back = types.KeyboardButton("Помощь")
        markup.add(btn1, btn2, btn3, btn4, btn5, back)
        bot.send_message(chat_id, text="Кафе/рестораны", reply_markup=markup)

    elif ms_text == "Василеостровский р-н":
        bot.send_message(chat_id, text="Брюгге - Набережная Макарова, 22 /n ")

    elif ms_text == "Помощь" or ms_text == "/help":
        bot.send_message(chat_id, "Автор: Саша Копина")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(chat_id, text="Напишите автору: https://t.me/kopinaS", reply_markup=markup)

    else:
        bot.send_message(chat_id, text="Я тебя слышу!!! Ваше сообщение: " + ms_text)

# -----------------------------------------------------------------------
bot.polling(none_stop=True, interval=0)

print()
