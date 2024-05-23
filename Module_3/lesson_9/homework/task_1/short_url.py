import json
import os.path

file_name = "storage.json"


class ShortUrl:

    def __init__(self):
        if not os.path.exists(file_name):
            with open(file_name, 'x') as file:
                print("Create storage file")
                file.write("{}")

    def write_new_url(self, url, short_name):
        with open(file_name, "r+") as json_file:
            storage = json.load(json_file)
            storage[short_name] = url
            json.dump(storage, json_file)

    def get_url_by_name(self, name):
        with open(file_name, 'r') as json_file:
            storage = json.load(json_file)
            return storage.get(name)
