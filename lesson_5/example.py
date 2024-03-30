# int array[5] = [1, 2, 3, 4, 5]
some_tuple = ()
some_tuple = (1, True, 3, "Hello", 5, (1, 2, 3))
for el in some_tuple:
    print(id(el), end=", ")

print()
print("> ", id(some_tuple))
