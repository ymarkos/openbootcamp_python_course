class Vehicle:
    def __init__(self, color, wheel, doors):
        self.color = color
        self.wheel = wheel
        self.doors = doors

class Car(Vehicle):
    def __init__(self, color, wheel, doors, speed, cylinder):
        super().__init__(color, wheel, doors)
        self.speed = speed
        self.cylinder = cylinder


c = Car("black", 4, 2, 160, 200)
print(f"The speed is: {c.speed}")
print(f"The cylinder is: {c.cylinder}")
print(f"The color is: {c.color}")


