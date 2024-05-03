from pprint import pprint

x = 2

b = type(x)
a = x.__class__

print(b, a)

"""
class MyClass:
    def __init__(self, param):
        self.param = param


def test_func(a, b):
    print(a + b)


func = test_func

test_func(1, 1)
func(10, 90)

new_class_name = MyClass

print(MyClass)
print(new_class_name)

class_object = new_class_name(45)
print(class_object.param)
"""

# pprint(str.__dict__)
"""
method_name = input("Method: ")
result = str.__dict__[method_name]("543+", "+")
print(result)
"""


class MyString(str):
    pass


class MySuperString(MyString, str):
    pass


print(MySuperString.__base__)
print(MySuperString.__bases__)
string_class = MySuperString.__bases__[0]
print(type(string_class()))

