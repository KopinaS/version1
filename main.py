import telebot
from telebot import types
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
        btn1 = types.KeyboardButton("Развлечения и прогулки")
        btn2 = types.KeyboardButton("Сериалы")
        back = types.KeyboardButton("Помощь")
        markup.add(btn1, btn2, back)
        bot.send_message(chat_id, text="Вы в главном меню", reply_markup=markup)

    elif ms_text == "Развлечения и прогулки":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Показать опоссума")
        btn2 = types.KeyboardButton("Информация о достопримечательности")
        back = types.KeyboardButton("Помощь")
        markup.add(btn1, btn2, back)
        bot.send_message(chat_id, text="Развлечения и прогулки", reply_markup=markup)

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
