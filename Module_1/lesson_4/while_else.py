x = 0
is_broken = True
while x < 10:
    # do something
    print(f"{x=}")
    x += 1
    # if x == 8:
    #     break
else:
    is_broken = False
    print("You successfully finish the loop")

print(is_broken)