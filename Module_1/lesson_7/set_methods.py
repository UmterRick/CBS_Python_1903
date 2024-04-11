for method in dir(set()):
    if not method.startswith("__"):
        print(method)
print()

set_1 = {'a', 'b', 'c', 'd'}
set_2 = {1, 2, 3, 4}

set_1.add('e')
set_2.add((9, 8, 7)) # tuple is okay to be in set
# set_2.add([9, 8, 7]) # list is NOT okay to be in set (unhashable)

print(set_1)
print(set_2)

set_1.update([3, 4, 5, 1])
set_1.update(set_2)

# set_1.clear()  # Remove all elements from set
print()
print(set_1)
set_1.pop()
print(set_1)
# some_list = [0, 1, 2, 3, 4]
# some_list.pop(2)
# print(some_list)




