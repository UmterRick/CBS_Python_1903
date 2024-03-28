x = 2

if x == 1:
    print("One")
elif x == 2:
    print("Two")
elif x == 3:
    print("Three")
else:
    print("X More then three")


if x == 1:
    print("One")
if x == 2:
    print("Two")
if x == 3:
    print("Three")
if x > 3:
    print("X More then three")

message = "Default message, all conditions are failed"
if x < 2:
    message = "x less then 2"
if x > 2:
    message = "x more then 2"

print(message)