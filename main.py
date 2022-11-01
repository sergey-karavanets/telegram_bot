import requests


def get_data():
    req = requests.get('https://yobit.net/api/3/ticker/btc_usd')
    response = req.json()