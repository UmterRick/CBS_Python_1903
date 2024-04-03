print("List Methods:")
for method in dir(list()):
    if not method.startswith("__"):
        print(method)

'''
append
clear
copy
count
extend
index
insert
pop
remove
reverse
sort
'''

example_list = [1, 2, 3]

example_list.append("New Element")  # [1, 2, 3, 'New Element']  return None

result = example_list.pop()  # [1, 2, 3]  return popped element ("New Element")
result = example_list.pop(1)  # [1, 3] return popped element (2)

example_list.insert(0, "First Element")  # ['First Element', 1, 3]
example_list.insert(1, 0)  # ['First Element', 0, 1, 3]
example_list.insert(len(example_list) // 2, "Middle Element")  # ['First Element', 0, 'Middle Element', 1, 3]

example_list.remove("First Element")  # [0, 'Middle Element', 1, 3]  return None

additional_list = [100, 101, 102]
example_list.extend(additional_list)  # [0, 'Middle Element', 1, 3, 100, 101, 102]


print(example_list)

example_list.reverse()
print(example_list)

example_list.sort(key=lambda element: len(str(element)), reverse=True)
print(example_list)

print()
reversed_version = list(reversed(example_list))
print(reversed_version)
print("Original:", example_list)


sorted_version = list(sorted(example_list, key=lambda element: len(str(element)), reverse=True))