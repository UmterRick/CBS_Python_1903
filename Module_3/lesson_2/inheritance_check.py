from Module_3.lesson_2.inheritance_example_2 import BaseUser, Manager, SuperManager

manager_1 = Manager("mail@gmail.com", "qwer1234")

print("\ninstance")
result = isinstance(manager_1, Manager)
print(result)
result = isinstance(manager_1, int)
print(result)
isinstance(manager_1, BaseUser)
print(result)


print("\nsubclass:")
result = issubclass(Manager, str)
print(result)

result = issubclass(Manager, BaseUser)
print(result)

result = issubclass(SuperManager, BaseUser)
print(result)
