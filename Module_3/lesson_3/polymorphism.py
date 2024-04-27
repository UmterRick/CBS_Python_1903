"""

class int
    def __add__(self, other)
        return self + other

10(self) + 30(other)

x = 10 + 30 + 3
print(x)

y = "Hello" + " " + "World"
print(y)
"""


class Animal:
    legs = None

    def __init__(self, weight):
        self.weight = weight

    def talk(self):
        print("I dont know what to say...")

    def __add__(self, other):
        if not isinstance(other, Animal):
            print(f"You cant add {type(other)} to Animal")
        self.legs += other.legs
        return self

    def __lt__(self, other):
        return self.weight < other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __le__(self, other):
        return self.weight <= other.weight

    def __ge__(self, other):
        return self.weight >= other.weight


class Cat(Animal):
    legs = 4

    def talk(self):
        print("Meow")


class Dog(Animal):
    legs = 4

    def talk(self):
        print("Woof")


class Fish(Animal):
    legs = 0


d = (30)
c = Cat(6)
x = c + d
print(x)
print(x.legs)

print(d > c)
print(d < c)
