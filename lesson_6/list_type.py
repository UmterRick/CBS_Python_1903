tuple_example = (1, 2, 3, 4, "Hello")
list_example = [1, 2, 3, 4, "Hello"]

list_example_2 = list()
list_example_2 = []

print(list_example[0])
print(list_example[-1])
print(list_example[2:4])
print(len(list_example))

print("Tuple Methods:")
for method in dir(tuple()):
    if not method.startswith("__"):
        print(method)

print()
print("List Methods:")
for method in dir(list()):
    if not method.startswith("__"):
        print(method)

