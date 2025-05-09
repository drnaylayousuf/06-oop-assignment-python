class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("student name:",self.name)
        print("student marks:",self.marks)

student1 = Student("ali",85)

student1.display()


