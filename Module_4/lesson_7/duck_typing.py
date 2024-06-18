from typing import Union
class User:

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self) -> str:
        return self.first_name + ' ' + self.last_name

    def __repr__(self):
        return f"User({self.first_name}, {self.last_name})"


def create_new_user(first_name: str, last_name: str) -> User:
    return User(first_name, last_name)


# user_1 = create_new_user(257, 20)
user_2 = create_new_user("Name", "LastName")
# print(user_1)
print(user_2)


def create_many_users(first_names: list[str], last_names: list[str]) -> list[User]:
    full_names = zip(first_names, last_names)
    users = []
    for name, surname in full_names:
        users.append(User(name, surname))

    return users


names = ["Joe", "Bob", "Bill"]
last_names_values = ["Dou", "Jackson", "Smith"]

many_users = create_many_users(names, last_names_values)


def sort_users(users: list[User]) -> dict[str, list[User]]:
    sorted_users = {}
    for user in users:
        first_letter = user.first_name[0]
        if first_letter in sorted_users:
            sorted_users[first_letter].append(user)
        else:
            sorted_users[first_letter] = [user]

    return sorted_users


s_users = sort_users(many_users)

x = [1, 2, 3, None, 5, 6, None, 0]


def func(arg: list[int | None]) -> list[int | None]:
    return arg


print(func(x))
