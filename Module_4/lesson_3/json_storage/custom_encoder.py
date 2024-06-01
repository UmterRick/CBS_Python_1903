import datetime
import json


class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.datetime):
            return {
                'value': o.strftime("%d/%m/%Y %H:%M:%S"),
                '__datetime__': True
            }
        elif isinstance(o, datetime.date):
            return {
                'value': o.strftime("%d/%m/%Y"),
                '__date__': True
            }
        elif isinstance(o, set):
            return list(o)
        return super().default(o)


data = {
    'first_name': 'Eugene',
    'last_name': 'Petrov',
    'age': 23,
    'birth_date': datetime.date(2000, 2, 1),
    'alarm': datetime.datetime(2024, 6, 2, 12, 0, 0),
    'hobbies': {
        'guitar',
        'cars',
        'mountains',
        'adventures',
        'gaming'
    }
}
json_data = json.dumps(data, cls=DateTimeEncoder)
print(json_data)
