def some_function(a, b, c, d, e, f):
    x = a + b + c + d + e + f

    def some_nested_function(arg1, arg2):
        print(arg1 - arg2)

    some_nested_function(x, f)


some_function(1, 2, 3, 4, 5, 6)
# some_nested_function(10, 20)


# a = input("Name: ")
a = [1, 2, 3]
# a = (1, 2, 3)
def transform_input(a):
    a.append("999")
    print("Inside:")
    print(a)
    print()


transform_input(a)

print("Outside")
print(a)

