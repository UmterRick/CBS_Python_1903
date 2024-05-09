import sys
import cProfile

num_list = [i ** 2 for i in range(10_001)]
num_gen = (i ** 2 for i in range(10_001))

# print("List: ", sys.getsizeof(num_list))
# print("Generator: ", sys.getsizeof(num_gen))


cProfile.run('sum([i ** 2 for i in range(1000001)])')
cProfile.run('sum((i ** 2 for i in range(1000001)))')






