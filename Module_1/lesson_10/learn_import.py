from random import *

from Module_1.lesson_10.another_file import (
    some_variable,
    very_useful_function,
)
from Module_1.lesson_9.homework import find_step

# from another_file import (
#     some_variable,
#     very_useful_function,
#
# )

"""
import some_module
from some_module import some_function
from some_module import *
"""


def randint():
    return 100


# x_1 = random.randint(10, 1000)
# x_2 = randint(10, 1000)
l = list("Hello world")

some_letter = choice(l)
print(some_letter)

print(some_variable)
very_useful_function()

find_step(10)
