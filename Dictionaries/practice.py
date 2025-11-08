# Dictionary Example 1: Basic creation and access
person = {
    "name": "Aryan",
    "age": 24,
    "city": "Delhi",
    "job": "Learning Python"
}

print(person)  # What prints?
print(person["name"])  # What's at key "name"?
print(person["age"])

# First print would print the whole dict with all key values
# Second print would print the value of key "name"
# Third print would print the value of key "age" from dict

# Dictionary Example 2: Adding and modifying
person["country"] = "India"  # Add new key-value
print(person)

person["age"] = 25  # Modify existing
print(person)

# First print would add another key "Country" with value "India" in the dict "person"
# second print would modify the key value of "Age" from 24 to 25.

# Dictionary Example 3: Checking keys and looping
if "name" in person:
    print(f"Name exists: {person['name']}")

# Loop through keys
for key in person:
    print(f"{key}: {person[key]}")

# First print would check for the key name and if it exist then would print "Name exists: value"
# second print would print all the keys from dict person and iterate through them.

# Dictionary Example 4: Multiple dictionaries (list of dicts)
students = [
    {"name": "Aryan", "score": 85},
    {"name": "Alice", "score": 92},
    {"name": "Bob", "score": 78}
]

for student in students:
    print(f"{student['name']} scored {student['score']}")

#This print would iterate through all the dicts and would grab the name key value and score key value and print them as
# "Name scored score"

# Dictionary Example 5: Useful methods
my_dict = {"a": 1, "b": 2, "c": 3}

print(my_dict.keys())  # Get all keys
print(my_dict.values())  # Get all values
print(my_dict.items())  # Get key-value pairs

# Get value with default if key doesn't exist
print(my_dict.get("d", "Not found"))  # Returns "Not found" if "d" doesn't exist

#First print would print only keys from the dict.
#second print would print only the values from the dict
# and the third print would only print the pair of key and their values.
#last print would return "not found" becuase there is no "d" in our dict


