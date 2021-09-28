import talib as ta
from LiquidityProvider import *
import pandas as pd
import matplotlib as plt
from RiskManager import *


class TradingStrategy:
    def __init__(self, riskManager):
        print("Strategy Initlized")
        self.rm = riskManager

    @staticmethod
    def SMA(close):
        sPeriod = 10
        lPeriod = 20
        shortSMA = ta.SMA(close, sPeriod)
        longSMA = ta.SMA(close, lPeriod)
        smaSell = ((shortSMA <= longSMA) & (
            shortSMA.shift(1) >= longSMA.shift(1)))
        smaBuy = ((shortSMA >= longSMA) & (
            shortSMA.shift(1) <= longSMA.shift(1)))
        return smaSell, smaBuy, shortSMA, longSMA

    @staticmethod
    def RSI(close):
        rsi = ta.RSI(close, 14)
        rsiSell = (rsi > 70) & (rsi.shift(1) <= 70)
        rsiBuy = (rsi < 30) & (rsi.shift(1) >= 30)
        return rsiSell, rsiBuy, rsi

    @staticmethod
    def MCAD(close):
        sPeriod = 9
        lPeriod = 18
        shortEMA = ta.EMA(close, sPeriod)
        longEMA = ta.EMA(close, lPeriod)
        MACD = shortEMA - longEMA
        signal = ta.EMA(MACD, 5)
        return MACD, signal

    @staticmethod
    def technical_plot(close):
        data['upper_band'], data['middle_band'], data['lower_band'] = ta.BBANDS(
            close, timeperiod=20)
        data[['close', 'upper_band', 'middle_band',
              'lower_band']].plot(figsize=(10, 5))
        plt.show()

    def strategy(self, symbol):
        data = LiquidityProvider.get_data_hist(symbol)
        for each_close, close_time in zip(data_df['close'], data_df['datetime']):
            closes.append(each_close)
            close = np.array(closes)
        # rsisell, rsibuy, rsi = TradingStrategy.RSI(close)
        sell, buy, short, long = TradingStrategy.SMA(close)
        MACD, signal = TradingStrategy.MCAD(close)
        avg_price = client.get_avg_price(symbol)
        upperband_crossed = numpy.where((np_closes > upperband), 1, 0)
        lowerband_crossed = numpy.where((np_closes < lowerband), 1, 0)

        fastk, fastd = talib.STOCHRSI(
            np_closes, timeperiod=14, fastk_period=5, fastd_period=3, fastd_matype=0)

        ast_upperband_crossed = upperband_crossed[-1]
        last_lowerband_crossed = lowerband_crossed[-1]
        last_macd = MACD[-1]
        last_signal = signal[-1]
        last_fastk = fastk[-1]
        last_fastd = fastd[-1]

        if last_macd > last_signal:
        should_buy += 1

        if last_lowerband_crossed:
            should_buy += 1

        if last_macd < last_signal:
            should_sell += 1

        if last_upperband_crossed:
            should_sell += 1

        if last_fastd > 90 and last_fastk > 90:
            should_buy += 1

        if last_fastd <= 20 and last_fastk <= 20:
            should_sell += 1

        if should_buy == 2 and lowest_price < close < avg_price and should_sell == 0:
            self.rm.order_risk_analysis(symbol, 'buy', 'low')
        elif should_buy >= 2 and lowest_price < close < avg_price:
            self.rm.order_risk_analysis(symbol, 'buy', 'medium')
        elif should_sell == 2 and max_price > close > avg_price:
            self.rm.order_risk_analysis(symbol, 'sell', 'low')
        elif should_sell <= 2 and max_price > close > average_price and should_buy == 0:
            self.rm.order_risk_analysis(symbol, 'sell', 'medium')


client = LiquidityProvider.get_client()
symbol = 'ETHBUSD'
data = LiquidityProvider.save_df(symbol)
# print(data)

close = data['close']
print(close)
rsisell, rsibuy, rsi = TradingStrategy.RSI(close)
sell, buy, short, long = TradingStrategy.SMA(close)
MACD, signal = TradingStrategy.MCAD(close)

print(rsibuy)
print(rsisell == True)
