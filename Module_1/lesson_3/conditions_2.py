x = input("Select number between 1 and 100: ")
x = int(x)
condition = x > 10 and x < 100
print("x>10? : ", condition)
secret_code = 21
if condition:
    print("Welcome to 'if' statement")
    if x == secret_code:
        print("You found secret code")
    else:
        print("Try to found secret code")
        if x > secret_code:
            print("Less")
        else:
            print("More")
else:
    print("Welcome to 'else' statement")
