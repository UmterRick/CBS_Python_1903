print("\nWrite to File ")
with open("example.txt", 'w') as file:
    file.write("New File content\n")

print("\nAdd to File ")
with open("example.txt", 'a') as file:
    file.write("Add to content")

print("\nWrite Lines to File ")
new_lines = ["New Content 2\n", "John Doe\n", "2024/05/11\n"]
with open("example.txt", 'w') as file:
    file.writelines(new_lines)