print("name", "age")
"""
for i in range(3):
    for j in range(5):
        print("*" * j, "+" * j, end="\n", sep="--")
"""

height = 10
width = 40
symbol = "+"
for i in range(height + 1):
    for j in range(width + 1):
        print(symbol, end="")
    print()