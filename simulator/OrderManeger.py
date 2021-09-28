from binance.enums import *
from Order import *
from LiquidityProvider import *


class OrderManager:
    order_data = []

    def __init__(self, client):
        print("Order Manager intialized")
        # order_data = []
        self.buy_data = []
        self.sell_data = []
        self.client = LiquidityProvider.get_clinet()

        print('simulation mode')

    def handle_order_from_risk_manager(self, order):
        if order.side == 'buy':
            order = self.client.order_market_buy(
                symbol=order.symbol,
                quoteOrderQty=order.qauntity)
            if order != null:
                print("Purchase order made" + order.symbol +
                      " for qaunitity" + order.qauntity + " @ " + order.price)

        if order.side == 'sell':
            order = self.client.order_market_sell(
                symbol=order.symbol,
                quoteOrderQty=order.qauntity)
            if order != null:
                print("Sale order made" + order.symbol +
                      " for qaunitity" + order.qauntity + " @ " + order.price)

    @staticmethod
    def lookup_order_by_id(id):
        for i in range(len(OrderManager.order_data)):
            if OrderManager.order_data[i].id == id:
                return OrderManager.order_data[i]
        return None


# client = Client("reE2ToRoB9AUvIuKt82UKLIsyp5fze39ZAiERi0mz6luLbbpeUFARlEaG4h841Eq",
#                 "rOIRYpnWuT1aJwMZEfUuFrChTnjIYzWAimrP2Z9VrZGzLYthTt0YcewVtjtvMTqc")

om = OrderManager(client)
order1 = Order(1, 'BTC', 'buy', 0.001, 500)
om.order_data.append(order1)
print(om.lookup_order_by_id(1).price)
