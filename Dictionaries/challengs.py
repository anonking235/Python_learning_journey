#First challenge
# Create a dictionary for yourself:
# Keys: name, age, city, learning_language, goal
# Add values for each
# Print each key-value pair
# (You write this)

person = {"name": "Ultraa", "age": 25, "city": "Delhi", "learning_language": "Python", "Goal": "Learn Python"}
print(person)
#or
items = person.items()
print(items)

#Challenge 2
# Create a dictionary of tech tools you want to learn:
# {"tool": "Django", "difficulty": "medium", "priority": "high"}
# {"tool": "Docker", "difficulty": "hard", "priority": "high"}
# Create at least 3 tool dictionaries in a list
# Loop through and print: "Django - Difficulty: medium, Priority: high"
# (You write this)

tools = [
    {"tool": "Django", "difficulty": "medium", "priority": "high", "Progress": "20%"},
    {"tool": "Docker", "difficulty": "hard", "priority": "high", "Progress": "40%"},
    {"tool": "flask", "difficulty": "medium", "priority": "high", "Progress": "40%"},
]

for tool in tools:
    print(f"{tool['tool']} - Difficulty: {tool['difficulty']}, Priority: {tool['priority']}, Progress: {tool['Progress']}")

#Done

#Challenge 3
# Create a function that takes a student dictionary:
# {"name": "Aryan", "math": 85, "python": 92, "english": 78}
# The function should calculate the average score
# Return a new dictionary with name and average
# Example return: {"name": "Aryan", "average": 85}
# Test it with 2 different students
# (You write this from scratch)

def calculate_student_average(student):
    name = student["name"]
    scores = student["math"], student["python"], student["english"]
    average = sum(scores) / len(scores)
    return {"name": name, "average": average}

student1 = {"name": "Alice", "math": 85, "python": 92, "english": 78}
student2 = {"name": "Aryan", "math": 100, "python": 100, "english": 100}

result1 = calculate_student_average(student1)
result2 = calculate_student_average(student2)

print(result1)
print(result2)


