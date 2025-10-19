"""🧬 4️⃣ Hierarchical Inheritance

➡️ One Parent → Multiple Children

Example:
A Parent has two children: Son and Daughter"""

class Parent:
    def show_parent(self):
        print("This is Parent")

class Son(Parent):
    def show_son(self):
        print("This is Son")

class Daughter(Parent):
    def show_daughter(self):
        print("This is Daughter")

s = Son()
d = Daughter()

s.show_son()
s.show_parent()

d.show_daughter()
d.show_parent()

"""✅ Key idea:
Multiple child classes share one parent."""

#output flow 
"""
       Parent
       /    \
   Son      Daughter

"""