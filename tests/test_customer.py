import unittest
from customer import Customer
from coffee import Coffee

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Alice")
        self.coffee = Coffee("Latte")

    def test_customer_name_valid(self):
        self.assertEqual(self.customer.name, "Alice")

    def test_customer_name_invalid(self):
        with self.assertRaises(ValueError):
            Customer("")

        with self.assertRaises(ValueError):
            Customer("A" * 16)

    def test_create_order(self):
        order = self.customer.create_order(self.coffee, 5.5)
        self.assertEqual(order.customer, self.customer)
        self.assertEqual(order.coffee, self.coffee)

    def test_orders_and_coffees(self):
        self.customer.create_order(self.coffee, 5.0)
        self.customer.create_order(self.coffee, 6.0)

        self.assertEqual(len(self.customer.orders()), 2)
        self.assertEqual(len(self.customer.coffees()), 1)

    def test_most_aficionado(self):
        c1 = Customer("Bob")
        c2 = Customer("Carol")
        coffee = Coffee("Espresso")
        c1.create_order(coffee, 5.0)
        c2.create_order(coffee, 9.0)

        self.assertEqual(Customer.most_aficionado(coffee), c2)
