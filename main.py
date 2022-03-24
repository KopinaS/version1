import telebot
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
        btn2 = types.KeyboardButton("Сериалы")
        back = types.KeyboardButton("Помощь")
        markup.add(btn1, btn2, back)
        bot.send_message(chat_id, text="Вы в главном меню", reply_markup=markup)

    elif ms_text == "Прогулки":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Показать место")
        back = types.KeyboardButton("Помощь")
        markup.add(btn1, back)
        bot.send_message(chat_id, text="Прогулки", reply_markup=markup)

    elif ms_text == "Показать место":
        bot.send_message(chat_id, text="/vasileostrovsky - Василеостровский район")
        bot.send_message(chat_id, text = "/admiralty - Адмиралтейский район")
        bot.send_message(chat_id, text="/moscow - Московский район")
        bot.send_message(chat_id, text="/nevsky - Невский район")
        bot.send_message(chat_id, text="/petrogradsky - Петроградский район")

    elif ms_text == "/vasileostrovsky":
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

    elif ms_text == "Сериалы":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Жанры")
        btn2 = types.KeyboardButton("Подборки")
        back = types.KeyboardButton("Помощь")
        markup.add(btn1, btn2, back)
        bot.send_message(chat_id, text="Сериалы", reply_markup=markup)

    elif ms_text == "Помощь" or ms_text == "/help":
        bot.send_message(chat_id, "Автор: Саша Копина")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        #btn1 = types.KeyboardButton("Напишите автору")
        #markup.add(btn1)
        bot.send_message(chat_id, text="Напишите автору: https://t.me/kopinaS", reply_markup=markup)

    else:
        bot.send_message(chat_id, text="Я тебя слышу!!! Ваше сообщение: " + ms_text)

# -----------------------------------------------------------------------
bot.polling(none_stop=True, interval=0)

print()
