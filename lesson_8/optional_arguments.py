def some_func(a: int, b: int = 0) -> None:
    print("Result", a + b)
    return None


some_func(12, b=23)


def another_func(a):
    inner_a = a.copy()
    print("START")
    print(inner_a)
    inner_a.append(3)
    print(inner_a)
    print("END")
    return inner_a


my_list = [0, 0, 0]
my_list = another_func(my_list)

# print()
print(my_list)
# another_func(my_list)
# print()
# another_func(my_list)
