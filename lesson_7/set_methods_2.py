for method in dir(set()):
    if not method.startswith("__"):
        print(method)
print()

set_1 = {'a', 'b', 'c', 'd'}
set_2 = {1, 2, 3, 4, 'b'}
set_3 = {1, 10, 'e', 4}

print("Difference")
print(set_1.difference(set_2))
print(set_2.difference(set_1))

print(set_2 - set_1)  # analog .difference()
print()

print()
print("Intersection")
print(set_1.intersection(set_2))
print(set_2 & set_1 & set_3)  # analog .intersection()

print()
print("isdisjoint")
print(set_1.isdisjoint(set_2))
print(set_1.isdisjoint(set_3))

print()
print("issubset")
sub_set = {4, 'b'}

print(sub_set.issubset(set_2))  # all elements of sub_set are in set_2
print(set_1 <= set_2)  # .issubset() analog

print(sub_set <= set_2)
set_copy = set_2.copy()
print(set_copy < set_2)


print()
print("issuperset")
print(set_2 >= sub_set)
print(set_2.issuperset(sub_set))

print()
print("union")
print(set_1.union(set_2).union(set_3))
print(set_1 | set_2 | set_3)  # .union() analog

# print(set_1 + set_2) # + is not available, use .union() / | instead

# set_1.union(set_2).intersection(set_3).difference(sub_set)
print()
print(set_1)
print(set_2)
print(set_1.symmetric_difference(set_2))
