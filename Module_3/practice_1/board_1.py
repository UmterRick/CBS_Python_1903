# Super method


class Parent:

    def __init__(self, name):
        self.name = name

    def method(self, arg1):
        return arg1


class Child(Parent):

    def __init__(self, name):
        age = 20
        super().__init__(name)  # super method

    def method(self, arg1):
        return 0

    def super_method(self, arg1):
        return super().method(arg1)


class GrandChild(Child):
    def super_puper_method(self, arg_1):
        super().super_method(arg_1)


# assert

assert 1 > 0, "Line 34, 1 is not less then 0"

expectation = 9


def test():
    reality = 8
    try:
        assert expectation == reality
    except AssertionError:
        print("Test Failed")
