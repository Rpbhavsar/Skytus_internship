#check if a person is eligible to vote (age>=18)
age = int(input("Enter Age:"))

if age>=18:
    print("The person is eligible to vote")
else:
    print("The person is not eligible to vote")


#Grade calculator based on marks
marks = int(input("Enter Marks: "))

if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
else:
    print("C")


#Simulate a traffic light
light = input("Enter traffic light color: ")

if light == "red":
    print("STOP")
elif light == "yellow":
    print("WAIT")
elif light == "green":
    print("GO")


# ATM withdrawal check: sufficient balance or not

balance = 5000
withdraw = int(input("Enter amount: "))

if withdraw <= balance:
    print("Withdrawal successful")
    balance = balance - withdraw
else:
    print("Insufficient balance")


#Check if a number is positive negative or zero
number=int(input("Enter a number:"))
if number > 0:
    print("It is positive")
elif number < 0:
    print("It is negative")
else:
    print("The number is zero")


#Check if a number lies within a given range
num = int(input("Enter a number: "))

if 10 <= num <= 50:
    print("Number lies within the range")
else:
    print("Number is outside the range")


#Username and password verification
username=input("Enter username:")
password=input("Enter password:")

if username=="Admin" and password=="Admin@123":
    print("Login successful")
else:
    print("login unsuccessful")


#Electricity bill calculator based on units consumed
units = float(input("Enter the units: "))

bill = units * 1.5
print("Electricity bill:", bill)


#Simple calculator add ,substract , multiply , divide
num1=int(input("Enter 1st number:"))
num2=int(input("Enter 2nd number:"))

operator=input("Enter operator(+,*,-,/):")

if operator=="+":
    print(num1+num2)
elif operator=="-":
    print(num1-num2)
elif operator=="*":
    print(num1*num2)
elif operator=="/":
    print(num1/num2)


#Check the type of triangle equilatera isosceles scalene
a=float(input("Enter 1st side:"))
b=float(input("Enter 2nd side:"))
c=float(input("Enter 3rd side:"))

if a == b and b == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")