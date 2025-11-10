#def get_user():
#    return ("Aryan", 24, "Delhi")

#name, age, city = get_user()
#print(name, age, city)

# Example 1: Returning multiple values
def get_user():
    return ("Aryan", 24, "Delhi")  # Tuple

name, age, city = get_user()
print(name, age, city)

####################

#user_scores = {
#    ("Aryan", "Python"):85,
#    ("Alice", "Java"):80
#}
#print(user_scores[("Aryan", "Python")])


# Example 2: Tuple in a dictionary (key must be immutable)
user_scores = {
    ("Aryan", "Python"): 85,  # Tuple as key
    ("Alice", "Java"): 92
}
print(user_scores[("Aryan", "Python")])  # Access using tuple


#############################
#point = (10, 20)

#x, y = point
#print(f"X: {x}, and Y:{y}")


# Example 3: Unpacking
point = (10, 20)
x, y = point
print(f"X: {x}, Y: {y}")



