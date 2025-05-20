import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Eve")
        self.coffee = Coffee("Mocha")

    def test_order_initialization(self):
        order = Order(self.customer, self.coffee, 4.5)
        self.assertEqual(order.customer, self.customer)
        self.assertEqual(order.coffee, self.coffee)
        self.assertEqual(order.price, 4.5)

    def test_invalid_customer_type(self):
        with self.assertRaises(TypeError):
            Order("NotCustomer", self.coffee, 4.5)

    def test_invalid_coffee_type(self):
        with self.assertRaises(TypeError):
            Order(self.customer, "NotCoffee", 4.5)

    def test_invalid_price(self):
        with self.assertRaises(ValueError):
            Order(self.customer, self.coffee, 0.5)

        with self.assertRaises(ValueError):
            Order(self.customer, self.coffee, 11.0)

        with self.assertRaises(ValueError):
            Order(self.customer, self.coffee, "free")
