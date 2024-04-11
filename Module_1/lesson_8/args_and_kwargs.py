def func(*args, **kwargs):
    print(args)
    print(kwargs)
    name = kwargs.get("name")
    if name is not None:
        print(f"Hello {name}")




func(1, 2, 2, 4, "saldmaskdmas", 432, "sdadasd", [1, 2, 3])

print("----------")
func(name="vlad", age=21, language="Python")


def get_sum(*args_nums):
    print(sum(args_nums))
