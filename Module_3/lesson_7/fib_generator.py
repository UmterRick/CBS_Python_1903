def fib_generator():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a


gen_obj = fib_generator()
for i in range(30):
    print(next(gen_obj))
print()
print(next(gen_obj))

