"""🧩 5️⃣ Hybrid Inheritance

➡️ Combination of two or more types of inheritance."""

class Grandpa:
    def show_grandpa(self):
        print("Grandpa traits")

class Father(Grandpa):
    def show_father(self):
        print("Father traits")

class Mother:
    def show_mother(self):
        print("Mother traits")

class Son(Father, Mother):
    def show_son(self):
        print("Son traits")

obj = Son()
obj.show_son()
obj.show_father()
obj.show_grandpa()
obj.show_mother()

"""✅ Key idea:
A mix of multilevel + multiple inheritance."""

#-------------------------------------------------
#output flow
"""
Grandpa
  ↓
Father
  ↘
   Son
   ↑
  Mother
"""
#-------------------------------------------------