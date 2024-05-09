def infinite_numbers():
    num = 0
    while True:
        yield num
        num += 1


"132231 -> == 132231 <-"


def is_palindrome(num: int):  # 123_456, 132_231
    if num // 10 == 0:
        return False

    temp = num
    reversed_num = 0
    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)  # 6, 65, 654, 6543, 65432, 654321
        # 1, 13, 132, 1322, 13223, 132231
        temp = temp // 10  # 12345, 1234 , 123 , 12, 1
        # 132231, 13223, 1322, 132, 13, 1

    if num == reversed_num:
        return True
    return False


for i in infinite_numbers():
    # is_pal = is_palindrome(i)
    # if is_pal:
    #     print(i)

    # if is_palindrome(i):
    #     print(i)

    if result := is_palindrome(i):  # := - моржовий оператор
        print(i, result)

