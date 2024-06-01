import csv


class MyDialect(csv.Dialect):
    quoting = csv.QUOTE_ALL
    quotechar = "*"
    delimiter = "#"
    lineterminator = "/"


csv.register_dialect("my_dialect", MyDialect)

with open("storage.csv", "r") as f:
    csv.DictReader(f, dialect="my_dialect")