from typing import Iterable, TypeVar

T = TypeVar('T')
TemplateDict = dict[str, T]
IntDict = TemplateDict[int]
StrDict = TemplateDict[str]

def copy_list(sequence: Iterable[T]) -> list[T]:
    new_list: list[T] = []
    for item in sequence:
        new_list.append(item)
    return new_list


x = ['a', 'b', 'c']
x_int = [1, 2, 4, 5]
y = copy_list(x)

y_int = copy_list(x_int)

def some_func() -> IntDict: # dict[str, int]
    ...