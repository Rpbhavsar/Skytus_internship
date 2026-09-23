#print numbers from 1 to 10
for i in range(10):
    print(i+1)


#Display multiplication table for a given number
n=int(input("Enter a number:"))

for i in range(1,11):
    print(n ,"x",i,"=",n*i)


#Find factorial of a number
num=int(input("Enter a number:"))
factorial=1

for i in range(1,num+1):
    factorial=factorial*i

print("Factorial is:",factorial)


#Generate the first n fibonacci numbers
num1= int(input("Enter a fibonacci number :"))

a=0
b=1

for i in range(num1):
    print(a,end=" ")
    a,b=b,a+b
print()


#Check if a number is prime
num2=int(input("Enter a number:"))

if num2<=1:
    print("It is not a prime number")
else:
    for i in range(2,num2):
        if num2%i ==0:
            print("Not a prime number")
            break
    else:
        print("It is a prime number")


#Reverse a number
num=int(input("Enter a number:"))
rev = 0

while num>0:
    digit = num % 10
    rev = rev * 10+digit
    num = num//10
print("Reverse is :",rev)


#Count digits in a number
num=int(input("Enter a number:"))
count=0

while num>0:
    num=num//10
    count = count+1
print("Number of digits:",count)


#Find sum of even numbers between 1-100
sum=0
for i in range(1,101):
    if i % 2==0:
        sum=sum+i
print("Sum of even numbres: ",sum)


#Print a pyramid pattern

for i in range(1, 6):
    for j in range(5-i):
        print(" ",end=" ")

    for j in range(2*i-1):
        print("*",end=" ")
    print()


#Find all divisiors of a number
num=int(input("Enter a number:"))

print("Divisiors are:")
for i in range (1,num+1):
    if num % i == 0:
        print(i,end=" ")