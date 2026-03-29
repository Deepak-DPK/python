"""
🧩 Write your own program with the following:

Class name: Student

Inside __init__(), take two parameters: name and grade

Create a method display_info() that prints something like:
"Student Name: Deepak, Grade: 12"

Create two student objects with different names and grades.

Call display_info() for both."""


print("--------------------------------------------------------------------------------")
print("--------------------------------CONSTRUCTOR(__init__)---------------------------")
print("--------------------------------------------------------------------------------")

class student:
    school_name="Islamiah Higher secondary School"
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
    def display_info(self):
        print(f"Student Name: {self.name}, Grade : {self.grade} , School : {student.school_name}")

stud1=student("Deepak", 12)
stud2=student("Srinath",14)
stud3=student("Devi",12)

stud1.display_info()
stud2.display_info()
stud3.display_info()



print("--------------------------------------------------------------------------------")
print("-------------------------CLASS VS INSTANCE(variable)----------------------------")
print("--------------------------------------------------------------------------------")


""" 
🧩 Your Turn:

Create a class called Employee with:

A class variable company = "TechCorp"

In __init__(), take parameters: name and salary

A method show_details() that prints:
"Employee Name: <name>, Salary: <salary>, Company: TechCorp"

Create two employees and display their details."""

class Employee:
    company = "TechCorp"  #class variable
    def __init__(self, name ,salary):
        self.name = name        #instance variable
        self.salary = salary    #instance variable
    def show_details(self):
        print(f"Employee Name: {self.name}, Salary : {self.salary}, Company:{Employee.company}")

emp1=Employee("Sachin", 12000)
emp2=Employee("Dravid", 15000)

emp1.show_details()
emp2.show_details()