x = input("Select number: ")
x = int(x)
condition = x > 10 and x < 100 or x == 200
print("x>10? : ", condition)
if condition:
    print("Welcome to 'if' statement")
else:
    print("Welcome to 'else' statement")

# Not the best code-style
# if condition: print("Single line block")
user_age = input("How old are you?: ")
if user_age.isnumeric():
    user_age = int(user_age)
    print(f"Success you are {user_age} y.o.")
else:
    print("Please use only digits!")
    exit()

print("Save age to database ...")
if not isinstance(user_age, int):
    raise ValueError





print("END")