class ReverseIterator:
    def __init__(self, iterable):
        self._iterable = iterable
        self._index = len(iterable) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < 0:
            raise StopIteration
        value = self._iterable[self._index]
        self._index -= 1
        return value

my_list = [1, 2, 3, 4, 5]
reverse_iterator = ReverseIterator(my_list)
for item in reverse_iterator:
    print(item)
