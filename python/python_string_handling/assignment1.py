#Task 1 take a string input and print its length 
print("Task 1: Take a string input and print its length")
s = input("Enter a string: ")
print("length of the string is:", len(s))


#Task 2 take convert a sentence into lowercase
print("Task 2: Convert a sentence into lowercase")
a=input("Enter a sentence: ")
print("The sentence in lowercase:",a.lower())


#Task 3: Replace spaces with underscores in a string
print("Task 3: Replace spaces with underscores in a string")
b = input("Enter a string: ")
print("the string after replacing:",b.replace(" ","_"))


#Task 4: Extract the first and last character of a string
print("Task 4: Extract the first and last character of a string")
c = input("Enter a string: ")
print("The first character is:",c[0])
print("The last character is:",c[-1])


#Task 5 reverse a string using slicing
print("Task 5: Reverse a string using slicing")
d=input("Enter a string:")
print("Reversed string is:",d[::-1])


#Task 6 count how many times a letter appears in a string
print("Task 6: Count how many times a letter appears in a string")
e=input("Enter a string:")
f=input("Enter the letter to count:")
print("The letter appears",e.count(f),"times in the string.")


#Task 7 check if a word is present in a sentence
print("Task 7: Check if a word is present in a sentence")
g=input("Enter a sentence:")
h=input("Enter a word to check:")
print("Is the word present in the sentence?", h in g)


#Task 8 take name and age and print using f-string formatting
print("Task 8: Take name and age and print using f-string formatting")
name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"Name: {name}, Age: {age}")


#Task 9 remove extra space from the start and end of a string
print("Task 9: Remove extra space from the start and end of a string")
i=input("Enter a string with extra spaces: ")
print("String after removing extra spaces:", i.strip())


#Task 10 join a list of word into a single string with - between them
print("Task 10: Join a list of words into a single string with '-' between them")
words = input("Enter a list of words separated by spaces: ").split()
print("Joined string:", "-".join(words))