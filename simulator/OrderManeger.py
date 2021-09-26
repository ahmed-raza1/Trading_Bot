class OrderManager:
    def __init__(self):
        print("Order Manager intialized")
        order_data = []
        buy_data = []
        sell_data = []

        print('simulation mode')

    def handle_order_from_risk_manager(self, order):
        pass

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

    def handle_input_from_market(self):
        # this will updates from the martket

        # if self.gw_2_om is not None:
        #     if len(self.gw_2_om) > 0:
        #         self.handle_order_from_gateway(self.gw_2_om.popleft())
        # else:
        #     print('simulation mode')

        # def handle_order_from_gateway(self, order_update):
        #     order = self.lookup_order_by_id(order_update['id'])
        #     if order is not None:
        #         order['status'] = order_update['status']
        #         if self.om_2_ts is not None:
        #             self.om_2_ts.append(order.copy())
        #         else:
        #             print('simulation mode')
        #         self.clean_traded_orders()
        #     else:
        #         print('order not found')

    def execute_order(order):
        order = client.create_order(
            symbol=order.symbol,
            side=SIDE_BUY,
            type=ORDER_TYPE_LIMIT,
            timeInForce=TIME_IN_FORCE_GTC,
            quantity=100,
            price='0.00001')

    def order_success(self, order):
        # update the order price in the databse

    def order_fail(self, order):
        # deal with the order rejected by the gateway
        #

    def calculate_charges(order):
        # charges for the order to be deducted from the cash

    def record_order(order):
        # record orders in a file
