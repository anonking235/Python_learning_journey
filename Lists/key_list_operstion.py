my_list = [1, 2, 3, 4, 5]

# Create
my_list = [1, 2, 3]

# Add
my_list.append(4)  # Add to end: [1, 2, 3, 4]
my_list.insert(0, 0)  # Insert at position: [0, 1, 2, 3, 4]

# Remove
my_list.pop()  # Remove last item
my_list.remove(2)  # Remove specific value

# Access
first = my_list[0]  # Get first item
last = my_list[-1]  # Get last item

# Loop
for item in my_list:
    print(item)

# Check length
length = len(my_list)

# Check if item exists
if 3 in my_list:
    print("3 is in the list")
