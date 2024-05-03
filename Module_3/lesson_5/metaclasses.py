class Metaclass(type):
    @classmethod
    def __prepare__(metacls, name, bases):
        class CustomDict(dict):
            __repr__ : lambda s: f"I am customdict at the  {id(s)}"
        namespace = CustomDict()
        print("From custom prepare: ", namespace)
        return namespace

    def __new__(metacls, name, bases, namespace):
        print(f"Create object using custom metaclass: {name}")
        name = name + "Vlad"
        bases = (list, MyClass)
        return super().__new__(metacls, name, bases, namespace)



class MyClass(metaclass=Metaclass):
    pass


obj = MyClass()
print(obj)
print(type(obj))

"""
print(type(1))
we_create_new_class = type("MyClass2", (str,), {})
print(we_create_new_class)
print(we_create_new_class.__bases__)
new_class_object = we_create_new_class()
print(type(new_class_object))

print(MyClass.__dict__)
x = MyClass()
print(x.__dict__)


class UncommonClass(metaclass=Metaclass):
    def __init__(self, x):
        self.x = x


obj = UncommonClass(3)
print(obj.__dict__)"""