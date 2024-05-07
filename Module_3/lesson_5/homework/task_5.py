import inspect

from task_2 import Contact, UpdateContact


c = Contact("Surname", "Name", 380671112233, "surname_name@gmail.com", )
u_c = UpdateContact("Surname_2", "Name_2", 380671112244, "surname_name_2@gmail.com", "Manager")

print(c.__dict__)
# print(inspect.getmembers(c))
print(u_c.__dict__)

delattr(u_c, "job")
print(
    "\nDelAttr\n"
)
print(c.__dict__)
print(u_c.__dict__)
