import csv

with open("storage_2.csv", "w") as f:
    writer = csv.writer(f)

    writer.writerow(["age", "class", "phone", "floor"])
    writer.writerow([12, 13, 14, 15])
    writer.writerow([12, 13, 14, 15])
    writer.writerow([12, 13, 14, 15])
    # writer.writerows()'

print("\nDict Reader\n")
with open("storage_2.csv", "r") as f:
    reader = csv.DictReader(f, delimiter=',')
    for data in reader:
        print(data)

quote = csv.QUOTE_ALL

with open("storage_2.csv", "w") as file:
    writer = csv.DictWriter(
        f=file,
        fieldnames=["name", "category", "price"],
        quoting=quote
    )
    writer.writeheader()
    writer.writerow(
        {
            "name": 'Phone, IPhone',
            "category": 'Smart;Phone@',
            "price": '15_000'
        }
    )
    writer.writerow(
        {
            "name": 'Samsung27``, TV\'\' \"',
            "category": 'Smart;TV',
            "price": '35_000'
        }
    )


print("\nDict Reader\n")
with open("storage_2.csv", "r") as f:
    reader = csv.DictReader(f, delimiter=',')
    for data in reader:
        print(data)
