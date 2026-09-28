import sqlite3
import os

base_path = os.path.dirname(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)
db_path = os.path.join(base_path, "Students.db")

connection = sqlite3.connect(db_path)
cursor = connection.cursor()
# 1. Count total number of students
print("\n ===Total Students===")
cursor.execute("""
SELECT COUNT(*)
From students """)

totalstd= cursor.fetchone()[0]
print("Total students:",totalstd)


# 2. Find average marks of students
print("\n ===Average Marks===")
cursor.execute("""
Select AVG(marks)
From students """)

avg=cursor.fetchone()[0]
print("average marks:",avg)


# 3. Find highest and lowest marks
print("\n ===Highest & Lowest marks===")
cursor.execute("""
Select MAX(marks), MIN(marks) 
From students""")

max_marks , min_marks=cursor.fetchone()
print("Highest marks:",max_marks)
print("Lowest marks:",min_marks)


# 4. Find department wise average marks
print("\n ===Department Wise average marks===")
cursor.execute("""Select department,
AVG(marks) From students
GROUP BY department
 """)


for department, average in cursor.fetchall():
    print(department,":",average)


# 5. Display departments where avg marks > 70
print("\n ==== Departments with Average Marks > 70 ====")
cursor.execute("""SELECT
department , AVG(marks) FROM students
GROUP BY department
HAVING AVG(marks)>70
 """)

for department, average in cursor.fetchall():
    print(department,":",average)
connection.close()