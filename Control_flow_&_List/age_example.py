age = int(input("How old are you? "))

if age >= 100:
    print("You are too old for this Grandpaa.")
elif age >= 18:
    print("You are eligible for credit card, please proceed.")
elif age <= 0:
    print("you haven't even born yet!")
else:
    print("You are not eligible for credit card.")

name = input("What is your name? ")

if name == "":
    print("You little bitch, you didn't typed your name.")
else:
    print(f"Hello {name}")