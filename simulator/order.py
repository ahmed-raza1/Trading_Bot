class order:
    order_id_count = 0

    def __init__(id, symbol, side, qauntity, price, status, action):
        self.id = id
        self.symbol = symbol
        self.status = status
        self.side = side
        self.qauntity = qauntity
        self.price = price
        self.action = action
        order_id_count += 1

    def order_validity(self, order):
        if order.qauntity < 0:
                return False
            if order.price < 0:
                return False
        return True
    
    @staticmethod
    def lookup_order_by_id(self, id):
        for i in range(len(self.orders)):
            if self.orders[i]['id'] == id:
                return self.orders[i]
        return None

