#Write a program to handle division by zero error
try:
    num1=float(input("Enter 1st number:"))
    num2=float(input("Enter 2nd number:"))

    div=num1/num2

    print("Result:",div)
except ZeroDivisionError:
    print("Cannot divisible by zero")


#Write a program to handle invalid integer input
try:
    num1=int(input("Enter 1st number:"))
    num2=int(input("Enter 2nd number:"))

    sum= num1+num2
    print("sum",sum)
except ValueError:
    print("Enter a valid input")


#Write a program to open the file and handle the "file not found" error
try:
    file = open("data.txt", "r")
    content = file.read()
    print(content)
    file.close()

except FileNotFoundError:
    print("Error: File not found.")


#Write a program to demonstrate multiple exception blocks
try:
    num1=int(input("Enter 1st integer:"))
    num2=int(input("Enter 2nd integer:"))

    result= num1/num2
    print("Result:",result)
except ZeroDivisionError:
    print("Value should not be zero")
except ValueError:
    print("Enter a valid value")
except Exception:
    print("Something went wrong")


#Write a program to use finally for resource cleanup
try:
    num1=int(input("Enter 1st integer:"))
    num2=int(input("Enter 2nd integer:"))

    result= num1/num2
    print("Result:",result)
except ZeroDivisionError:
    print("Value should not be zero")
finally:
    print("It will always execute at the End of a program")


#Write a program to create a custom exception for invalid age (<18).
class InvalidAgeError(Exception):
    pass

try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise InvalidAgeError("Age must be 18 or above.")

    print("You are eligible.")

except InvalidAgeError as e:
    print("Error:", e)


#Write a program to handle IndexError when accessing a list.
try:
    lst=[1,2,3,4,5]
    index=int(input("Enter Index:"))

    print("Value:",lst[index])
except IndexError:
    print("Index not found out of range.")


#Write a program that takes two numbers and handles all possible errors.

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2
    print("Result:", result)

except ValueError:
    print("Error: Please enter valid numbers.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except Exception:
    print("Error: Something went wrong.")

#Write a program to log errors to a file instead of printing them.
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2
    print("Result:", result)

except ValueError as e:
    with open("error.log", "a") as file:
        file.write("ValueError: " + str(e) + "\n")

except ZeroDivisionError as e:
    with open("error.log", "a") as file:
        file.write("ZeroDivisionError: " + str(e) + "\n")


#Write a program that validates an email format and raises an exception for invalid ones.
class InvalidEmailError(Exception):
    pass


try:
    email = input("Enter your email: ")

    if "@" not in email or "." not in email:
        raise InvalidEmailError("Invalid email format.")

    print("Valid email.")

except InvalidEmailError as e:
    print("Error:", e)