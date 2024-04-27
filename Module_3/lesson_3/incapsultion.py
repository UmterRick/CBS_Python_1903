"""
public - доступен всім і всюди
protected - доступен всюди але не бажано до взаємодії ззовні
private - доступ ззовні заборонено
"""


class SomeClass:
    def public_method(self):
        print("I am public")
        self.private_method_1()
        self.private_method_2()

    def private_method_1(self):
        print("I am private")
        print("Hidden logic")

    def private_method_2(self):
        print("I am private")
        print("Hidden logic")


new_obj = SomeClass()

new_obj.public_method()
new_obj.private_method_1()
