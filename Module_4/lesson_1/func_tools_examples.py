example_list = list(range(1, 21))
# map
def transform(x):
    return x ** 2

map_result = list(map(transform, example_list))
map_result_2 = list(map(lambda el: True if el % 2 else False, example_list))
print(map_result)
print(map_result_2)


# filter
print("FILTER")
def make_decision(x):
    if x < 10:
        return False
    return True
filter_result = list(filter(make_decision, example_list))
filter_result_2 = list(filter(lambda el: el > 10, example_list))
print(filter_result)
print(filter_result)

from functools import reduce

reduce_result = reduce(lambda x, y: x-y, example_list)
print(sum(example_list))
print(reduce_result)
