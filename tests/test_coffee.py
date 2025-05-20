import unittest
from customer import Customer
from coffee import Coffee

class TestCoffee(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Dan")
        self.coffee = Coffee("Cappuccino")

    def test_coffee_name_valid(self):
        self.assertEqual(self.coffee.name, "Cappuccino")

    def test_coffee_name_invalid(self):
        with self.assertRaises(ValueError):
            Coffee("A")

    def test_orders_and_customers(self):
        self.customer.create_order(self.coffee, 5.0)
        self.customer.create_order(self.coffee, 6.5)

        self.assertEqual(len(self.coffee.orders()), 2)
        self.assertEqual(len(self.coffee.customers()), 1)

    def test_num_orders_and_average_price(self):
        self.customer.create_order(self.coffee, 5.0)
        self.customer.create_order(self.coffee, 7.0)

        self.assertEqual(self.coffee.num_orders(), 2)
        self.assertAlmostEqual(self.coffee.average_price(), 6.0)
