from functools import partial

print_with_comma = partial(print, sep=' ___ ')

print_with_comma(2, 3, 5)


def example(arg1, arg2):
    print(arg1, arg2)


new_example = partial(example, arg1=10)
new_example(arg2=3)
new_example(arg2=4)
new_example(arg2=5)
new_example(arg2=99)


class User:
    def action(self, mode):
        return mode


default_user = User()
reader_user = User()
reader_user.action = partial(reader_user.action, mode="read")
reader_user_2 = User()

print(default_user.action('write'))
print(reader_user.action())
