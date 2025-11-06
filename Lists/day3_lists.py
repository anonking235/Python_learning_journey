# List Example 1: Creating and accessing
fruits = ["apple", "banana", "orange", "mango"]
print(fruits)  # What prints?

#I predict that it would print all the elements of the list "fruits"
#it did

# Access individual items (remember: indexing starts at 0)
print(fruits[0])  # What's at position 0?
print(fruits[1])
print(fruits[-1])  # What does negative index mean? Predict!

#I predict that [0] would print apple, [1] would print banana and [-1] would print mango.
#I was right.

# List Example 2: Adding and removing
my_list = ["Python", "JavaScript", "Go"]
print(my_list)

my_list.append("Rust")  # Add to end
print(my_list)

my_list.remove("JavaScript")  # Remove specific item
print(my_list)

#first print would print the main list - python, javascript and go.
# second print would add Rust at the end of list and print updated list.
# and third print would remove javascript from the list and would print the updated list.
#It did.

# List Example 3: Length and looping
numbers = [10, 20, 30, 40, 50]
print(f"List has {len(numbers)} items")

# Loop through list
for num in numbers:
    print(f"Number: {num}")

#I predict that the first print would print the number of items in the list with the text List has 5 items.
# and the second print would print all the items from the list with "Number:" text added before them.
#I was right again.

# List Example 4: List of lists (nested)
student_data = [
    ["Aryan", 24, "Delhi"],
    ["Alice", 23, "Mumbai"],
    ["Bob", 25, "Bangalore"]
]

# Access nested data
print(student_data[0])  # First student
print(student_data[0][0])  # First student's name
print(student_data[1][2])  # Second student's city

#I predict that the first print would print all the data related to the first student.
# second print would print the first index inside the first studentes nested list.
# and third print would access and print second student's city.

# List Example 5: List methods (useful tools)
scores = [85, 92, 78, 95, 88]

print(f"Highest score: {max(scores)}")
print(f"Lowest score: {min(scores)}")
print(f"Average score: {sum(scores) / len(scores)}")

sorted_scores = sorted(scores)
print(f"Sorted: {sorted_scores}")

# First print would print the highest number from the list and that is 95.
#second print would print the lowest score from the list and that is 78.
# third print would first add all the numbers in the list and then divide by the total number of items in list and then print that data.

# forgot about the sorted one and ran the program, but ok, the sorted statement sorts the numbers in list in order.


