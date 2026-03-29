"""
🏆 Next Challenge — Level 3: Multiple Inheritance

Create this scenario 👇

Class: Father

Method: skills() → prints "Father knows driving"

Class: Mother

Method: skills() → prints "Mother knows cooking"

Class: Child

Inherits from both Father and Mother

Method: skills() → prints "Child knows coding"

Task:

Create an object of Child

Call skills()

Then, using super(), also call one of the parent’s skills() inside the child’s method.
"""

class Father:
    def skills(self):
        print("Father knows driving")
class Mother:
    def skills(self):
        print("Mother knows cooking ")
class child(Father,Mother):
    def skills(self):
        print("Child knows coding")
        super().skills()

obj1=child()

obj1.skills()