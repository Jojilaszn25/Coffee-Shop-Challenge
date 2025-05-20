from order import Order  

class Coffee:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Coffee name must be a string")
        if len(name) < 3:
            raise ValueError("Coffee name must be at least 3 characters")
        self._name = name

    @property
    def name(self):
        return self._name

    def orders(self):
        return [order for order in Order.all_orders if order.coffee == self]

    def customers(self):
        unique_customers = set(order.customer for order in self.orders())
        return list(unique_customers)

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        orders = self.orders()
        if not orders:
            return 0
        total = sum(order.price for order in orders)
        return total / len(orders)
