for method in dir(dict()):
    if not method.startswith("__"):
        print(method)
print()

some_dict = {
    "list_value": [1, 2, 3, ["Hello"]],
    "dict_value": {"nested_key": {"vlad": "Python Teacher"}},
    "key": "value",
    (1, 2, 3): "World!",
}

print(list(some_dict.keys()))
print(list(some_dict.values()))
print()
print(list(some_dict.items()))
print()

a, b = (10, 20)
print(a)
print(b)

for key, value in some_dict.items():
    print(f"In my dict i have key={key} and value={value}")
    if isinstance(value, list):
        some_dict[key] = value * 2
    # print(some_dict[i])
    # print()

print()
print(some_dict)

print("\n\n\n\n")

# just to see variable
variable = [1, 2, 3, ["Hello"]]

some_dict = {
    "list_value": variable,
    "dict_value": {"nested_key": {"vlad": "Python Teacher"}},
    "key": None,
    (1, 2, 3): "World!",
}

x = some_dict.get("unknown_key", "Default Value")
print(x)


print(some_dict)
if "list_value" in some_dict:
    popped_value = some_dict.pop("list_value")
    print(">", popped_value)

# print(variable)


print(some_dict)
x = some_dict.popitem()
print(x)

print(some_dict)
x = some_dict.popitem()
print(x)

print(some_dict)

add_to_dict = {"key_1": 100, "key_2": 200}
some_dict.update(add_to_dict)
print(some_dict)

print()
empty_dict = {}
empty_dict["new_key"] = 999
print(empty_dict)


