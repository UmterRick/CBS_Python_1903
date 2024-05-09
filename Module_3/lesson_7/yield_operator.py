def new_generator(n):
    print(f"1) Yield new value - {n}")
    yield n
    n += 1
    print(f"2) Yield another value - {n}")

    yield n


generator_object = new_generator(10)
print(generator_object)
print(next(generator_object))
print(next(generator_object))
print(next(generator_object))
# for i in generator_object:
#     print(i)
