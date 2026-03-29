"""🤝 3 Multiple Inheritance

➡️ One Child inherits from more than one Parent.

Example:
A Student can be both a Sportsperson and a Scholar."""

class Sports:
    def show_sports(self):
        print("Plays Football")

class Academics:
    def show_academics(self):
        print("Topper in Science")

class Student(Sports, Academics):
    def show_student(self):
        print("This is Student")

obj = Student()
obj.show_student()
obj.show_sports()
obj.show_academics()


"""✅ Key idea:
Child can inherit features from multiple parent classes."""

#output flow ------------------------------------------------
"""
  Sports      Academics
     \          /
      \        /
        Student

"""#------------------------------------------------------------