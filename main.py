import telebot  # pyTelegramBotAPI	4.3.1

bot = telebot.TeleBot("5278792568:AAFt3lJxrghz3F7WiMCKXxsQsfOQ3FC0Lqo")  # Создаем экземпляр бота
# -----------------------------------------------------------------------
# Функция, обрабатывающая команду /start
@bot.message_handler(commands = ["start"])
def start(message, res=False):
    chat_id = message.chat.id

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Главное меню")
    btn2 = types.KeyboardButton("Помощь")
    markup.add(btn1, btn2)

    bot.send_message(chat_id,
                     text="Привет, {0.first_name}! Я тестовый бот для курса программирования на языке Пайтон".format(
                         message.from_user), reply_markup=markup)
# -----------------------------------------------------------------------
# Получение сообщений от юзера
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    chat_id = message.chat.id
    ms_text = message.text

    if ms_text == "Главное меню" or ms_text == "👋🏻Главное меню" or ms_text == "Вернуться в главное меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Развлечения и прогулки")
        btn2 = types.KeyboardButton("Сериалы")
        back = types.KeyboardButton("Помощь")
        markup.add(btn1, btn2, back)
        bot.send_message(chat_id, text = "Вы в главном меню", reply_markup = markup)
    elif ms_text == "Развлечения":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Прислать опоссума")
        btn2 = types.KeyboardButton("Прислать информацию о достопримечательности")
        back = types.KeyboardButton("Вернуться в главное меню")

    elif ms_text == "/opossum" or ms_text == "Прислать опоссума":
        bot.send_message(chat_id, text = "ещё не готово..." )

    elif ms_text == "Прислать информацию о достопримечательности":
        bot.send_message(chat_id, text = "ещё не готово...")

    elif ms_text == "Сериалы":
        bot.send_message(chat_id, text = "ещё не готово...")

    elif ms_text == "Помощь" or ms_text == "/help":
        bot.send_message(chat_id, "Автор: Копина Саша")
        key1 = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text = "Напишите автору", url = "htts://t.me/kopinaS")
        key1.add(btn1)
    else:
        bot.send_message(chat_id, text = "Я тебя слышу! Ваше сообщение: " + ms_text)

# -----------------------------------------------------------------------
bot.polling(none_stop=True, interval=0) # Запускаем бота

print()
