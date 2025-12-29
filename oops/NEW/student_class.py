class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old")

s1=student('SURYA',22)
s2=student('VIJAY',33)

s1.introduce()
s2.introduce()
