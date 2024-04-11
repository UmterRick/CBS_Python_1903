# and - "і"
# or - "або"
# not - "не"

x = 10
y = 11
a = 10

print(x < y)  # True
print(x <= y)  # True
print(x > y)  # False
print(x >= y)  # False

print(x == a)  # True
print(x != a)  # False

print(x is a)
print("x:", id(x))
print("a:", id(a))

print(x is not a)

color = "red"
size = 10
shape = "circle"
print("============================")
print(color == 'red')
print(size > 5)
print(shape != "square")

print("Do we have circle of blue color, with size bigger then 3?")
condition = color == "blue" and shape == "circle" and size > 3  # False and True and True -> False and True -> False
print(condition)

print("Do we have figure of blue color, with size bigger then 15 or at least it is a circle?")
condition = (color == "blue" and size > 15) or shape == "circle" # (False and False) or True -> False or True -> True
print(condition)





