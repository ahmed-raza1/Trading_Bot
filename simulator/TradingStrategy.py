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

    @staticmethod
    def technical(symbol):
