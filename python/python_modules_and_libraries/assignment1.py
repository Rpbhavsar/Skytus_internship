#Create a custom math module and import it in another file
import maths
print("-------------------")
print("Addition:",maths.add(4,5))
print("-------------------")
print("Substraction:",maths.sub(20,8))
print("-------------------")
print("Multiplication:",maths.mul(2,80))
print("-------------------")
print("Division:",maths.div(10,5))
print("-------------------")


#Create a module to perform string operations
import stroperations
text=input("Enter a string: ")
print("-------------------")
print("Reverse string:",stroperations.stringrev(text))          
print("-------------------")
print("Uppercase:",stroperations.strupper(text))
print("-------------------")
print("Lowercase:",stroperations.strlower(text))
print("-------------------")
print("Number of characters:",stroperations.strcount(text))
print("-------------------")


#Use random module to generate 5 random integers 
import random

for i in range (5):
    print(random.randint(1,1000))


#Use datetime module to display current date and time
import datetime

print("Current Date and time:",datetime.datetime.now())


#Use math module to find a factorial of a number
import math

num1=int(input("Enter a number: "))
result= math.factorial(num1)
print("The factorial is :",result)


#Create a package shapes with modules for circle and rectangle.
from shapes import circle
from shapes import rectangle

print("Area of circle:",circle.area(7))
print("Area of rectangle:",rectangle.area(5,10))


#Import multiple function from one module and use them

from maths import add,sub,mul,div

print("Addition:", add(10, 5))
print("Subtraction:", sub(10, 5))
print("Multiplication:", mul(10, 5))
print("Division:", div(10, 5))


#Write a program to shuffle a list using random module.

num=[1,2,3,4,5]

print("Original list:",num)

random.shuffle(num)
print("Shuffeled list:",num)


#Write a program to calculate the difference between two dates.

date1= datetime.date(2026,10,6)
date2= datetime.date(2025,10,6)

diff=date1-date2
print("Date1:",date1)
print("Date2:",date2)
print("Difference between dates:",diff)


#Use os module to list files in a directory.
import os

files=os.listdir(".")
print("Files and folders in the current directory:")

for file in files:
    print(file)