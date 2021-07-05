
import telebot
import mysql.connector

bot = telebot.TeleBot("1899262722:AAHSl3ZuCM17iMvgHklY7g5Yhzk9HY32kjQ")


db = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="",
      port="3306",
      database="telegramm"
)




cursor = db.cursor()




class User:
    def __init__(self, first_name):
        self.first_name = first_name
        self.last_name = ''

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
        msg = bot.send_message(message.chat.id, "Введите имя")
        bot.register_next_step_handler(msg, process_firstname_step)

user_data = {}

def process_firstname_step(message):
    try:
        user_id = message.from_user.id
        user_data[user_id] = message.text
        print(user_data)
        msg = bot.send_message(message.chat.id, "Введите фамилию")
        bot.register_next_step_handler(msg, process_lastname_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_lastname_step(message):
        user_id = message.from_user.id
        name = user_data[user_id]
        last_name = message.text

        sql = "INSERT INTO users (name, surname, id) \
                                  VALUES (%s, %s, NULL)"
        val = (name, last_name)
        cursor.execute(sql, val)
        db.commit()
        print(user_data)
        bot.send_message(message.chat.id, "Вы успешно зарегистрированны!")


bot.enable_save_next_step_handlers(delay=2)


bot.load_next_step_handlers()

if __name__ == '__main__':
    bot.polling(none_stop=True)