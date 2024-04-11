tuple_methods = dir(tuple())

# for method in tuple_methods:
#     print(method)
"""
count
index
"""
my_tuple_1 = (1, -4, 10, 3, 4, 7)
my_tuple_2 = tuple([1, 2, 3, 4, 4])

a = my_tuple_1.count(4)
print("Count >", a)

b = my_tuple_1.index(4, 2)
print("Index >", b)

to_find = "Hello"
if to_find in my_tuple_1:
    print("Index (element not in collection): ", my_tuple_1.index(to_find))
else:
    print(f"element {to_find} not in tuple")


print("Tuple + Tuple: ", my_tuple_1 + my_tuple_2)
print("Tuple * int: ", my_tuple_1 * 3)
# print("Tuple - Tuple: ", my_tuple_1 - my_tuple_2) Error
print("Length: ", len(my_tuple_1))
print("Max element: ", max(my_tuple_1))
print("Mix element: ", min(my_tuple_1))


# random_tuple = (1, 2, 10, 4, (2, 3, 4))
# print(">>>", min(random_tuple))

sorted_tuple = tuple(sorted(my_tuple_1, reverse=True))
print(f"Original: {my_tuple_1} {type(my_tuple_1)}")
print(f"Sorted: {sorted_tuple} {type(sorted_tuple)}")

reversed_tuple = tuple(reversed(my_tuple_1))
print(f"Original: {my_tuple_1} {type(my_tuple_1)}")
print(f"Reversed: {reversed_tuple} {type(reversed_tuple)}")
