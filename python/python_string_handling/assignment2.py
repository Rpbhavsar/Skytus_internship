#Task 11 create a list of your 5 favourit movies
print("Task 11: Create a list of your 5 favorite movies")
movies = ["horror", "action", "comedy", "drama", "thriller"]
print("Your favorite movies are:", movies)


#Task 12 add a new movie to the list 
new_movie = input("Enter a new movie to add to the list: ")
movies.append(new_movie)
print("Updated list of favorite movies:", movies)


#Task 13 remove the first movie from the list
print("Task 13: Remove the first movie from the list")
movies=["horror", "action", "comedy", "drama", "thriller"]
movies.pop(0)
print("List after removing the first movie:", movies)


#Task 14 sort a list of number in ascending order
print("Task 14: Sort a list of numbers in ascending order")
numbers = [5, 2, 9, 1, 5, 6]
numbers.sort()
print("Sorted list of numbers in ascending order:", numbers)


#Task 15 reverse a list 
print("Task 15: Reverse a list")
numbers = [5, 2, 9, 1, 5, 6]
numbers.reverse()
print("Reversed list of numbers:", numbers)


#Task 16 find the largest number in the list 
print("Task 16: Find the largest number in the list")
numbers = [5, 2, 9, 1, 5, 6]
largest = max(numbers)
print("The largest number in the list is:", largest)


#Task 17 merge two list into one
print("Task 17: Merge two lists into one")
list1 = [1,2,3]
list2 = [10,11,12]
merged_list = list1 + list2
print("Merged list :", merged_list)


#Task 18 access the last element of a list without using index number
print("Task 18: Access the last element of a list without using index number")
numbers = [5, 2, 9, 1, 5, 6]
last_element = numbers[-1]
print("The last element of the list is:", last_element)


#Task 19 create a nested list and access a specific inner element from it
print("Task 19: Create a nested list and access a specific inner element from it")
nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
specific_element = nested[1][2]
print("The specific inner element is:", specific_element)


#Task 20 count how many times an element appears in a list
print("Task 20: Count how many times an element appears in a list")
num = [1, 2, 3, 1, 4, 1, 5]
letter_to_count = int(input("Enter the number to count: "))
count = num.count(letter_to_count)
print(f"The number {letter_to_count} appears {count} times in the list.")