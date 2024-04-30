def test_func():
    raise ZeroDivisionError()


def second_func():
    print("\n\t\t\t\tEnd of Program")

class MyException(Exception):
    def __init__(self, *args):
        self.args = args

    def print_exc_message(self):
        print("Oops!")


try:
    print("Try to run code with potential errors:\n")
    # x = 1 < "Hello"
    # raise ZeroDivisionError()
    # raise Exception()
    raise ValueError("1 is not good value for email", 213, 342, 31231, 12312, )
    # raise AttributeError("Name", "Object")

    print("Attempt successful, no errors \n")
except (ZeroDivisionError, AttributeError):
    print("\nError Handled, it was zero division or value error, I catch It")

except ValueError as my_error:
    # print(">>>My Error: ", my_error.args)
    print(f"\nValue error, I see you :) send report to developer team about {my_error}")
    if 0 in my_error.args:
        raise ZeroDivisionError()
    raise

except MyException as exc:
    print(exc.print_exc_message())


# except Exception:
#     print("Unknown error!!!")


second_func()
