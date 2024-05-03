import inspect
from pprint import pprint

pprint(dir(inspect))


def get_sum():
    return None


res = inspect.isbuiltin(get_sum)
print(res)

