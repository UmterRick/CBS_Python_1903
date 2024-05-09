def iterate_over(iterable):
    iterator = iter(iterable)
    while True:
        try:
            value = next(iterator)
            print(value)
        except StopIteration:
            break


my_iterable = [1, 2, 3, 4, 5]
my_iterable = {1, 2, 3, 6,4 ,5, 3,3, 3}
iterate_over(my_iterable)
