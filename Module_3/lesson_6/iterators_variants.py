list_1 = [1, 2, 3]
tuple_1 = (1, 2, 3)
dict_1 = {'a': 1, 'b': 2, 'c': 3}
set_1 = {1, 2, 3}
string_1 = "Hello"

for collection in [list_1, tuple_1, dict_1, set_1, string_1]:
    print(f"Class: {collection.__class__}, IteratorClass: {iter(collection).__class__}")
