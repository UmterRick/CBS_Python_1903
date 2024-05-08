my_list = [0, 1, 2, 3]
# print(my_list[3])

iterator_object = iter(my_list)
"""
print(iterator_object)
print("Class: ", iterator_object.__class__)
print(iterator_object.__dir__())
"""
print("---- MANUAL NEXT() CALLS ----")
try:
    next(iterator_object)
    # print(x)
    next(iterator_object)
    # print(x)
    x = next(iterator_object)
    print(x)
    x = next(iterator_object)
    print(x)
    x = next(iterator_object)
    print(x)
except StopIteration:
    pass
print("END")


print()
print("---- FOR LOOP ----")
for i in my_list:
    print(i)
print("END")

print()
print("---- WHILE LOOP ACTS LIKE FOR LOOP ----")
iter_obj = iter(my_list)
while True:
    try:
        i = next(iter_obj)
        print(i)
    except StopIteration:
        break
print("END")


iterator = iter(my_list)
for i in range(2):
    print("Call next()")
    next(iterator)

print(">>>", next(iterator))