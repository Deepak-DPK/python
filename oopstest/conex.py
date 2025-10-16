"""
🧩 Write your own program with the following:

Class name: Student

Inside __init__(), take two parameters: name and grade

Create a method display_info() that prints something like:
"Student Name: Deepak, Grade: 12"

Create two student objects with different names and grades.

Call display_info() for both."""

class student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
    def display_info(self):
        print(f"Student Name: {self.name}, Grade : {self.grade}")

stud1=student("Deepak", 12)
stud2=student("Srinath",14)
stud3=student("Devi",12)

stud1.display_info()
stud2.display_info()
stud3.display_info()