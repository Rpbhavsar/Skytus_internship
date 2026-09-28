import sqlite3

connection = sqlite3.connect("Students.db")

cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    year INTEGER,
    marks INTEGER
)
""")

students = [
    (1, "Ronit", "CSE", 3, 96),
    (2, "Rahul", "IT", 2, 72),
    (3, "Priya", "CSE", 3, 91),
    (4, "Amit", "Mechanical", 4, 68),
    (5, "Neha", "CSE", 2, 79),
    (6, "Karan", "IT", 3, 95)
]

cursor.execute("DELETE FROM students")

cursor.executemany("""
INSERT INTO students
(student_id, name, department, year, marks)
VALUES (?, ?, ?, ?, ?)
""", students)

connection.commit()


# 1. Display all student records
print("\n==== All Students ====")

cursor.execute("SELECT * FROM students")

for student in cursor.fetchall():
    print(student)


# 2. Display only name and department
print("\n==== Name and Department ====")

cursor.execute("""
SELECT name, department
FROM students
""")

for student in cursor.fetchall():
    print(student)


# 3. Find students with marks greater than 75
print("\n==== Marks Greater Than 75 ====")

cursor.execute("""
SELECT *
FROM students
WHERE marks > 75
""")

for student in cursor.fetchall():
    print(student)


# 4. Display students from CSE department
print("\n==== CSE Students ====")

cursor.execute("""
SELECT *
FROM students
WHERE department = 'CSE'
""")

for student in cursor.fetchall():
    print(student)


# 5. Sort students by marks descending
print("\n==== Students Sorted By Marks ====")

cursor.execute("""
SELECT *
FROM students
ORDER BY marks DESC
""")

for student in cursor.fetchall():
    print(student)


# 6. Display top 3 scorers
print("\n==== Top 3 Scorers ====")

cursor.execute("""
SELECT *
FROM students
ORDER BY marks DESC
LIMIT 3
""")

for student in cursor.fetchall():
    print(student)
connection.close()