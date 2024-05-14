import datetime

print("Hello from Module_2")


def get_age_from_date(birth_date: datetime.date) -> int:
    time_from_birth = datetime.date.today() - birth_date
    return int(time_from_birth.days / 365)


def get_birth_year_from_age(age: int) -> int:
    return datetime.date.today().year - age
