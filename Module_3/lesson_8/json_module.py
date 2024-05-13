import json


with open("example_data.json") as json_file:
    x = json.load(json_file)
    json_file.seek(0)
    file_content = json_file.read()
print(x)
print(type(x))
y = json.loads(file_content)
print(y)

x['name'] = "vlad"

with open("new_json.json", 'w+') as f_j:
    json.dump(x, f_j)


python_dict_obj = {
  "name": "vlad",
  "surname": "Surname",
  "fiends_names": (
    "John",
    'Jack',
    "Hanna",
  ),
}
x =  json.dumps(python_dict_obj)
print(x)
print(type(x))



