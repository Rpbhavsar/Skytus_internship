import sqlite3
conn = sqlite3.connect("SQL_practice.db")
cursor = conn.cursor()

cursor.execute("PRAGMA foreign_keys = ON")


cursor.execute("DROP TABLE IF EXISTS employees")
cursor.execute("DROP TABLE IF EXISTS team_a")
cursor.execute("DROP TABLE IF EXISTS team_b")
cursor.execute("DROP TABLE IF EXISTS Logs")

cursor.execute("""
CREATE TABLE employees (
    emp_id INTEGER PRIMARY KEY,
    emp_name TEXT NOT NULL,
    dept_id INTEGER,
    salary INTEGER,
    hire_date TEXT
)
""")

cursor.executemany("""
INSERT INTO employees
VALUES (?, ?, ?, ?, ?)
""", [
    (1, "Ronit", 1, 50000, "2026-08-10"),
    (2, "Amit", 2, 70000, "2026-05-15"),
    (3, "Hem", 1, 60000, "2026-06-20"),
    (4, "Amit", 2, 70000, "2026-05-15"),
    (5, "Rohit", 3, 45000, "2026-09-01")
])

conn.commit()



# 1. Find the Second-Highest Salary
print("\n=== 1. Second-Highest Salary ===")

cursor.execute("""
SELECT DISTINCT salary
FROM employees
ORDER BY salary DESC
LIMIT 1 OFFSET 1
""")

print(cursor.fetchall())



# 2. Remove Duplicate Employee Records
print("\n=== 2. Remove Duplicate Records ===")

cursor.execute("""
DELETE FROM employees
WHERE emp_id NOT IN (
    SELECT MIN(emp_id)
    FROM employees
    GROUP BY emp_name, dept_id, salary, hire_date
)
""")

conn.commit()

cursor.execute("""
SELECT * FROM employees
ORDER BY emp_id
""")

print(cursor.fetchall())



# 3. Find Common Records in Two Tables
print("\n=== 3. Common Employees ===")

cursor.execute("""
CREATE TABLE team_a (
    name TEXT PRIMARY KEY
)
""")

cursor.execute("""
CREATE TABLE team_b (
    name TEXT PRIMARY KEY
)
""")

cursor.executemany("""
INSERT INTO team_a VALUES (?)
""", [
    ("Ronit",),
    ("Amit",),
    ("Hem",)
])

cursor.executemany("""
INSERT INTO team_b VALUES (?)
""", [
    ("Amit",),
    ("Hem",),
    ("Rohit",)
])

cursor.execute("""
SELECT name FROM team_a
INTERSECT
SELECT name FROM team_b
""")

print(cursor.fetchall())



# 4. Find Employees Hired in the Last 6 Months
print("\n=== 4. Employees Hired in Last 6 Months ===")

cursor.execute("""
SELECT emp_name, hire_date
FROM employees
WHERE date(hire_date) >= date('now', '-6 months')
  AND date(hire_date) <= date('now')
ORDER BY hire_date
""")

print(cursor.fetchall())



# 5. Find Numbers Repeated 3 Times Consecutively
print("\n=== 5. Consecutive Duplicate Numbers ===")

cursor.execute("""
CREATE TABLE Logs (
    id INTEGER PRIMARY KEY,
    num INTEGER NOT NULL
)
""")

cursor.executemany("""
INSERT INTO Logs VALUES (?, ?)
""", [
    (1, 5),
    (2, 5),
    (3, 5),
    (4, 8),
    (5, 8),
    (6, 3)
])

cursor.execute("""
SELECT DISTINCT a.num
FROM Logs AS a
JOIN Logs AS b ON b.id = a.id + 1
JOIN Logs AS c ON c.id = a.id + 2
WHERE a.num = b.num
  AND b.num = c.num
""")

print(cursor.fetchall())


conn.commit()
conn.close()

print("\nAll SQL practice questions completed!")