import inspect
from pprint import pprint

from task_2 import Contact, UpdateContact

c = Contact("Surname", "Name", 380671112233, "surname_name@gmail.com", )
u_c = UpdateContact("Surname_2", "Name_2", 380671112244, "surname_name_2@gmail.com", "Manager")

pprint(inspect.getmembers(u_c, predicate=inspect.ismethod))