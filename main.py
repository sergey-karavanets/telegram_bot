import requests
from datetime import datetime
import telebot
from auth_data import token


def get_data():
    req = requests.get('https://yobit.net/api/3/ticker/btc_usd')
    response = req.json()
    sell_price = response['btc_usd']['sell']
    print(f'{datetime.now().strftime("%Y-%m-%d %H:%M")}\nSell BTC price: {sell_price}')


def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handlers(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, "Hi, dude! Write the 'price' to find out the cost of BTC!")


if __name__ == '__main__':
    get_data()
    telegram_bot(token)