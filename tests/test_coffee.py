import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCoffee(unittest.TestCase):
    def setUp(self):
        Order.all_orders = []
        self.customer = Customer("Alice")
        self.coffee = Coffee("Espresso")

    def test_coffee_name_validation(self):
        with self.assertRaises(ValueError):
            Coffee("AB")
        with self.assertRaises(TypeError):
            Coffee(123)

    def test_orders_and_customers(self):
        self.customer.create_order(self.coffee, 4.0)
        self.assertEqual(len(self.coffee.orders()), 1)
        self.assertIn(self.customer, self.coffee.customers())

    def test_num_orders_and_avg_price(self):
        self.customer.create_order(self.coffee, 4.0)
        self.customer.create_order(self.coffee, 6.0)
        self.assertEqual(self.coffee.num_orders(), 2)
        self.assertAlmostEqual(self.coffee.average_price(), 5.0)

if __name__ == "__main__":
    unittest.main()
