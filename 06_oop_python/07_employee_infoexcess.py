
class Employee:
    def __init__(self):
        self.name = "John"           # Public variable
        self._salary = 50000         # Protected variable
        self.__ssn = "123-45-6789"   # Private variable

emp = Employee()

print("Name:", emp.name)  # ✅ Works fine

print("Salary:", emp._salary)  # ⚠️ Works, but by convention should not be accessed outside the class

try:
    print("SSN:", emp.__ssn)  # ❌ Will raise an AttributeError
except AttributeError:
    print("Private attribute cannot be accessed directly.")

print("SSN (using name mangling):", emp._Employee__ssn)  # ✅ Works, but not recommended

