class Animal:
    planet = "Earth"

    def __init__(self, animal_type, name, color):
        self.type = animal_type
        self.name = name
        self.color = color


cat = Animal("Cat", "Barsik", "ginger")
dog = Animal("Dog", "Tuzik", "black")

print("Barsik: ", cat.planet)
print("Tuzik: ", dog.planet)

cat.planet = "Mars"

print("Barsik: ", cat.planet)
print("Tuzik: ", dog.planet)

Animal.planet = "Jupiter"

print("Barsik: ", cat.planet)
print("Tuzik: ", dog.planet)

# Only one constructor method is possible
# class Person:
#
#     def __init__(self, name):
#         self.name = name
#
#     def __init__(self, name, sername):
#         self.name = name
#         self.sername = sername



