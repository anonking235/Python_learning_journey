#Challenge 1
# Create a tuple with your top 3 programming languages
# Unpack it into 3 variables
# Print each one

def fav_lang():
    return("Python", "C++", "Java")

fav1, fav2, fav3, = fav_lang()
print(fav1, fav2, fav3)



languages = ["Python", "Java", "C++"]
for i, lang in enumerate(languages):
    print(f"Position {i}: {lang}")
