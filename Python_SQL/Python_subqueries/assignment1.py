import sqlite3
import os
db_path =os.path.join(r"C:\Users\Ronit Bhavsar\OneDrive\Desktop\skytusintern", "Company.db")
conn= sqlite3.connect(db_path)
cursor = conn.cursor()

print("\n===Employees earning more than average salary===")
cursor.execute("""
SELECT emp_name,salary from employees
WHERE salary > (Select AVG(salary)FROM employees)
""")
for emp_name , salary in cursor.fetchall():
    print(emp_name,":",salary)


print("\n ===Department with highest total salary===")
cursor.execute("""
SELECT d.dept_name, SUM(e.salary)as total_salary
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
GROUP BY d.dept_name
ORDER BY total_salary DESC
LIMIT 1
""")
for dept_name, total_salary in cursor.fetchall():
    print(dept_name,":",total_salary)


print("\n ===Display employee with second highest salary===")
cursor.execute("""
SELECT emp_name, salary FROM  employees
WHERE salary = (SELECT DISTINCT salary from employees ORDER BY salary DESC LIMIT 1 OFFSET 1)
 """)

emp=cursor.fetchone()
print(emp[0],":",emp[1])


print("\n ===Employee working in same department as 'Amit'===")
cursor.execute("""
SELECT emp_name, dept_id FROM employees
WHERE dept_id = (SELECT dept_id FROM employees WHERE emp_name = 'Amit')
""")
for emp_name, dept_id in cursor.fetchall():
    print(emp_name,":",dept_id)
