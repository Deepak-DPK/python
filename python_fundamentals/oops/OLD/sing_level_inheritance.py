"""🌳 1. Single Inheritance

➡️ One Parent → One Child

Example:
A Father has a property, and the Son inherits it."""


class Father:
    def show_father(self):
        print("This is Father class")

class Son(Father):
    def show_son(self):
        print("This is Son class")

obj = Son()
obj.show_son()
obj.show_father()   # inherited from Father


#✅ Key idea:
#Child inherits from only one parent.

#outputflow -----------------------------------------------------
"""
Father
  ↓
Son
"""