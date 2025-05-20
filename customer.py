from order import Order 

class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not (1 <= len(value) <= 15):
            raise ValueError("Name length must be 1 to 15 characters")
        self._name = value

    def orders(self):
        return [order for order in Order.all_orders if order.customer == self]

    def coffees(self):
        unique_coffees = set(order.coffee for order in self.orders())
        return list(unique_coffees)

    def create_order(self, coffee, price):
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        customers = coffee.customers()
        if not customers:
            return None
        max_spender = None
        max_spent = 0
        for customer in customers:
            total_spent = sum(order.price for order in customer.orders() if order.coffee == coffee)
            if total_spent > max_spent:
                max_spent = total_spent
                max_spender = customer
        return max_spender
