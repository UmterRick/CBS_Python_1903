def test_func(a):
    raise AttributeError()
    if a > 10:
        return 2
    return 1

def some_func():
    try:
        x = test_func(20)
        return x
    except AttributeError as exc:
        print("Problem, some errors here")
        raise ValueError("Second Error") from exc
    else:
        print("All is good, no errors")

    finally:
        print("\nNo matter what, FINALLY is here ")


y = some_func()
print(f"\nWe got y={y}")