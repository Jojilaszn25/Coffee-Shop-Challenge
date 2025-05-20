import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder(unittest.TestCase):
    def setUp(self):
        Order.all_orders = []
        self.customer = Customer("John")
        self.coffee = Coffee("Americano")

    def test_valid_order(self):
        order = Order(self.customer, self.coffee, 4.5)
        self.assertEqual(order.customer, self.customer)
        self.assertEqual(order.coffee, self.coffee)
        self.assertEqual(order.price, 4.5)

    def test_invalid_customer(self):
        with self.assertRaises(TypeError):
            Order("NotACustomer", self.coffee, 4.0)

    def test_invalid_coffee(self):
        with self.assertRaises(TypeError):
            Order(self.customer, "Latte", 4.0)

    def test_invalid_price(self):
        with self.assertRaises(ValueError):
            Order(self.customer, self.coffee, 0.5)
        with self.assertRaises(TypeError):
            Order(self.customer, self.coffee, "expensive")

if __name__ == "__main__":
    unittest.main()
