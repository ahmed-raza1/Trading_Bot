import OrderManeger


class RiskManager:

    MIN_NUM_SHARES_PER_TRADE = 1
    MAX_NUM_SHARES_PER_TRADE = 50
    INCREMENT_NUM_SHARES_PER_TRADE = 2
    # Beginning number of shares to buy/sell on every trade
    num_shares_per_trade = MIN_NUM_SHARES_PER_TRADE
    risk_limit_weekly_stop_loss = 6 % @ total investment
    INCREMENT_RISK_LIMIT_WEEKLY_STOP_LOSS = 2 % @ total investment
    risk_limit_monthly_stop_loss = 10 % @ total investment
    INCREMENT_RISK_LIMIT_MONTHLY_STOP_LOSS = 2 % @ total investment
    risk_limit_max_position = 5
    INCREMENT_RISK_LIMIT_MAX_POSITION = 3
    RISK_LIMIT_MAX_POSITION_HOLDING_TIME_DAYS = 35
    risk_limit_max_trade_size = 20 % @ total investment
    INCREMENT_RISK_LIMIT_MAX_TRADE_SIZE = 2 % @ total investment
    last_risk_change_index = 0

    MIN_PROFIT_TO_CLOSE = num_shares_per_trade * 10

    def __init__(self, order, positions):
        print("Risk Manager intialized")
        self.position = positions

    def clear_offset_positions(order):
        # clear off the postion

    def get_position(self):
        # get current holdings

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
