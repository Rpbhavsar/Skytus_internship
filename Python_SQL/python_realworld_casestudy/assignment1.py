import sqlite3
conn = sqlite3.connect("ecommerce.db")

cursor=conn.cursor()

cursor.execute("PRAGMA foreign_keys=ON")

cursor.execute('''CREATE TABLE IF NOT EXISTS customers(
    customer_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    city TEXT NOT NULL)
 ''')

cursor.execute('''CREATE TABLE IF NOT EXISTS orders(
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    order_date TEXT NOT NULL,
    amount REAL NOT NULL CHECK(amount >= 0),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id))
''')

cursor.execute('''CREATE TABLE IF NOT EXISTS products(
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    price REAL NOT NULL CHECK(price>=0))
 ''')

cursor.execute('''CREATE TABLE IF NOT EXISTS order_items(
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER NOT NULL CHECK(quantity>0),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id))
''')

customers=[
    (1,"John","NYC"),
    (2,"Aron","LA"),
    (3,"Karan","Mumbai"),
    (4,"Alvin","Delhi")
]

cursor.executemany("""
INSERT OR IGNORE INTO customers (customer_id, name, city)
VALUES (?, ?, ?)
""", customers)

products=[
    (1,"laptop",10000),
    (2,"mobile",20000),
    (3,"keyboard",5000),
    (4,"mouse",2000)
]
cursor.executemany("""
INSERT OR IGNORE INTO products (product_id, product_name, price)
VALUES (?, ?, ?)
""", products)

orders=[
    (101,1,"2024-02-02",20000),
    (102,2,"2024-02-02",10000),
    (103,3,"2025-05-05",5000),
    (104,4,"2025-05-07",2000),
    (105,1,"2025-07-09",100000)
]

cursor.executemany("""
INSERT OR IGNORE INTO orders (order_id, customer_id, order_date, amount)
VALUES (?, ?, ?, ?)
""", orders)

order_items=[
    (101, 1, 1),
    (101, 3, 2),
    (102, 2, 2),
    (102, 4, 1),
    (103, 2, 1),
    (103, 3, 2),
    (104, 1, 1),
    (104, 4, 1),
    (105, 2, 1),
    (105, 4, 1)
]
cursor.executemany("""
INSERT OR IGNORE INTO order_items (order_id, product_id, quantity)
VALUES (?, ?, ?)
""", order_items)
conn.commit()

# 1.Total orders per customer
print("===Total orders per customer===")
cursor.execute('''SELECT c.name, count(o.order_id)AS total_orders FROM customers c
LEFT JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name
ORDER BY c.customer_id
 ''')

for name,total_orders in cursor.fetchall():
    print(f"Customer: {name}, Total Orders: {total_orders}")


# 2. customer who never placed an order
print("\n===Customer who never placed an order===")
cursor.execute("""
SELECT c.name, c.city
FROM customers AS c
LEFT JOIN orders AS o
ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL
""")

for name, city in cursor.fetchall():
    print(name, ":", city)

# 3. Highest selling product by quantity
print("\n===Highest selling product by quantity===")
cursor.execute('''SELECT p.product_name, SUM(oi.quantity) AS total_quantity FROM products p
LEFT JOIN order_items oi
ON p.product_id = oi.product_id
GROUP BY p.product_id, p.product_name
ORDER BY total_quantity DESC
LIMIT 1
''')
result = cursor.fetchone()

if result:
    print(result[0], ":", result[1], "units sold")
else:
    print("No products sold yet.")


# 4. Monthely sales report
print("\n===Monthly Sales Report===")
cursor.execute('''SELECT
    strftime('%Y-%m', order_date) AS month,
    SUM(amount) AS total_sales
FROM orders
GROUP BY strftime('%Y-%m', order_date)
ORDER BY month
 ''')

for month, total_sales in cursor.fetchall():
    print(f"Month: {month}, Total Sales: {total_sales}")


# 5. customers with total purchase > 50000
print("\n===Customer with total purchase > 50000")
cursor.execute('''SELECT c.name, SUM(o.amount)AS total_purchase
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name
HAVING SUM(o.amount) > 50000
ORDER BY total_purchase DESC
 ''')

for name, total_purchase in cursor.fetchall():
    print(name, ":", total_purchase)


# 6.TOP 3 cities by revenue
print("\n===Top 3 cities by revenue")
cursor.execute("""
SELECT c.city, SUM(o.amount) AS revenue
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.city
ORDER BY revenue DESC
LIMIT 3
""")

for city, revenue in cursor.fetchall():
    print(city, ":", revenue)
conn.close()