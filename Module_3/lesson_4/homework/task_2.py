class Calculator:
    @staticmethod
    def _transform_params(a, b):
        return [float(a), float(b)]

    def add(self, a, b):
        try:
            a, b = self._transform_params(a, b)
            return a + b
        except ValueError:
            print("A and B must be valid numbers")

    def subtract(self, a, b):
        a, b = self._transform_params(a, b)
        return a - b

    def multiply(self, a, b):
        a, b = self._transform_params(a, b)

        return a * b

    def divide(self, a, b):
        try:
            a, b = self._transform_params(a, b)
            return a / b
        except ValueError:
            print("A and B must be valid numbers")
        except ZeroDivisionError:
            print("B cant be a zero")

    def pow(self, a, b):
        try:
            a, b = self._transform_params(a, b)

            return a ** b
        except ZeroDivisionError as exc:
            print(exc.args)


calculator = Calculator()
operator = None
while operator != "exit":
    a = input("Type A param:")
    b = input("Type B param:")
    operator = input("Type operation:")
    result = None

    match operator:
        case '-':
            result = calculator.subtract(a, b)
        case '+':
            result = calculator.add(a, b)

        case '/':
            result = calculator.divide(a, b)

        case '*':
            result = calculator.multiply(a, b)

        case '^':
            result = calculator.pow(a, b)

        case _:
            print("Select acceptable operator (+, -, /, *, ^)")
    if result is not None:
        print(f"Result: {result}")
