import json

json_data = '{"first_name": "Eugene", "last_name": "Petrov", "age": 23, "birth_date": "2000/02/01", "hobbies": ["guitar", "cars", "mountains", "adventures", "gaming"]}'
python_data = json.loads(json_data)
print(type(python_data))
print(python_data)
print(python_data["first_name"])



with open("storage.json", "r") as f:
    python_data_2 = json.load(f)
    print(type(python_data_2))
    print(python_data_2)
    print(python_data_2["first_name"])
