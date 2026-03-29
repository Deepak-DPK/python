"""Your Turn (Mini Exercise):

Write a class called StudentRecord:

Inside __init__(): take name and marks (make marks private using __)

Add methods:

set_marks(new_marks) → updates marks safely

get_marks() → returns marks

Try changing marks both:

Using the setter method

Directly (to see what happens)"""

class StudentRecord:
    def __init__(self,name,marks):
        self.name=name
        self.__marks=marks
    def set_marks(self,new_marks):
        self.__marks = new_marks
    def get_marks(self):
        print(f"Name: {self.name} marks : {self.__marks}")

stud1=StudentRecord("DEEPAK", 82)

stud1.get_marks()

print("after update marks ")

stud1.set_marks(93)
stud1.get_marks()