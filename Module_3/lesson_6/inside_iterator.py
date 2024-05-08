# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ...


class FibonacciIter:
    def __init__(self, limit):
        print(f"Init {self.__class__.__name__}")
        self.limit = limit

    def __iter__(self):
        print(f"ITER {self.__class__.__name__}")

        self.counter = 0
        self.numbers = (0, 1)
        return self

    def __next__(self):
        # last_num = self.numbers[0]
        # curr_num = self.numbers[1]
        print("Call NEXT")
        print(f"Numbers were: {self.numbers}")
        last_num, curr_num = self.numbers

        last_num, curr_num = curr_num, last_num + curr_num
        self.numbers = last_num, curr_num

        print(f"Numbers now: {self.numbers}")

        self.counter += 1

        if self.counter > self.limit:
            raise StopIteration

        return last_num


fib = FibonacciIter(5)
for num in fib:
    print(f"> {num}")


print("END OF CODE")