test_list = [-1, 10, -33, 42, 55, -13, 45]
print(test_list)


def transform(element):
    return f"New Element - {element}"


def validate(element):
    is_valid = element < 0
    return is_valid


list_1 = [transform(x) for x in test_list]
print(list_1)

list_2 = [validate(x) for x in test_list]
print(list_2)

list_3 = [transform(x) for x in test_list if validate(x)]
print(list_3)

list_4 = [f"{x} {y}" for x in ["John", "Jack", "Michel"] for y in ["Doe", "Smith", "Jackson"]]
gen_4 = (f"{x} {y}" for x in ["John", "Jack", "Michel"] for y in ["Doe", "Smith", "Jackson"])
print(list_4)

for i in gen_4:
    print(i)
