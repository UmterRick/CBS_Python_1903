class MyDict:
    class MyDictIterator:
        def __init__(self, curr_dict):
            self.values = list(curr_dict.values())
            self.counter = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.counter >= len(self.values):
                raise StopIteration
            value = self.values[self.counter]
            self.counter += 1
            return value

    def __init__(self, **kwargs):
        self.storage: dict = kwargs

    def __iter__(self):
        return MyDict.MyDictIterator(self.storage)


my_dict = MyDict(name="Name", age=10, email="test@mail.com")
for i in my_dict:
    print(i)
