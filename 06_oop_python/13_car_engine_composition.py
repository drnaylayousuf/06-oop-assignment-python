# Create a class Engine
class Engine:
    def start(self):
        return "Engine started!"

# Create a class Car that uses composition (Car has an Engine)
class Car:
    def __init__(self, engine):
        self.engine = engine  # Engine object is passed to Car

    def start_car(self):
        return self.engine.start()  # Calling Engine's start method via Car

engine = Engine()

car = Car(engine)


print(car.start_car())  # Accessing Engine's method through Car
