import json
import telebot

exchanges = {
    'доллар': 'USD',
    'евро': 'EUR',
    'рубль': 'RUB'
}
TOKEN = ""
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
    bot.reply_to(message, text)


bot.polling()