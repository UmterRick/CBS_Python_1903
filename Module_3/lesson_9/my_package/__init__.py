from Module_3.lesson_9.my_package.module_1 import get_name_lower, get_name_upper, Example
from Module_3.lesson_9.my_package.module_2 import get_age_from_date, get_birth_year_from_age

Example.counter = 10


print("Hello from my_package __init__")

__all__ = (
    "Example",
    "get_name_lower"
)