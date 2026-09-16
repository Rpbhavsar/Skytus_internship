import csv
#Write a program to read a file and display its contents
file = open("data.txt", "r")

content = file.read()

print(content)
file.close()


#Write a program to count the number of lines in a file
file = open("data.txt", "r")

lines = file.readlines()

print("Number of lines:", len(lines))
file.close()


#Write a program to count how many times each word appears in a file.
file = open("data.txt", "r")

text = file.read()

words = text.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word Frequency:")

for word, count in word_count.items():
    print(word, ":", count)

file.close()


#Write a program to write 5 user entered sentences to the file
file = open("data.txt", "w")

for i in range(5):
    sentence = input("Enter a sentence: ")
    file.write(sentence + "\n")

file.close()
print("5 sentences written to the file successfully.")


#Write a program to append a list of string to an existing file
file = open("data.txt","a")

str=["Hello","python","file","handling","program"]

for string in str:
    file.write(string +"\n")
file.close
print("String append successfully")


#Write a program to read a file and print only lines containing a specific word.
file = open("data.txt", "r")

word = input("Enter the word to search: ")

for line in file:
    if word in line:
        print(line, end="")

file.close()


#Write a program to replace a specific word in a file and save changes
file = open("data.txt","r")

content = file.read()
file.close

word_to_change = input("Enter the word to replace:")
new_word = input("Enter a new word:")
content = content.replace(word_to_change,new_word)

file = open("data.txt", "w")
file.write(content)
file.close()
print("Word replaced successfully.")


#Write a program to merge the contents of two text files into a third file.
file1 = open("data.txt", "r")
file2 = open("file2.txt", "r")

content1 = file1.read()
content2 = file2.read()

file1.close()
file2.close()

file3 = open("file3.txt", "w")
file3.write(content1)
file3.write("\n")
file3.write(content2)
file3.close()
print("Files merged successfully.")


#Write a program to read a CSV file and display its content in a formatted way.
file = open("data1.csv","r")

read = csv.reader(file)

for row in read:
    print("|".join(row))
file.close()


#Write a program to back up a file by copying its contents into another file.

file = open("data.txt", "r")

content = file.read()

file.close()

backup = open("data_backup.txt", "w")

backup.write(content)
backup.close()
print("File backed up successfully.")