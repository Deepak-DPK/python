#Types of methods in python 

# There are 3 types
#    1.Instance method (self)
"""🧠 These work on individual objects.
They can access and modify instance variables using self."""


class Student:
    def __init__(self, name, marks):  # works with self (object data)
        self.name = name
        self.marks = marks
    
    def display(self):  # instance method
        print(f"{self.name} has {self.marks} marks")


"-------------------------------------------------------------"

#    2.class method   keyword : @classmethod (cls)
"""🧠 These work on the class itself, not on individual objects.
They use a special keyword: @classmethod
and take a parameter cls (refers to the class)."""

# works with class variables
class Student:
    school_name = "Sunshine School"

    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name



"--------------------------------------------------------------------"
#    3.static method  keyword : @staticmethod 
"""🧠 These dont depend on the class or object data.
They Are just utility methods inside the class (for organization).
They dont take self or cls."""

class Student:
    @staticmethod               # performs a general task
    def welcome_message():
        print("Welcome to the School Management System!")


