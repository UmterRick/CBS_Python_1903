class A:
    def method(self):
        print("Class A")


class B(A):
    def method(self):
        print("Class B")


class C(A):
    def method(self):
        print("Class C")


class D(C, B):
   pass


new_object = D()
new_object.method()

print(D.__mro__)
