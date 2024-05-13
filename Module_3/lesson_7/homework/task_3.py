def prime_numbers_gen(n):
    num = 2
    count = 0

    while count < n:
        if is_prime(num):
            yield num
            count += 1
        num += 1


#  Сито Ератосфена
def is_prime(number) -> bool:
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


for i in prime_numbers_gen(21):
    print(i)
