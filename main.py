import telebot
from config import *
from extensions import *


bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    text ="Приветствие!"
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['values'])
def start(message: telebot.types.Message):
    text = "доступные валюты"
    for i in exchanges.keys():
        text = '\n'.join((text, i))
    bot.send_message(message.chat.id, text)

@bot.message_handler(content_types=['text'])
def converter(message: telebot.types.Message):
        try:
            base, quote, amount = message.text.split()
        except ValueError as e:
            bot.reply_to(message, 'неверное количество параметров!')
        try:
            new_price = Converter.get_price(base, quote, amount,)
        except ApiException as e:
            bot.reply_to(message, f'ошибка в команде:\n{e}')

        base, quote, amount = message.text.split()
        new_price = Converter.get_price(base, quote, amount, )
        bot.reply_to(message, f"цена {amount} {base} в {quote} : {new_price}")






bot.polling(none_stop=True)