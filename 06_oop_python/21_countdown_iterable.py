# Create class Countdown
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self  # Iterable is the object itself

    def __next__(self):
        if self.current < 0:
            raise StopIteration  # Stop when below 0
        num = self.current
        self.current -= 1
        return num

# Use the iterable in a for-loop
for number in Countdown(5):
    print(number)
