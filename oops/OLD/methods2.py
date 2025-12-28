class student:
    school_name = "Islmiah Higher seconary school"

    def __init__(self, name , grade):
        self.name = name
        self.grade=grade

    def stud_details(self):
        print(f"STUDENT NAME: {self.name} , GRADE : {self.grade} , SCHOOL NAME: {student.school_name} ")

    @classmethod
    def change_schl_name(cls,newname):
        cls.school_name = newname
    
    @staticmethod
    def greet():
        print("Welcome to our School students")

stud1=student("DEVA",12)
stud2=student("linga",13)

student.greet()

stud1.stud_details()
stud2.stud_details()

print("------------------------------------------------------------------------------------------------")

student.change_schl_name("VIDHYALAKSHMI HIGHER SECONDARY SCHOOL")

stud1.stud_details()
stud2.stud_details()