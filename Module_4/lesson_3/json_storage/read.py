import datetime
import json

data = {
    'first_name': 'Eugene',
    'last_name': 'Petrov',
    'age': 23,
    'birth_date': datetime.date(2000, 2, 1).strftime("%Y/%m/%d"),
    'hobbies': [
        'guitar',
        'cars',
        'mountains',
        'adventures',
        'gaming'
    ]
}

json_format_data = json.dumps(data)
print(json_format_data, type(json_format_data))


with open("storage.json", "w") as f:
    json.dump(data, f)

