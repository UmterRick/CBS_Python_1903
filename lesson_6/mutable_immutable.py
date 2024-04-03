# str is immutable (незмінюваний)
from sys import getsizeof

print("\tStr: ")

some_str = "hello world!"
# TypeError
# some_str[0] = "H"
print(some_str, id(some_str))
some_str = some_str.upper()
print(some_str, id(some_str))

# tuple is immutable (незмінюваний)
print("\tTuple: ")

some_tuple = (1, 2, 3, 4, 5)
# print(some_tuple[4])

# Type Error
# some_tuple[4] = 10
# print(some_tuple)


# list mutable (змінюваний)
print("\n\tList: ")

some_list = [1, 2, 3, 4, 5]
print(f"Address: {id(some_tuple)}")
print(some_list[4])
some_list[4] = 10
print(some_list[4])
print(f"Address: {id(some_tuple)}")

some_list.append(99)
print(some_list)

big_list = [x for x in range(10_000)]
big_tuple = tuple(big_list)
print("Tuple:", getsizeof(big_tuple), "bytes")
print("List:", getsizeof(big_list), "bytes")

