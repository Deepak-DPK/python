class student:
    def __init__(self,name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display_details(self):
        print("--------YOUR DETAILS--------------------")
        print(f"Name : {self.name}")
        print(f"Roll_number : {self.roll_number}")
        print(f"Marks : {self.marks}")
        print(f"Status : {self.check_pass_fail()}")

    def check_pass_fail(self):
        if self.marks >= 40:
            return "PASS"
        else:
            return "FAIL"

name = input("Enter your name: ").capitalize()
roll =int(input("Enter your Roll : "))
marks =int(input("Enter your makrs: "))

s1 = student(name,roll,marks)

s1.display_details()
