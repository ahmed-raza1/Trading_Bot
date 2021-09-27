from binance.enums import *
from order import *


class OrderManager:
    order_data = []

    def __init__(self):
        print("Order Manager intialized")
        # order_data = []
        self.buy_data = []
        self.sell_data = []

        print('simulation mode')

    def handle_order_from_risk_manager(self, order):
        if order.side == 'buy':
            order = client.order_limit_buy(
                symbol='BNBBTC',
                quantity=100,
                price='0.00001')
            if order != null:
                self.buy_data.append(order)
                order_data.append(order)

        if order.side == 'sell':
            order = client.order_limit_sell(
                symbol='BNBBTC',
                quantity=100,
                price='0.00001')
            if order != null:
                self.sell_data.append(order)
                order_data.append(order)

    def lookup_order_by_id(self, id):
        for i in range(len(self.orders)):
            if self.orders[i]['id'] == id:
                return self.orders[i]
        return None

    def clean_traded_orders(self):
        order_offsets = []
        for k in range(len(self.orders)):
            if self.orders[k]['status'] == 'filled':
                order_offsets.append(k)
        if len(order_offsets):
            for k in sorted(order_offsets, reverse=True):
                del (self.orders[k])
