# Create a class Employee
class Employee:
    def __init__(self, name):
        self.name = name

# Create a class Department that stores a reference to an Employee
class Department:
    def __init__(self, department_name, employee):
        self.department_name = department_name
        self.employee = employee  # Department has a reference to Employee

# Create an Employee object
employee1 = Employee("John Doe")

# Create a Department object, passing the Employee object to it
department1 = Department("IT", employee1)

# Print department and employee info
print(f"Department: {department1.department_name}, Employee: {department1.employee.name}")
