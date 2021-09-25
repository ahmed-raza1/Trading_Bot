class TradingStrategy:
    def __init__(symbol):
        # NUM_PERIODS_FAST = 3
        K_FAST = 2 / (4)
        ema_fast = 0
        ema_fast_values = []
        # NUM_PERIODS_SLOW = 7
        K_SLOW = 2 / (8)
        ema_slow = 0
        ema_slow_values = []
        apo_values = []
        last_buy_price = 0
        last_sell_price = 0

    def initilize(symbol):
