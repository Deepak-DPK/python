"""
💪 Next Challenge — Level 2: Multilevel Inheritance

Create this chain 👇

Class: LivingBeing

Method: breathe() → prints "All living beings breathe"

Class: Animal (inherits from LivingBeing)

Method: eat() → prints "Animals eat food"

Class: Human (inherits from Animal)

Method: think() → prints "Humans can think"

Task:
Create an object of Human and call all three methods:

breathe()

eat()

think()
"""

class LivingBeing:
    def breath(self):
        print("All living beings breathe")
class Animal(LivingBeing):
    def eat(self):
        print("Animals eat food ")
class Human(Animal):
    def think(self):
        print("Human can think")

obj1=Human()
obj1.breath()
obj1.eat()
obj1.think()