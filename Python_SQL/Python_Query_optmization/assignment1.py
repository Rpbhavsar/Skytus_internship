import sqlite3

conn = sqlite3.connect("ecommerce.db")
cursor = conn.cursor()

cursor.execute("PRAGMA foreign_keys = ON")

query = """
SELECT c.name, c.city, o.order_id, o.order_date, o.amount
FROM orders AS o
JOIN customers AS c
    ON c.customer_id = o.customer_id
WHERE o.customer_id = ?
ORDER BY o.order_date DESC
"""


# 1. Analyze query BEFORE creating index
print("\n=== Query Plan Before Index ===")

cursor.execute("DROP INDEX IF EXISTS idx_orders_customer_date")
conn.commit()

cursor.execute("EXPLAIN QUERY PLAN " + query, (1,))

for row in cursor.fetchall():
    print(row[3])


# 2. Create index on orders.customer_id
print("\n=== Creating Index ===")

cursor.execute("""
CREATE INDEX IF NOT EXISTS idx_orders_customer_date
ON orders(customer_id, order_date DESC)
""")

conn.commit()

print("Index created successfully!")


# 3. Analyze query AFTER creating index
print("\n=== Query Plan After Index ===")

cursor.execute("EXPLAIN QUERY PLAN " + query, (1,))

for row in cursor.fetchall():
    print(row[3])


# 4. Execute the optimized JOIN query
print("\n=== Optimized Customer Orders ===")

customer_id = 1

cursor.execute(query, (customer_id,))
results = cursor.fetchall()

if results:
    for name, city, order_id, order_date, amount in results:
        print(
            f"Customer: {name} | City: {city} | "
            f"Order ID: {order_id} | Date: {order_date} | "
            f"Amount: ₹{amount}"
        )
else:
    print("No orders found for this customer.")


# 5. Explain when indexes may not help
print("\n=== When Indexes May Not Help ===")
print("1. Very small tables.")
print("2. Queries that return most rows.")
print("3. Columns with very few distinct values.")
print("4. Tables with frequent INSERT and UPDATE operations.")
print("5. Queries that cannot use the index efficiently.")
conn.close()