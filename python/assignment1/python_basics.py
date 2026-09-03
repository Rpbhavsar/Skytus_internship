#this is a 1st python programe
print("Name : Ronit Bhavsar , Age : 21 , City : Valsad")


#this is a 2nd python programe
num1=int(input("Enter 1st number : "))
num2=int(input("Enter 2nd number : "))
sum=num1+num2
print("Sum of two number is : ",sum)


#this is a 3rd python programe (temperature conversion)
celsius=float(input("Enter temperature in Celsius : "))
fahrenheit=(celsius*9/5)+32
print("Temperature in Fahrenheit is : ",fahrenheit)


#this is a 4th python programe (store variable name print in uppercase)
name=input("Enter your name : ")
print("Your name in uppercase is : ",name.upper())


#this is a 5th python programe (calculate current age)
birthyear=int(input("Enter your birth year : "))
ongoingyear=int(input("Enter current year : "))
age=ongoingyear-birthyear
print("Your current age is : ",age)


#this is a 6th python programe (swap values of two variables)
num1=int(input("Enter 1st number : "))
num2=int(input("Enter 2nd number : "))
num1,num2=num2,num1
print("After swapping : num1 =",num1,"and num2 =",num2)


#this is a 7th python programe (calculate area of rectangle)
length=float(input("Enter length of rectangle : "))
width=float(input("Enter width of rectangle : "))
arearect=length*width
print("Area of rectangle is : ",arearect)


#this is a 8th python programe (check if the number is positive or negative)
num=int(input("Enter a number : "))
if num>0:
    print("The number is positive.")
elif num<0:
    print("The number is negative.")


#this is a 9th python programe (average of two numbers)
num1=float(input("Enter 1st number : "))
num2=float(input("Enter 2nd number : "))
average=(num1+num2)/2
print("Average of two numbers is : ",average)