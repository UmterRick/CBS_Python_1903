def reversed_gen(input_iterable):
    for i in range(len(input_iterable) - 1, -1, -1):
        yield input_iterable[i]


example_list = [0, 1, 2, 3, 4, 5, 6, 7]
for element in reversed_gen(example_list):
    print(element)
