import sqlite3

conn = sqlite3.connect("orders.db")
cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

# 1. Create users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL)
""")
users=[
    (1,"Ronit","Ronit@mail.com","Ronit123"),
    (2,"Hem","Hem@mail.com","Hem123"),
    (3,"Karan","Karan@mail.com","Karan123")
]
cursor.executemany("INSERT OR IGNORE INTO users (user_id, user_name, email, password) VALUES (?, ?, ?, ?)", users)

# 2. Create orders table with foreign key
cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    order_date TEXT DEFAULT CURRENT_TIMESTAMP,
    total_amount REAL NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id))
""")
orders=[
    (1,1,"2025-01-01",1000),
    (2,1,"2025-01-02",1500),
    (3,2,"2025-01-03",2000),
    (4,3,"2025-01-04",2500)
]
cursor.executemany("INSERT OR IGNORE INTO orders (order_id, user_id, order_date, total_amount) VALUES (?, ?, ?, ?)", orders)

# 3. Create index on email
cursor.execute("""
CREATE INDEX IF NOT EXISTS idx_users_email
ON users(email)
""")

# 4. Create view for user order summary
cursor.execute("""
CREATE VIEW IF NOT EXISTS user_order_summary AS
SELECT
    u.user_id,
    u.user_name,
    u.email,
    COUNT(o.order_id) AS total_orders,
    COALESCE(SUM(o.total_amount), 0) AS total_spent
FROM users u
LEFT JOIN orders o
    ON u.user_id = o.user_id
GROUP BY
    u.user_id,
    u.user_name,
    u.email
""")

conn.commit()

print("Database objects created successfully!")

print("\n=== User Order Summary ===")
cursor.execute("SELECT * FROM user_order_summary")

for row in cursor.fetchall():
    print(row)

conn.close()