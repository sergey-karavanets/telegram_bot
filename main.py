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

    def start_message():


if __name__ == '__main__':
    get_data()