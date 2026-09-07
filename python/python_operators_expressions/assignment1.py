#This is 1st practical(calculate the remainder of two numbers)
num1=int(input("Enter 1st number:"))
num2=int(input("Enter 2nd number:"))

remainder=num1%num2
print("The remainder is:",remainder)


#This is 2nd practical(check if the number is even or odd)
num=int(input("Enter a number:"))
if num%2==0:
    print("It is even number")
else:
    print("It is odd number")


#This is 3rd practical(calculate two numbers and print the larger number)
num1=int(input("Enter 1st number:"))
num2=int(input("Enter 2nd number:"))
if num1>num2:
    print("The larger number is:",num1)
else:
    print("The larger number is:",num2)


#This is 4th practical(calculate the square and cube of a number)
num=int(input("Enter a number:"))
squre=num**2
cube=num**3
print("The square of the number is:",squre)
print("The cube of the number is:",cube)


#This is 5th practical(check if two numbers are equal or not)
num1=int(input("Enter 1st number:"))
num2=int(input("Enter 2nd number:"))
if num1==num2:
    print("Both numbers are equal")
else:
    print("Both numbers are not equal")


#This is 6th practical(take two numbers and print true if both are positive else print false)
num1=int(input("Enter 1st number:"))
num2=int(input("Enter 2nd number:"))
if num1>0 and num2>0:
    print("True")
else:
    print("False")


#This is 7th practical(convert float number to integer)
num=float(input("Enter a float number:"))
int_num=int(num)
print("The integer value is:",int_num)


#This is 8th practical(take a number as string and convert it into integer and multiply it by 10)
str=input("Enter a number as string:")
num=int(str)
result=num*10
print("The result after multiplying by 10 is:",result)


#This is 9th practical(programe that uses and & or operators to check multiple conditions)
num1=int(input("Enter 1st number:"))
num2=int(input("Enter 2nd number:"))
if num1>0 and num2>0:
    print("Both numbers are positive")
elif num1>0 or num2>0:
    print("Only one number is positive")
else:
    print("Neither number is positive")


#This is 10th practical(devide two numbers and print the quotient and remainder seperately)
num1=int(input("Enter 1st number:"))
num2=int(input("Enter 2nd number:"))
quotient=num1//num2
remainder=num1%num2
print("The quotient is:",quotient)
print("The remainder is:",remainder)