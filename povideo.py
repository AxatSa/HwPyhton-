import json
import telebot
import requests

bot = telebot.TeleBot("6655899756:AAEObBG886lPE4GcElXsZ3s4YHPhA0ti0bc")
Api = 'c5cd0b7e85dab26a794e84fd57075f2f'

@bot.message_handler(comands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет рад тебя видеть, напиши город")

@bot.message_handler(content_types=['text'])
def get_weather(message):
    sity = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={sity}&appid={Api}')
    data = json.loads(res.text)
    bot.reply_to(message, f"Сейчас погода: {data['main']['temp']}")


bot.polling(none_stop=True)