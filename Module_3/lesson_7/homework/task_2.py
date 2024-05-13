def square_of_even_gen(input_iterable):
    for num in input_iterable:
        if num % 2 == 0:
            yield num ** 2


def square_of_even_loop(input_iterable):
    result_list = []
    for num in input_iterable:
        if num % 2 == 0:
            result_list.append(num ** 2)
    return result_list


example_list = [0, 1, 2, 3, 4, 5, 6, 7]
result = [x ** 2 for x in example_list if x % 2 == 0]
print(result)

print()

for element in square_of_even_loop(example_list):
    print(element)


