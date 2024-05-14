import sys

from pprint import pprint
import random
import module_example

# sys.path.pop(0)

print(module_example.IMPORTANT_VALUE)
pprint(sys.path)
print(random.randint(10, 20))