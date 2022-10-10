import json
from sys import argv
import urllib.request
import time
import requests
import telebot

""" Получение курса валют и рассчет суммы """

bot = telebot.TeleBot('token');

@bot.message_handler(content_types=['text'])

def get_text_messages(message):
  if message.text == "/start":
      bot.send_message(message.from_user.id, "Привет, введи сумму в Белках")
  elif message.text == "/help":
      bot.send_message(message.from_user.id, "Введи сумму в Белках")
  else:
      global mes
      try:
          mes = float(message.text.replace(',', '.'))
          bot.send_message(message.from_user.id,f"{currency() * mes:.2f} рублей.")
      except Exception:
          bot.send_message(message.from_user.id ,f"Ошибка при обработке {message.text}")

def currency():
    currencies = 'byn'
    basecurrency = 'rub'

    currencyurl = "http://freecurrencyrates.com/api/action.php?do=cvals&iso=" + currencies.replace(',','') + "&f=" + basecurrency + "&v=1&s=cbr"
    f = urllib.request.urlopen(currencyurl)
    obj = json.loads(f.read())
    res = "";
    for c in currencies.split(','):
        res = "{:,.2f}".format(1/obj[c.upper()]).replace(',',' ')
    return float(res)

bot.polling(none_stop=True, interval=0)
