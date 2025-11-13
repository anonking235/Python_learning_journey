class Products:
    def __init__(self, name, price, rating):
        self.name = name
        self.price = price
        self.rating = rating

    def summary(self):
        return (f"Products: {self.name} - ${self.price} (Rating: {self.rating})")

product1 = Products("HP", 50000, 4.5)
product2 = Products("Apple", 80000, 5)

print(product1.summary())
print(product2.summary())