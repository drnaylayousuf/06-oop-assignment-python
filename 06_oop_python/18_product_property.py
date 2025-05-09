# Create class Product
class Product:
    def __init__(self, price):
        self._price = price  # Private attribute

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @price.deleter
    def price(self):
        del self._price

# Create a Product object
p = Product(100)

# Get the price
print(p.price)

# Update the price
p.price = 150
print(p.price)

# Delete the price
del p.price
