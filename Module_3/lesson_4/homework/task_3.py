import random


class Worker:
    def __init__(self, name, surname, department, year):
        self.validate_name(name)
        self.validate_name(surname)
        self.validate_year(year)

        self.name = name
        self.surname = surname
        self.department = department
        self.year = year

    def __repr__(self):
        return f"'{self.surname} {self.name}' {self.department} ({self.year})"

    @staticmethod
    def validate_name(name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if not name.isascii():
            raise ValueError("Name cant contain numbers and special symbols")

    @staticmethod
    def validate_year(year):
        if not isinstance(year, int):
            raise ValueError("Year must be a integer")
        if 3000 < year < 1000:
            raise ValueError("Please provide valid information")


name = "Worker"
surname = "Surname"
department = "Managment"
possible_years = list(range(2010, 2024))


workers = []
for i in range(10):
    current_name = name + f"-{chr(70 + i)}"
    print(current_name)
    year = random.choice(possible_years)
    workers.append(Worker(current_name, surname, department, year))

print(workers)

new_workers = list(filter(lambda w: w.year > 2017, workers))

print(new_workers)