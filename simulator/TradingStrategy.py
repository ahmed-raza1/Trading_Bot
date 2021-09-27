import talib
from LiquidityProvider import *
import pandas and pd
import matplotlib as plt


class TradingStrategy:
    def __init__(symbol):
        print("Strategy Initlized")

    def SMA(close):
        speriod = 10
        lperiod = 20
        shortSMA = ta.SMA(close, sPeriod)
        longSMA = ta.SMA(close, lPeriod)
        smaSell = ((shortSMA <= longSMA) & (
            shortSMA.shift(1) >= longSMA.shift(1)))
        smaBuy = ((shortSMA >= longSMA) & (
            shortSMA.shift(1) <= longSMA.shift(1)))
        return smaSell, smaBuy, shortSMA, longSMA

    def RSI(close):
        rsi = ta.RSI(close, timePeriod)
        rsiSell = (rsi > 70) & (rsi.shift(1) <= 70)
        rsiBuy = (rsi < 30) & (rsi.shift(1) >= 30)
        return rsiSell, rsiBuy, rsi

    def MCAD(close):
        speriod = 9
        lperiod = 18
        shortEMA = ta.EMA(close, sPeriod)
        longEMA = ta.EMA(close, lPeriod)
        MACD = shortEMA - longEMA
        signal = talib.EMA(MACD, 5)

    @staticmethod
    def technical_plot(symbol):
        data = LiquidityProvider.get_data_hist(symbol)
        close = data[:, 4]
        data['upper_band'], data['middle_band'], data['lower_band'] = ta.BBANDS(
            close, timeperiod=20)
        data[['close', 'upper_band', 'middle_band',
              'lower_band']].plot(figsize=(10, 5))
        plt.show()

    def strategy(close):
