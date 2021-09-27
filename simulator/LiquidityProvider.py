import os
import csv
from binance.client import Client
import datetime
import time


class LiquidityProvider:
    def __init__(self, symbol):
        self.api_key = "reE2ToRoB9AUvIuKt82UKLIsyp5fze39ZAiERi0mz6luLbbpeUFARlEaG4h841Eq"
        self.api_secret = "rOIRYpnWuT1aJwMZEfUuFrChTnjIYzWAimrP2Z9VrZGzLYthTt0YcewVtjtvMTqc"

        client = Client("reE2ToRoB9AUvIuKt82UKLIsyp5fze39ZAiERi0mz6luLbbpeUFARlEaG4h841Eq",
                        "rOIRYpnWuT1aJwMZEfUuFrChTnjIYzWAimrP2Z9VrZGzLYthTt0YcewVtjtvMTqc")

    # save the data in the csv file
    @staticmethod
    def get_clinet():
        client = Client("reE2ToRoB9AUvIuKt82UKLIsyp5fze39ZAiERi0mz6luLbbpeUFARlEaG4h841Eq",
                        "rOIRYpnWuT1aJwMZEfUuFrChTnjIYzWAimrP2Z9VrZGzLYthTt0YcewVtjtvMTqc")
        return client

    def save_data_csv(self):
        pass

    def provide_live_data(self):
        pass

    @staticmethod
    def get_positions():
        account = client.get_account()
        assets = account['balances']
        return assets

    @staticmethod
    def get_data_hist(name):
        Client = LiquidityProviderfrom.get_client()
        client.get_klines(symbol=name, interval=Client.KLINE_INTERVAL_1DAY)

        return candles

# create a data frame
    @staticmethod
    def save_df(name):
        data = LiquidityProvider.get_data_hist(name)
        df = pd.DataFrame(data, columns=['dateTime', 'open', 'high', 'low', 'close', 'volume', 'closeTime',
                                         'quoteAssetVolume', 'numberOfTrades', 'takerBuyBaseVol', 'takerBuyQuoteVol', 'ignore'])
        # df.dateTime = pd.to_datetime(df.dateTime, unit='ms').dt.strftime(Constants.DateTimeFormat)
        df.set_index('dateTime', inplace=True)
        return df


client = LiquidityProvider.get_clinet()
print(LiquidityProvider.get_positions())
if len(LiquidityProvider.get_positions()) == 0:
    print('null postion')
# print(client)
