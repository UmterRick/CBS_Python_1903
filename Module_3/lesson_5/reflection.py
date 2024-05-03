class CustomClass:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.name = None

    def get_coords(self):
        return self.x, self.y

    def set_name(self, new_name):
        self.name = new_name


"""
hasattr
getattr
delattr
setattr
"""

coordinate = CustomClass(10, 5)

if hasattr(coordinate, "x"):
    print("This obj has attribute x", coordinate.x)

if not hasattr(coordinate, "age"):
    print("This obj doesnt has attribute age")

print(coordinate.x)
# print(coordinate.age)


possible_attr = ["x", "age", "name", "y", "a"]

delattr(coordinate, "name")

for some_attr in possible_attr:
    print("\n\n")
    if hasattr(coordinate, some_attr):
        result = getattr(coordinate, some_attr)
        print(some_attr, result)
    else:
        print(f"Object coordinate does not have attr {some_attr}")
        setattr(coordinate, some_attr, "New Value")
        print(f"We got new attribute for object: {some_attr} = {getattr(coordinate, some_attr)}")

class TestClass:
    pass

def set_name(obj, value):
    if hasattr(obj, "name"):
        obj.name = value
        return

    if hasattr(obj, "title"):
        obj.title = value
        return

    setattr(obj, "name", value)


x = TestClass()
set_name(x, "Test Name")
print(x.name)


print(globals())


custom_class_instance = globals()["CustomClass"](1, 2)
setattr(custom_class_instance, "x", 100)
print(custom_class_instance.get_coords())


some_code = input(">")
eval(some_code)

print(globals())