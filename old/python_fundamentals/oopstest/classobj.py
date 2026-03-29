"""
🧩 Mini Exercise:

writing a Python program using class object concept👇

Task:

Create a class called Car

Give it one attribute brand with value "Tesla"

Give it one method drive() that prints "The car is moving"

Create an object of the class and call both the attribute and method. """


class car:
    brand = "Tesla"

    def drive(self):
        print("The car is moving")

car1=car()

print(car1.brand)
car1.drive()
