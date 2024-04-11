world = "Hello"


def add_number(a: int, b: int) -> int:
    result = a + b
    print(result)

    return result


def extend_list_with_itself(arg1: list) -> None:
    arg1.extend(arg1)


list_1 = [1, 2, 3]
print("Before", list_1)
extend_list_with_itself(list_1)
print("After", list_1)



x, y = 1, 99

x_plus_y = add_number(x, y)

print(x_plus_y ** 2)
