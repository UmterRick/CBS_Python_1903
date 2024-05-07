from task_2 import upd_contact


x = hasattr(upd_contact, "name")
print("Has: ", x)


x = getattr(upd_contact, "name")
print("Get: ", x)


setattr(upd_contact, "age", 100)
setattr(upd_contact, "name", 100)
print("Set: ", upd_contact.age)
print("Set: ", upd_contact.name)

try:
    delattr(upd_contact, "name")
    print(upd_contact.__dict__)
    print("Del: ", upd_contact.name)
except AttributeError as exc:
    print(f"Object {exc.obj}: attr {exc.name} not found (((")

