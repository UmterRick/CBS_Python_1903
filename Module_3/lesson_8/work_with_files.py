file = open(
    file="example_2.txt",
    mode='w+',
    # encoding="utf-16",
)

print(file)

file.close()
print(file)

file.write("dmasasdasdlas")