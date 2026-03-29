"""
🚀 Next Challenge — Hierarchical Inheritance

Now lets see if you can build this structure 👇

Structure:

        Vehicle
        /     \
      Car     Bike


Task:

class Vehicle:

def start(self): → prints "Vehicle started"

class Car(Vehicle):

def show(self): → prints "Car is a 4-wheeler"

class Bike(Vehicle):

def show(self): → prints "Bike is a 2-wheeler"

Then:

Create one Car object and one Bike object

Call start() and show() on both
"""

class Vehicle:
    def start(self):
        print("Vehicle is Started")
class car(Vehicle):
    def show(self):
        print("Car is a 4-wheeler")
class Bike(Vehicle):
    def show(self):
        print("Bike is a 2-wheeler")

obj1=car()
obj2=Bike()

obj1.start()
obj1.show()

obj2.start()
obj2.show()