import telebot
from config import *
from extensions import *


bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    text ="чтобы начать работу введите команду боту в следующемформате:\n<имя валюты корою переводим> \ <имя валюты в которую переводим> " \
          "\ <количество переводимой валюты>\nувидеть список доступных валют: /values"
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
        values = message.text.split()
        if len(values) != 3:
            raise ApiException('неверное количество параметров!')
        quote, base, amount = values
        new_price = Converter.get_price(quote, base, amount, )
    except ApiException as e:
        bot.reply_to(message, f'Ошибка в команде:\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Ошибка:\nОтсутствует связь с поставщиком данных')
    else:
        bot.reply_to(message, f"цена {amount} {quote} в {base} : {new_price}")


bot.polling(none_stop=True)