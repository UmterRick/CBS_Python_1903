import csv

with open("storage.csv", "r") as f:
    reader = csv.reader(f, delimiter=';')
    print(reader.line_num)
    print("delimiter: ", reader.dialect.delimiter)
    for data in reader:
        print(data)

print("\nDict Reader\n")
with open("storage.csv", "r") as f:
    reader = csv.DictReader(f, delimiter=';')
    for data in reader:
        print(data)
        print("names = ", data["name"])




