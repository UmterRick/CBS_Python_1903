import functools


def is_divider(number):
    print("Coroutine started")
    while True:
        value = yield
        if number % value == 0:
            print(value,  "is divider for", number)
        else:
            print(value,  "is NOT divider for", number)

cor = is_divider(100)
print(cor)
cor.send(None)
cor.send(11)
cor.send(18)
cor.send(20)


def coroutine(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        res.send(None)
        return res
    return wrapper


@coroutine
def is_divider_cor(number):
    print("Coroutine started")
    while True:
        value = yield
        if number % value == 0:
            print(value,  "is divider for", number)
        else:
            print(value,  "is NOT divider for", number)


cor = is_divider_cor(100)

cor.send(11)
cor.send(18)
cor.send(20)
