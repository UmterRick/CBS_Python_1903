"""
with open("example.txt") as file:
    print(file)
    print("Inside with:", file.closed)
    line_1 = file.readline()
    print(line_1)
    line_x = file.readline()
    print(line_x)
print("Outside with:", file.closed)
"""
print("\nFile readlines")
with open("example.txt") as file:
    lines = file.readlines()
    print(lines)

for line in lines:
    print(line)

print("\nFile Iterator")
with open("example.txt") as file:
    for line in file:
        print(line)

print("\nRead File ")
with open("example.txt") as file:
    x = file.read(17)
    print(x)

