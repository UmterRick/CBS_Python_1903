data = input("Type Name, age, height, weight, description with spaces: ").split()


# name, age, height, weight, description = data
# print(f"{name=}", f"{age=}", f"{height=}", f"{weight=}", f"{description=}")

match data:
    case name, age, height, weight, description:
        print(f"My name is {name}, I am {age} y.o. My params are {height} cm {weight} kg. I am {description}")
    case name, age, height, weight:
        print(f"My name is {name}, I am {age} y.o. My params are {height} cm {weight} kg.")
    case name, age, height:
        print(f"My name is {name}, I am {age} y.o. My params are {height} cm")
    case name, age:
        print(f"My name is {name}, I am {age} y.o.")
    case _:
        print("Incorrect data")

