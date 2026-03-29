class Car:
    def __init__(self, brand, color):
        self.brand = brand        # instance variable
        self.color = color        # instance variable

    def show_details(self):
        print(f"This is a {self.color} {self.brand}")

# Create multiple car objects
car1 = Car("Tesla", "Red")
car2 = Car("BMW", "Blue")

car1.show_details()
car2.show_details()
