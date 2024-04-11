# dict use HashTable

some_dict = dict()
another_dict = {}

my_set = {1, 2, 3, 4, 5}
my_dict = {
    1: "Hello",
    "key": "value",
    (1, 2, 3): "World!",
    # [1, 2, 3]: "dsdksa",
    # "key": "World!",  # no duplicates
}
print(my_dict)

phonebook = {
    'Jack': '032-846',
    'Guido': '917-333',
    'Mario': '120-422',
    'Mary': '890-532',
}

print(my_dict)
print(phonebook["Jack"])

another_dict = {
    "list_value": [1, 2, 3, ["Hello"]],
    "dict_value": {"nested_key": {"vlad": "Python Teacher"}},
    "key": "value",
    (1, 2, 3): "World!",
}

print(another_dict["list_value"][-1][0][3])
print(another_dict["dict_value"]["nested_key"]["vlad"])


