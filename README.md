# coffee-shop-challenge

##  Requirements

### Models & Validations

#### `Customer`
- `__init__(self, name)` – name must be a string (1–15 chars).
- `name` (property) – getter and setter with validation.
- `.orders()` – returns all orders for that customer.
- `.coffees()` – returns unique list of coffees ordered.
- `.create_order(coffee, price)` – creates and returns a new order.

#### `Coffee`
- `__init__(self, name)` – name must be a string (min 3 chars).
- `name` (property) – read-only.
- `.orders()` – returns all orders of this coffee.
- `.customers()` – returns unique list of customers.
- `.num_orders()` – returns total number of orders.
- `.average_price()` – returns average price of all orders.

#### `Order`
- `__init__(self, customer, coffee, price)` – requires valid instances and price (float between 1.0 and 10.0).
- `customer`, `coffee`, `price` – read-only properties.

---

## Relationships

- One `Customer` can have many `Order`s.
- One `Coffee` can have many `Order`s.
- One `Order` belongs to one `Customer` and one `Coffee`.
- `Customer` <--> `Coffee` is a many-to-many via `Order`.

---

## Running Tests

Make sure you're inside your pipenv shell:

```bash
pipenv shell
python -m unittest discover tests
