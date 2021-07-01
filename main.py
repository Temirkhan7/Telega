import telebot
import os


bot = telebot.TeleBot("1899262722:AAHSl3ZuCM17iMvgHklY7g5Yhzk9HY32kjQ")


def log(message, answer):
    print("\n ------------")

    from datetime import datetime

    print(datetime.now())

    print("Сообщение от {0} {1}. (id = {2}) \n Текст - {3}".format(message.from_user.first_name,

                                                                   message.from_user.last_name,

                                                                   str(message.from_user.id),

                                                                   message.text))


@bot.message_handler(commands=["start"])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)

    # переменная, которая хранит разметку нашей клавиатуры

    # 1 - True - для того,чтобы сделать размер клавиатуры поменьше, False - побольше

    # 2 - True - убрать клавиатуру после одного раза пользования

    user_markup.row('/start', '/stop')  # добавляем команды

    user_markup.row('фото', 'аудио', 'документы')  # и ограничиваем размер клавиатуры 3х4

    user_markup.row('стикер', 'видео', 'голос', 'локация')

    # перед тем, как показать клавиатуру пользователю бот должен отправить сообщение вроде приветствия

    bot.send_message(message.from_user.id, 'Добро пожаловать', reply_markup=user_markup)


@bot.message_handler(commands=["stop"])
def handle_start(message):  # функция, которая убирает нашу клавиатуру

    hide_markup = telebot.types.ReplyKeyboardRemove()

    bot.send_message(message.from_user.id, '...', reply_markup=hide_markup)

@bot.message_handler(commands=["help"])
def handle_text(message):
    bot.send_message(message.chat.id, """Чем могу помочь?""")



@bot.message_handler(content_types=["text"])

def handle_text(message):

    if message.text == 'фото':

        directory = '/Users/azimo/OneDrive/Рабочий стол/PhotoTelegram'

        img = open(directory+ '/'+"phototele.JFIF", 'rb')

        bot.send_chat_action(message.from_user.id, 'upload_photo')

        bot.send_photo(message.from_user.id, img)

        img.close()

    elif message.text == 'аудио':

        audio = open("/Users/azimo/Music/iTunes/10age_-_pushka.mp3", 'rb')

        bot.send_chat_action(message.from_user.id, 'upload_audio')

        bot.send_audio(message.from_user.id, audio)

        audio.close()
    elif message.text == 'документы':

        directory = '/Users/azimo/OneDrive/Рабочий стол/DocumentsTelegram'

        all_files_in_directory = os.listdir(directory)

        print(all_files_in_directory)

        for files in all_files_in_directory:
            document = open(directory + '/' + files, 'rb')

            bot.send_chat_action(message.from_user.id, 'upload_document')

            bot.send_document(message.from_user.id, document)

            document.close()

    elif message.text == 'локация':

        bot.send_location(message.from_user.id, 43.23827342474483, 76.89753494602552)

def handle_text(message):
    answer = "Извините, я еще не научился отвечать на такие сообщения"

    if message.text.lower() == "привет":

        answer = "Приветствую Semga Pidr"

        bot.send_message(message.chat.id, answer)

        log(message, answer)

    elif message.text.lower() == "как дела?":

        answer = "Получше чем у тебя Семга?"

        bot.send_message(message.chat.id, answer)

        log(message, answer)

    elif message.text.lower() == "хорошо":

        answer = "Классно, хорошего дня"

        bot.send_message(message.chat.id, answer)

        log(message, answer)

    else:

        bot.send_message(message.chat.id, answer)

        log(message, answer)


bot.polling(none_stop=True, interval=0)