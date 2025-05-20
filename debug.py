from customer import Customer
from coffee import Coffee
from order import Order

Order.all_orders = []

alice = Customer("Alice")
bob = Customer("Bob")

latte = Coffee("Latte")
mocha = Coffee("Mocha")

order1 = alice.create_order(latte, 4.5)
order2 = alice.create_order(mocha, 5.0)

order3 = bob.create_order(latte, 6.0)

print("All Orders:")
for order in Order.all_orders:
    print(f"{order.customer.name} ordered {order.coffee.name} for ${order.price}")

print("\nAlice's Orders:")
for order in alice.orders():
    print(f"{order.coffee.name} - ${order.price}")

print("\nAlice's Coffees:")
for coffee in alice.coffees():
    print(coffee.name)

print(f"\nLatte order count: {latte.num_orders()}")

print(f"Latte average price: ${latte.average_price():.2f}")

most = Customer.most_aficionado(latte)
print(f"\nMost aficionado of Latte: {most.name if most else 'None'}")
