class Animal:
    @staticmethod
    def breathe():
        print("Inhale-Exhale")

    def eat(self):
        print("Eating Something...")


class Predator(Animal):
    def eat(self):
        print("Eating Meat!!!")


class Tiger(Predator):
    color = "orange/black"
    legs = 4
    is_tail = True

    def hide(self):
        print("You cant see me :)")



some_animal = Animal()
some_animal.breathe()
some_animal.eat()
print()
tiger = Predator()
tiger.breathe()
tiger.eat()
