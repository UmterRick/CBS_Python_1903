my_tuple = ("Hello", True, 1, 2, 3, (4, 5, 6))
print(my_tuple)

print(len(my_tuple))
for i in range(0, len(my_tuple)):
    print(my_tuple[i])

# print(my_tuple[99])
print("Full slice", my_tuple[0:99])

print("Reversed: ", my_tuple[::-1])

print(">>>", my_tuple[-1][1])

print("Slice", my_tuple[1::2])




