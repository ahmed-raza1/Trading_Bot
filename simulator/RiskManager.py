from OrderManeger import *
from LiquidityProvider import *
import Order
from Order import *


class RiskManager:

    # MIN_NUM_SHARES_PER_TRADE = 1
    # MAX_NUM_SHARES_PER_TRADE = 50
    # increment the amount on every consecutive trade
    INCREMENT_NUM_SHARES_PER_TRADE = 0.1
    investment = 500
    risk_limit_weekly_stop_loss = 0.06  # 6 % @ total investment
    INCREMENT_RISK_LIMIT_WEEKLY_STOP_LOSS = 0.02 * investment  # % @ total investment
    risk_limit_monthly_stop_loss = 0.1 * investment  # @ total investment
    INCREMENT_RISK_LIMIT_MONTHLY_STOP_LOSS = 0.02 * investment  # % @ total investment
    risk_limit_max_position = 0.20 * investment  # % @ total investment
    INCREMENT_RISK_LIMIT_MAX_POSITION = 0.02 * investment  # % @ total investment
    RISK_LIMIT_MAX_POSITION_HOLDING_TIME_DAYS = 5
    risk_limit_max_trade_size = 0.15 * investment  # % @ total investment
    INCREMENT_RISK_LIMIT_MAX_TRADE_SIZE = 0.02 * investment  # % @ total investment
    last_risk_change_index = 0

    # MIN_PROFIT_TO_CLOSE = num_shares_per_trade * 10

    # @staticmethod
    def order_risk_analysis(symbol, side, msg):
        if side == 'buy':
            cleint = LiquidityProvider.get_client()
            order_investment = client.get_asset_balance(asset=symbol)['free']

            if side == 'buy':
                if msg == 'low':
                    quant = 0.075 * RiskManager.investment
                if msg == 'medium':
                    quant = 0.15 * RiskManager.investment
                if order_investment != 0:
                    quant = RiskManager.risk_limit_max_position - \
                        order_investment
                    print("RisK Manager purchase order genrated " +
                          "order of" + symbol + " @ " + allownance)
                    id = Order.id + 1
                    ord = Order(id, symbol, 'buy', quant, null)
            if side == 'sell' and order_investment == 0:
                print("Sell order rejected, coin not in holidngs")
            elif side == 'sell':
                if msg == 'low':
                    quant = 0.075 * order_investment
                if msg == 'medium':
                    quant = 0.15 * order_investment
                print("RisK Manager sell order genrated " +
                      "order of" + symbol + " @ " + allownance)
                id = Order.id + 1
                ord = Order(id, symbol, 'sell', quant, null)

    @staticmethod
    def perfomance_analysis(pnl):
        if len(pnls) > 20:
            monthly_pnls = pnls[-1] - pnls[-20]

            if len(pnls) - last_risk_change_index > 20:
                if monthly_pnls > 0:
                    num_shares_per_trade += INCREMENT_NUM_SHARES_PER_TRADE
                    if num_shares_per_trade <= MAX_NUM_SHARES_PER_TRADE:
                        print('Increasing trade-size and risk')
                        risk_limit_weekly_stop_loss += INCREMENT_RISK_LIMIT_WEEKLY_STOP_LOSS
                        risk_limit_monthly_stop_loss += INCREMENT_RISK_LIMIT_MONTHLY_STOP_LOSS
                        risk_limit_max_position += INCREMENT_RISK_LIMIT_MAX_POSITION
                        risk_limit_max_trade_size += INCREMENT_RISK_LIMIT_MAX_TRADE_SIZE
                    else:
                        num_shares_per_trade = MAX_NUM_SHARES_PER_TRADE
                elif monthly_pnls < 0:
                    num_shares_per_trade -= INCREMENT_NUM_SHARES_PER_TRADE
                    if num_shares_per_trade >= MIN_NUM_SHARES_PER_TRADE:
                        print('Decreasing trade-size and risk')
                        risk_limit_weekly_stop_loss -= INCREMENT_RISK_LIMIT_WEEKLY_STOP_LOSS
                        risk_limit_monthly_stop_loss -= INCREMENT_RISK_LIMIT_MONTHLY_STOP_LOSS
                        risk_limit_max_position -= INCREMENT_RISK_LIMIT_MAX_POSITION
                        risk_limit_max_trade_size -= INCREMENT_RISK_LIMIT_MAX_TRADE_SIZE
                    else:
                        num_shares_per_trade = MIN_NUM_SHARES_PER_TRADE

            last_risk_change_index = len(pnls)

        for posit in pos:
            if holding_time > 5:
                weekly_loss = pnls[-1] - pnls[-6]

                if weekly_loss < risk_limit_weekly_stop_loss:
                    print('RiskViolation weekly_loss', weekly_loss,
                          ' < risk_limit_weekly_stop_loss', risk_limit_weekly_stop_loss)
                    risk_violated = True

            if holding_time > 20:
                monthly_loss = pnls[-1] - pnls[-21]

                if monthly_loss < risk_limit_monthly_stop_loss:
                    print('RiskViolation monthly_loss', monthly_loss,
                          ' < risk_limit_monthly_stop_loss', risk_limit_monthly_stop_loss)
                    risk_violated = True

            if (pos.starttime - time) > RISK_LIMIT_MAX_POSITION_HOLDING_TIME_DAYS:
                # posit.sell sell the posit
                print("Selling " + posit + " on voilation of maximum holding days")
