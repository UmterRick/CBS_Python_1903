from task_2 import Contact, UpdateContact


c = Contact("Surname", "Name", 380671112233, "surname_name@gmail.com", )
u_c = UpdateContact("Surname_2", "Name_2", 380671112244, "surname_name_2@gmail.com", "Manager")

print("u_c is Contact: ", isinstance(u_c, Contact))
print("c is UpdateContact: ", isinstance(c, UpdateContact))
print("u_c is UpdateContact: ", isinstance(u_c, UpdateContact))
print("u_c is child of Contact: ", issubclass(u_c.__class__, Contact))
print("c is child if UpdateContact: ",  issubclass(c.__class__, UpdateContact))