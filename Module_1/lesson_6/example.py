from copy import deepcopy

# list_1 = [1, 2, 3]
# print(list_1, id(list_1))
# list_2 = list_1
# print(list_2, id(list_2))
# list_1[0] = "Something new"
# print(list_2)


# list_1 = [1, 2, 3]
# print(list_1, id(list_1))
# list_2 = list_1.copy()
# print(list_2, id(list_2))
# list_1[0] = "Something new"
# print(list_1)
# print(list_2)


list_0 = ["a", "b", "c"]
print(f"{list_0=} | {id(list_0)=}")
list_1 = [1, 2, list_0]
print(f"{list_1=} | {id(list_1)=}")
list_2 = deepcopy(list_1)
print(f"{list_2=} | {id(list_2)=}")


print("List1 [-1] ID:", id(list_1[-1]))
print("List2 [-1] ID:", id(list_2[-1]))

# list_0[0] = "abra"
# list_0[1] = "kadabra"
list_1[-1][0] = "abra"


print(f"{list_1=} | {id(list_1)=}")
print(f"{list_2=} | {id(list_2)=}")





