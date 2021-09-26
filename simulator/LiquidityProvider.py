import os
import csv
from binance.client import Client


# privdie all the data and informaton
class LiquidityProvider:
    api_key = "reE2ToRoB9AUvIuKt82UKLIsyp5fze39ZAiERi0mz6luLbbpeUFARlEaG4h841Eq"
    api_secret = "rOIRYpnWuT1aJwMZEfUuFrChTnjIYzWAimrP2Z9VrZGzLYthTt0YcewVtjtvMTqc"

    def __init__(self, symbol):
        client = Client(api_key, api_secret)

    # save the data in the csv file

    def save_data_csv(self):
        pass

    # create a data frame
    def save_df(self):
        pass

    def provide_live_data(self):
        pass

    @staticmethod
    def get_positions(self):
        account = client.get_account()
        assets = account['balances']
        return assets

    @staticmethod
    def get_data_hist(name):

        candles = candles = client.get_klines(
            symbol=name, interval=Client.KLINE_INTERVAL_1DAY)

        return candles
