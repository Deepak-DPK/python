"""
💡 Exercise 1 — Single Inheritance (Warm-up)

Create two classes:

Class: Animal

Has a method sound() that prints "Animals make sounds".

Class: Dog

Inherits from Animal

Adds its own method bark() that prints "Dog barks loudly"

Task:

Create an object of Dog

Call both bark() and sound() methods
"""

class Animal:
    def sound(self):
        print("Animals make sounds")
class dog(Animal):
    def bark(self):
        print("Dog barks Loudly")

ob1=dog()

ob1.sound()
ob1.bark()