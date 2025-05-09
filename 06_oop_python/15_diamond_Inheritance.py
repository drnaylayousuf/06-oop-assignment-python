# Create class A
class A:
    def show(self):
        print("Method from class A")

# Create class B that inherits from A and overrides show()
class B(A):
    def show(self):
        print("Method from class B")

# Create class C that inherits from A and overrides show()
class C(A):
    def show(self):
        print("Method from class C")

# Create class D that inherits from both B and C
class D(B, C):
    pass  # No need to override show(), MRO will determine the method

# Create an object of D
obj = D()

# Call show() method
obj.show()  # MRO will determine which show() method to call
