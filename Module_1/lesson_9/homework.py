rec_counter = 0


def find_step(n):
    print(f">>> We are on {n} step:")
    global rec_counter
    rec_counter += 1
    if n == 0:
        print(f"We are Done from {n} step")
        print("+1 Way to get down")
        return 1
    elif n < 0:
        print(f"No way to get there from {n} step")
        return 0
    else:
        print(f"Go from {n} to {n-2}")
        two_step = find_step(n-2)

        print()
        print(f"Go from {n} to {n-1}")
        one_step = find_step(n-1)
        steps = two_step + one_step
        return steps


n = int(input("N: "))
print(find_step(n))
print(">>>", rec_counter)
