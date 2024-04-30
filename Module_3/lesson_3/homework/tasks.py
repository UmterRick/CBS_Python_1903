class Car:
    def __init__(self, vin_code, model, color, motor, running_distance):
        self.color = color
        self.motor = motor
        self.__model = model
        self.__vin_code = vin_code
        self.__running_distance = running_distance

    def get_vin_code(self):
        return self.__vin_code

    def set_vin_code(self):
        print("Not Available")

    def get_model(self):
        return self.__model

    def set_model(self):
        print("Not Available")


    def get_running_distance(self):
        return self.__running_distance


    def set_running_distance(self, new_value):
        self.__running_distance = new_value

    def start_engine(self):
        print("Vroom")

    def drive_km(self, distance):
        self.__running_distance += self.__km_to_miles(distance)

    def drive_miles(self, distance):
        self.__running_distance += distance

    def __km_to_miles(self, distance):
        return distance * 1.4



