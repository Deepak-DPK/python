
class grandpa:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def grandpa_det(self):
        print(f"Grandpa name: {self.name} Grandpa Age: {self.age}")

class dad(grandpa):
     def __init__(self,name,age):
        self.name=name
        self.age=age
     def dad_det(self):
        print(f"dad name: {self.name} dad Age: {self.age}")

class son(dad):
     def __init__(self,name,age):
        self.name=name
        self.age=age
     def son_det(self):
        print(f"Son name: {self.name} son Age: {self.age}")

s1=son("Deepak",22)
d1=dad("Ramesh",53)
g1=grandpa("palani",84)

g1.grandpa_det()
d1.dad_det()
s1.son_det()

