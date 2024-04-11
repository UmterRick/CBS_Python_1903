def example_recursion(depth: int = 1):
    print(f"Hello from recursion on depth: {depth}")
    if depth < 3:
        go_out_with = example_recursion(depth + 1)
        print(f"It was return from example_recursion({go_out_with}")
    return depth


x = example_recursion()
print(x)

"""
0 1 1 2 3 5 8 13 21 34 

"""


def recursion_fibonacci(n):
    if n <= 1:
        return n
    else:
        arg_1 = recursion_fibonacci(n - 1)
        arg_2 = recursion_fibonacci(n - 2)
        return arg_1 + arg_2


for i in range(20):
    print(recursion_fibonacci(i))


#  binary search