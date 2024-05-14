import json
import os.path

file_name = "storage.json"


def write_new_url(url, short_name):
    with open(file_name, "r+") as json_file:
        storage = json.load(json_file)
        storage[short_name] = url
        json.dump(storage, json_file)


def get_url_by_name(name):
    with open(file_name, 'r') as json_file:
        storage = json.load(json_file)
        return storage.get(name)


if not os.path.exists(file_name):
    with open(file_name, 'x') as file:
        print("Create storage file")
        file.write("{}")


while True:
    action = input("Add, get or exit")
    match action:
        case 'add':
            url = input("Add url: ")
            name = input("Create Name: ")
            write_new_url(url, name)
        case 'get':
            name = input("Name: ")
            url = get_url_by_name(name)
            print(url)
        case 'exit':
            break


