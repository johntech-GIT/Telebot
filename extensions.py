import requests
import json
from config import exchanges

class ApiException(Exception):
    pass
class Converter:
    @staticmethod
    def get_price(base, quote, amount):
        try:
            base_key = exchanges[base.lower()]
        except KeyError:
            return ApiException(f"валюта {base} не найдена!")
        try:
            base_key = exchanges[quote.lower()]
        except KeyError:
            return ApiException(f"валюта {quote} не найдена!")
        if base == quote:
            raise ApiException(f'Невозможно перевезти одинаковые валюты! {base}')
        try:
            amount = float(amount.replace(',','.'))
        except ValueError:
            raise ApiException(f'Не удалось обработать количество {amount} !')


        URL = f'https://min-api.cryptocompare.com/data/price?fsym={exchanges[base]}&tsyms={exchanges[quote]}'
        new_price = (json.loads(requests.get(URL).content)[exchanges[quote]]) * float(amount)
        return round(new_price, 2)


