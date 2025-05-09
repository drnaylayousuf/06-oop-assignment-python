class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    def show_count(cls):
        print("total count:",cls.count)

c1 = Counter()
c2 = Counter()
c3 = Counter()

Counter.show_count(Counter)