class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(self.brand, "is starting")

car1 = Car("lamborghini")

print("car brand:", car1.brand)

car1.start()