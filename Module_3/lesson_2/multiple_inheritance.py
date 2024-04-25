class Vehicle:
    def __init__(self):
        print(self.__class__.__name__)

    def move(self):
        print("bacbacbacbabc")


class Car(Vehicle):
    def drive(self):
        print("I am driving")

    def move(self):
        super().move()
        print("Go on the surface")


class Boat(Vehicle):
    def swim(self):
        print("I am swimming")

    def move(self):
        super().move()
        print("Go on water")


class Amphibian(Boat, Car):
    pass

    __mro__ = (Car, Boat, Vehicle)


car_1 = Car()
car_1.drive()

boat_1 = Boat()
boat_1.swim()

amphibian_1 = Amphibian()
amphibian_1.drive()
amphibian_1.swim()

amphibian_1.move()

"""
MRO - method resolution order
"""

print()
print(Amphibian.__mro__)