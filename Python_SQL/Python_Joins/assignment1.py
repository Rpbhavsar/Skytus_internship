import sqlite3
conn= sqlite3.connect("Company.db")

cursor=conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees(
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    dept_id INT,
    salary INT
    ) """)

cursor.execute("""
CREATE TABLE IF NOT EXISTS departments(
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50)
    ) """)

employees=[
    (1,'Mit',1,50000),
    (2,'Rohit',2,60000),
    (3,'Amit',1,44000),
    (4,'Sita',3,70000),
    (5,'John',2,45000),
    (6,'Jane',1,80000)
]

departments=[
    (1,'HR'),
    (2,'IT'),
    (3,'Finance')
]

cursor.executemany("INSERT OR IGNORE INTO employees VALUES (?,?,?,?)",employees)
cursor.executemany("INSERT OR IGNORE INTO departments VALUES (?,?)",departments)

conn.commit()


print("\n ===Employee name with department name===")
cursor.execute(""" 
SELECT e.emp_name, d.dept_name FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
""")

for emp_name, dept_name in cursor.fetchall():
    print(emp_name,":",dept_name)

print("\n ===Employee name with salary greater than 50000===")
cursor.execute("""
SELECT emp_name , salary
FROM employees
WHERE salary > 50000
 """)

for emp_name, salary in cursor.fetchall():
    print(emp_name,":",salary)


print("\n ===Department wise total salary===")
cursor.execute("""
SELECT d.dept_name, SUM(e.salary) as total_salary
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
GROUP BY d.dept_name
 """)

for dept_name, total_salary in cursor.fetchall():
    print(dept_name,":",total_salary)


print("\n===Departments with more than 2 employees===")
cursor.execute("""
SELECT d.dept_name, COUNT(e.emp_id)
FROM departments d
JOIN employees e
ON d.dept_id = e.dept_id
GROUP BY d.dept_name
HAVING COUNT(e.emp_id) > 2
""")

for row in cursor.fetchall():
    print(row[0],":",row[1])


print("\n ===Employees without a department===")
cursor.execute("""
SELECT emp_name FROM  employees
WHERE dept_id NOT IN (SELECT dept_id FROM departments)
""")

for emp_name in cursor.fetchall():
    print(emp_name[0])
