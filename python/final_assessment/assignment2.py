#Quiz game
score = 0

print("----Quiz Game----")

print("\n 1. Which symbol is used for comments in python")
print("A. //")
print("B. <!-- -->")
print("C. #")
print("D. **")

answer = input("Enter your answer:")

if answer.lower() == "b":
    print("Correct")
    score= score+1
else:
    print("Wrong")

print("\n 2. Which loop is used to repeat while a condition is true?")
print("A. for")
print("B. while")
print("C. if")
print("D. switch")

answer = input("Enter your answer:")

if answer.lower()== "b":
    print("Correct")
    score=score+1
else:
    print("Wrong")

print("\ 3n. Which data type stores multiple values in a sequence?")
print("A. list")
print("B. int")
print("C. float")
print("D. bool")

answer= input("Enter your answer:")

if answer.lower()== "a":
    print("Correct")
    score=score+1
else:
    print("Wrong")


print("----Result----")
print("Your score is :",score,"/3")