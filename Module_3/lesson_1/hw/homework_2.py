class Car:
    def __init__(self, car_id, car_info, price: int):
        self.info = car_info
        self.id = car_id
        self.price = price


class Dealership:
    def __init__(self):
        self.cars: dict[int, Car] = {}
        self.income = 0

    def add_car(self, car: Car):
        if car.id in self.cars:
            print("Car with this ID Already in the garage")
            return
        self.cars[car.id] = car

    def sell_car(self, car_id):
        sold_car = self.cars.pop(car_id)
        self.income += sold_car.price


dealership = Dealership()

car_1 = Car(1234534, "Mazda 3", 10000)
car_2 = Car(1234535, "Mazda 5", 15000)
car_3 = Car(1234536, "Mazda 6", 16000)

dealership.add_car(car_1)
dealership.add_car(car_2)
dealership.add_car(car_3)

print(dealership.cars)
print(dealership.income)

dealership.sell_car(1234536)
dealership.sell_car(1234535)

print(dealership.cars)
print(dealership.income)