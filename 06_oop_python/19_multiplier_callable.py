# Create class Multiplier
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number):
        return number * self.factor

# Create an object
m = Multiplier(5)

# Test with callable()
print(callable(m))  # Should print True

# Call the object like a function
print(m(10))  # 10 * 5 = 50
