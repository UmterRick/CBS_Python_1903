my_list = [1, 2, 3]
for i in my_list:
    print(i)

some_str = "Hello"

def func():
    j = 0
    my_list[j] = 0
    return my_list[j]


# my_list[j]
# print(j)

def outer_function():
    global some_str
    variable = 42
    some_str = "World ----"
    print(some_str)
    def inner_function():
        print('Внутрішня функція')
        print(variable)
        print('Зовнішня функція')

    # print(variable)
    inner_function()

def change_global():
    global some_str
    some_str = "World -----"


func()

# print(10 / my_list[0])
print(some_str)
print("---------")
change_global()
print("---------")
print(some_str)
