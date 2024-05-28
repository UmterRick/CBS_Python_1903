calculate_formula = lambda a, b, c: a ** 2 - b + c / 3
print(calculate_formula)
result = calculate_formula(2, 3, 6)
print(result)

list_def = []
for i in range(10):
    x = lambda a, b: a + b - i
    result = x(1, 2)
    list_def.append(x)


def some_func_1():
    print("Meow")


def some_func_2():
    print("Woof")


def talk(func, *args):
    print(f"Lets launch func from arg: {func.__name__}")
    if args:
        func(*args)
    else:
        func()


def choose_animal(number):
    if number == 1:
        return some_func_1
    return some_func_2


talk(some_func_1)
talk(some_func_2)
talk(print, 1, 2, 3, 4, 5)
print("After empty print")

animal_sound_function = choose_animal(1)
a = animal_sound_function
a()

b = a
b()
animal_sound_function_2 = choose_animal(34328947)
print(type(animal_sound_function))
animal_sound_function()
