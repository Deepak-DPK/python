"""🪜 2 Multilevel Inheritance

 Like a family chain — Grandpa → Father → Son"""

class Grandpa:
    def show_grandpa(self):
        print("This is Grandpa")

class Father(Grandpa):
    def show_father(self):
        print("This is Father")

class Son(Father):
    def show_son(self):
        print("This is Son")

obj = Son()
obj.show_son()
obj.show_father()
obj.show_grandpa()


"""✅ Key idea:
Child (Son) inherits from Father, who already inherits from Grandpa.
So Son gets everything from both!"""


#output flow ---------------------------------------------------------
"""
Grandpa
   ↓
Father
   ↓
Son

"""