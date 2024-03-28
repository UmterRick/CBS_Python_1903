value = 23
if value is None:
    pass  # TODO: resolve later
else:
    print("value is not None")


arg1 = input("First Number: ")
arg2 = input("Second Number: ")


if arg1.isnumeric() and arg2.isnumeric():
    arg1 = int(arg1)
    arg2 = int(arg2)
    operator = input("Select operator (+, -, *, /): ")
    if operator == '+':
        print(arg1 + arg2)
    elif operator == '-':
        print(arg1 - arg2)
    elif operator == '*':
        print(arg1 * arg2)
    elif operator == '/':
        print(arg1 / arg2)
    else:
        print("Unknown operator")
else:
    print(f"Cant to math operation between {arg1} and {arg2}")

x = input("Some number: ")
x = int(x)
if x % 2 == 0:
    print(f"{x} парне число")
else:
    print(f"{x} не парне число")
