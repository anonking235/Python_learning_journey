# Function Example 1: Simple greeting
def greet(name):
    print(f"Hello, {name}!")


# I predict that it would return nothing because we haven't called the function yet but if we assume that we called the
# function and gave a input for the parameter name like "Aryan" then it would return "Hello, Aryan!"

#I ran the program and as I predicted it didn't return anything, now I'm gonna call this function and gonna give a input to the parameter.

greet("Aryan")
# As I said it returned "Hello, Aryan!"

# Oh I forgot to check this part of the code
# Call the function
greet("Aryan")
greet("Alice")
greet("Bob")


# ok ok
#this function basically takes the input of the parameter name when it's called and run the function's code block by filling that value and return the output
#on to the next one.

# Function Example 2: With math
def add_numbers(a, b):
    result = a + b
    return result  # This sends the result BACK to whoever called the function


answer = add_numbers(5, 3)
print(f"5 + 3 = {answer}")


#print("---")

# I predict that it would return "5 + 3 = 8
# I was right.
#This function bascially takes the input for a and b parameter and then add those numbers and return the value to fucntion
# and then send the value of fucntion to answer variable and procced to use the value of variable "answer"in next print.
# on to the next one.

# Function Example 3: Multiple parameters
def create_profile(name, age, city):
    profile = f"{name} is {age} years old and lives in {city}"
    return profile


profile1 = create_profile("Aryan", 24, "Delhi")
print(profile1)


#print("---")
# I predict that when we call this function first it would take the input from "profile1" and then go to "profile" and place that data there
# and return that data to "create_profile" and that would return to print part and would return as "Aryan is 24 years old and lives in Delhi.
# I ran and was correct again.
#This function bascially takes the input for parameter and run the code block in function and return the value (or statement "Aryan is 24 years old and lives in delhi"
# and return the value in profile1 variable and that is printed in next line.
# On to the next one

# Function Example 4: No parameters, no return
def show_motivation():
    print("You're doing great! Keep going!")


show_motivation()
show_motivation()


# I predict that it would return "You're doing great! Keep going!" 2 times.
# again I was right .
#This function basically is being called two times and each time it prints the code block in the function.

#If I would call these functions multiple time then it would print the output multiple times.

# Next

def greet_with_print(name):
    print(f"Hello, {name}!")  # Just prints, doesn't send back


def greet_with_return(name):
    return f"Hello, {name}!"  # Sends the value back


# With print:
greet_with_print("Aryan")  # Prints, but you can't store it

# With return:
message = greet_with_return("Aryan")  # You CAPTURE the result
print(message)  # Now you can use it


#Tbh it's a bit hard to think of the instances where I would like to use print or return, I do understand the differences tho.

#Challenge 1
# Create a function called "multiply"
# It takes two numbers as parameters
# It returns the product (result of multiplication)
# Call it with 4 and 5, store the result, and print it
# (You write this from scratch)

def multiply(a, b):
    result = a * b
    return result


result = multiply(4, 5)
print(result)


# done

#Challenge 2
# Create a function called "check_age"
# It takes age as a parameter
# If age >= 18, return "You can vote"
# Else, return "You're too young to vote"
# Call it twice with different ages
# (You write this from scratch)

def check_age(age):
    if age >= 18:
        return "You can vote"
    else:
        return "You are too young to vote."


age = check_age(13)
print(age)


#did with 2 different age - 25 and 13 and it works perfectly.

#Challenge 3
# Create a function called "calculate_study_hours"
# It takes daily_hours and num_days as parameters
# It calculates total study hours
# It returns a formatted message: "You will study X hours in Y days"
# Call it with your real numbers (5 hours/day for 30 days)
# (You write this from scratch)

def calculate_study_hours(daily_hours, num_days):
    study_hours = daily_hours * num_days
    return (f"You will study {study_hours} hours in {num_days} days.")


study_hours = calculate_study_hours(5, 5)
print(study_hours)


#Done


# Create two functions:

# 1. calculate_monthly_income(daily_rate, days_worked)
#    Should RETURN total monthly income
#    (don't print)

# 2. calculate_taxes(income)
#    Should RETURN taxes (assume 10% tax)
#    (don't print)

# 3. In main code, call both functions in sequence:
#    - Calculate monthly income with daily_rate=500, days_worked=20
#    - Use that RESULT to calculate taxes
#    - Print final result: "Monthly income: X, Taxes: Y"

# The key: You MUST use return, because you need the result from
# the first function to use in the second function.
# If you used print, the second function couldn't see the result.

def calculate_monthly_income(daily_rate, days_worked):
    total = daily_rate * days_worked
    return total

def calculate_taxes(income):
    taxes = income * .10
    return taxes

total = calculate_monthly_income(500, 20)
taxes = calculate_taxes(total)

print(f"Your total monthly income is ${total} and your total taxes is: {taxes}")