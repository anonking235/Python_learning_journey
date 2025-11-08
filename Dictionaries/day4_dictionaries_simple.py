#Real web scraper data

product = {
    "name": "Laptop",
    "price": 50000,
    "rating": 3.1,
    "in_stock": True
}

#Access by key label
print(product["name"])
print(product["price"])

#change a value

product.update({"price": "60000"})
print(product["price"])

#Add a new info
product.update({"country": "India"})
print(product)
#or
product["seller"] = "Amazon"
print(product["seller"])

#Chack is key exists
if "discount" in product:
    print(product["discount"])
else:
    print("key not exists")

#loop and print nicely
print("\n---- Product details ----")
for key in product:
    print(f"{key}: {product[key]}")


#Challenge for today
# You create this list of 3 products
# Each product has: name, price, rating, in_stock
# Example structure:
products = [
    {"name": "Laptop", "price": 50000, "rating": 4.5, "in_stock": True},
    {"name": "Laptop2", "price": 60000, "rating": 4.6, "in_stock": False},
    {"name": "laptop3", "price": 70000, "rating": 4.7, "in_stock": True}
    # Add 2 more products yourself
]

for product in products:
    print(f"{product['name']}- {product['price']} (Rating: {product['rating']})")

cheapest = min(products, key = lambda x: x['price'])
print(f"Cheapest: {cheapest['name']} at the price of $: {cheapest['price']}")

#def get_price(product):
#    return product["price"]

#cheapest = min(products, key = get_price)
#print(f"Cheapest: {cheapest['name']} at the price of ${cheapest['price']}")

#cheapest = min(products, key = lambda x: x["price"])
#print(f"Cheapest:{cheapest['name']} with the price of: {cheapest['price']}")







