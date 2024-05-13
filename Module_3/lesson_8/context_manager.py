with open("example.txt") as file:
    print(file)
    print("Inside with:", file.closed)
    line_1 = file.readline()
    print(line_1)
    line_x = file.readline()
    print(line_x)
print("Outside with:", file.closed)