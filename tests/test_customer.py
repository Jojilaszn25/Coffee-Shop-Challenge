import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer(unittest.TestCase):
    def setUp(self):
        Order.all_orders = []  # Reset before each test
        self.customer1 = Customer("Alice")
        self.customer2 = Customer("Bob")
        self.coffee1 = Coffee("Latte")
        self.coffee2 = Coffee("Mocha")

    def test_customer_name_validation(self):
        with self.assertRaises(ValueError):
            Customer("")
        with self.assertRaises(TypeError):
            Customer(123)
        with self.assertRaises(ValueError):
            Customer("x" * 16)

    def test_create_order(self):
        order = self.customer1.create_order(self.coffee1, 5.0)
        self.assertEqual(order.customer, self.customer1)
        self.assertEqual(order.coffee, self.coffee1)

    def test_customer_orders_and_coffees(self):
        self.customer1.create_order(self.coffee1, 5.0)
        self.customer1.create_order(self.coffee2, 6.0)
        self.assertEqual(len(self.customer1.orders()), 2)
        self.assertIn(self.coffee1, self.customer1.coffees())
        self.assertIn(self.coffee2, self.customer1.coffees())

    def test_most_aficionado(self):
        self.customer1.create_order(self.coffee1, 5.0)
        self.customer2.create_order(self.coffee1, 7.0)
        result = Customer.most_aficionado(self.coffee1)
        self.assertEqual(result, self.customer2)

if __name__ == "__main__":
    unittest.main()
