#Function to check whether the number is prime or not
def _isprime_(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
        return True

num=int(input("Enter a number:"))
if _isprime_(num):
    print("It is a prime number")
else:
    print("Not a prime number")


#Function to reverse a string
def _strreverse_(str):
    return str[::-1]

str=input("Enter a string to reverse:")
print("Reversed string:",_strreverse_(str))


#Function to find a factorial
def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact

num = int(input("Enter a number: "))

print("Factorial:", factorial(num))


#Function to calculate simple interest
def simple_interest(p, r, t):
    si = (p * r * t) / 100
    return si

p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time: "))
print("Simple Interest:", simple_interest(p, r, t))


#Function to check if a word is palindrome or not
def palindrome (str):
    if str==str[::-1]:
        print("It is palindrome")
    else:
        print("Not a palindrome")
str=input("Enter a word:")
print(palindrome(str))


#Function to count vowels in a string
def vowels(str):
    count=0

    for char in str:
        if char in "aeiouAEIOU":
            count += 1
    return count
str=input("Enter a string:")
print("Vowels are:",vowels(str))


#Function to merge two list
def merge(l1,l2):
    return l1+l2
list1=[1,2,3]
list2=[4,5,6]
print("Merged List:",merge(list1,list2))


#Function to find gcd of two numbers
def find_gcd(a, b):
    while b:
        a, b = b, a % b

    return a

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("GCD:", find_gcd(num1, num2))


#Function to find area of rectangle
def area(w,h):
    return w*h

width=int(input("Enter width:"))
length=int(input("Enter Length:"))
print("Area of Rectangle:",area(width,length))    


#Function to check Armstrong number
def is_armstrong(n):
    original = n
    digits = 0
    temp = n

    while temp > 0:
        digits += 1
        temp = temp // 10

    total = 0
    temp = n

    while temp > 0:
        digit = temp % 10
        total = total + digit ** digits
        temp = temp // 10

    return total == original


num = int(input("Enter a number: "))

if is_armstrong(num):
    print("Armstrong number")
else:
    print("Not an Armstrong number")