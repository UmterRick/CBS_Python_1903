def generator():
    print("Generator Start")
    ...
    print("Yield at Generator")
    sub_result = yield from sub_generator(3)
    print(f"--- Generator After Yield (Got result = {sub_result})")

    print("Generator Second Yield")
    yield "END"


def sub_generator(num):
    print("Sub-Generator Start")

    a, b = 0, 1
    for _ in range(num):
        a, b = b, a + b
        print("Yield at Sub-Generator")
        yield a
        print("Sub-Generator After Yield")
    return "RESULT"



x = generator()
print(x)
print(">>>", next(x))
print(">>>", next(x))
print(">>>", next(x))
print(">>>", next(x))
# print(">>>", next(x))


y = generator()
print("\n Second Launch \n")
for i in y:
    print(f">>> {i}")


print("CODE END")
