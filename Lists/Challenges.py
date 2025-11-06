#Challenge 1
# Create a list of 5 programming languages you want to learn
# Print the first and last language
# Add one more language to the list
# Remove one language
# Print the final list
# (You write this)

lan = ["python", "java", "c++", "rust", "go"]
print(lan[0],lan[-1]) #here I could have printed them seprately but I printed them together and it's a funny name "Python go"

lan.append("Javascript")
print(lan)

lan.remove("go")
print(lan)
#Done

#Challenge 2
# Create a list of numbers: [10, 20, 30, 40, 50]
# Use a FOR loop to print each number multiplied by 2
# (You write this)

my_list = [10, 20, 30, 40, 50]

for item in my_list:
    item = item * 2
    print(item)

#Done

#Challenge 3
# Create a list of students with their scores:
# [["Aryan", 85], ["Alice", 92], ["Bob", 78]]
# Loop through and print: "Aryan scored 85"
# Then find the highest score and print who got it
# (You write this from scratch - think about logic first)

students = [["Aryan", 85],
            ["Alice", 92],
            ["Bob", 78]
            ]
for student in students:
    print(f"{student[0]} scored {student[1]}")

# Find highest
highest_student = max(students, key=lambda x: x[1])
print(f"Highest score: {highest_student[0]} with {highest_student[1]}")

#this was surely a difficult one.