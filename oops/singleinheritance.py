#inheritaNCE 

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


g1=grandpa("thatha",55)
d1=dad("appa",39)

d1.dad_det()
g1.grandpa_det()