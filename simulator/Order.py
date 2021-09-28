class Order:
    id = 0

    def __init__(self, id, symbol, side, qauntity, price):
        self.id = id
        self.symbol = symbol
        self.side = side
        self.qauntity = qauntity
        self.price = price

    def order_validity(self, order):
        if order.qauntity < 0:
            return False
        if order.price < 0:
            return False
        return True
