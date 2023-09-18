import types
import telebot
import buttons

bot = telebot.TeleBot('5926697072:AAG_ix8bBs7sZQXINY31too3qo-Vq4OnirA')
@bot.message_handler(commands=['start'])
def start_message(message):
    global user_id
    user_id = message.from_user.id
    bot.send_message(user_id, message.from_user.username + ' Добро пожаловать Выберите кнопку',
                     reply_markup=buttons.choice_buttons())
@bot.message_handler(content_types=['text'])
def start_bot_text(message):
    if message.text =='Заказать услугу':
        bot.send_message(message.from_user.id, 'Отправьт свое имя', reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, get_name)
def get_name (message):
    user_name = message.text
    bot.send_message(message.from_user.id, 'Отлично теперь оставьте номер телфона',reply_markup=buttons.number_buttons())
    bot.register_next_step_handler(message, get_number, user_name)
def get_number (message, user_name):
    if message.contact and message. contact.phone_number:
        user_number = message.contact.phone_number
        bot.send_message(message.from_user.id, 'Отправьте локацию', reply_markup =buttons.geo_button())
        bot.register_next_step_handler(message, get_location, user_number, user_name)
    else:
        bot.send_message(message.from_user.id, "отправь через кнопку")
        bot.register_next_step_handler(message, user_name, get_number)
def get_location(message,user_name,user_number):
    if message.location:
        user_location = message.location
        bot.send_message(message.from_user.id, 'напишите услугу', reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, get_servise, user_name, user_number, get_location)
    else:
        bot.send_message(message.from_user.id, "Отправьте локацию через кнопку")
        bot.register_next_step_handler(message, user_name, user_number, get_location)

def get_servise(message, user_name,user_number,user_location):
    user_servise = message.text
    bot.send_message(message.from_user.id,'какие сроки')
    bot.register_next_step_handler(message,get_deadline,user_name,user_number,user_location,user_servise)

def get_deadline(message,user_mame,user_number,user_servise,user_location,):
    user_deadline = message.text
    bot.send_message(-4043040524, f'Новый заказ\n'
                                  f'Имя:{user_mame}\n\n'
                                  f'номер:{user_number}\n\n'
                                  f'локация:{user_location}\n\n'
                                  f'сервис:{user_servise}\n\n'
                                  f'скроки:{user_deadline}\n\n')
    bot.send_message(message.from_user.id, 'Ваши данные сохранены по ссылке https://t.me/+mkQS5JELKyY1OTY6 :)')
    bot.process_new_messages(message, start_bot_text)


bot.infinity_polling()