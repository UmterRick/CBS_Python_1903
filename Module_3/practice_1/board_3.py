# aggregation and composition
class First:
    def __init__(self, second_class_obj):
        self.smth = second_class_obj


class AnotherFirst:
    def __init__(self, second_class_data):
        self.smth = Second(second_class_data)


class Second:
    def __init__(self, data):
        self.data = data


second_obj = Second("dnaskdas")
first_obj = First(second_obj)

another_first_obj = First("dnaskdas")


class Apartment:
    def __init__(self, bedrooms: int, area, height, design):
        self.bedrooms = bedrooms
        self.area = area
        self.height = height
        self.design = design

    def __repr__(self):
        return f"Apartment {self.bedrooms} ({self.area} m^2) - {self.design}"


class Building:
    def __init__(self):
        self.apartments = []

    def build_apartment(self, **apartment_data):
        new_apart = Apartment(**apartment_data)
        self.apartments.append(new_apart)


house = Building()
house.build_apartment(bedrooms=2, area=50, height=2.5, design="Retro")

print(house.apartments)
del house


class Engine:
    def __init__(self, num_of_power: int):
        self.cylinders = num_of_power

    def __repr__(self):
        return f"Engine V{self.cylinders}"

class Car:

    def __init__(self, model: str, motor: Engine):
        self.model = model
        self.motor = motor


new_engine = Engine(4)
print(new_engine)
new_car = Car("PythonCar", new_engine)

del new_car
print(new_engine)
new_car = Car("PythonCar2", new_engine)
print(new_engine)



