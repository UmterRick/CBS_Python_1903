
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before original (from decorator wrapper)")
        valid_args = [isinstance(arg, int) for arg in args]
        if not all(valid_args):
            raise TypeError("All arguments must be <type 'int'>")

        args = [arg * 100 for arg in args]
        func(*args, **kwargs)
        result = "HAHAHAHAHAHAHA"
        print(f"Catch result in decorator: {result}")
        # result = None
        print("After original (from decorator wrapper)")
        return result

    return wrapper


def logger_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open("log.txt", "a") as file:
            file.write(f"Func {func.__name__} completed with {result} (args={args}, kwargs={kwargs})")
        return result
    return wrapper
def original_function():
    print("Some Important things happened")

@decorator
@logger_decorator
def another_function(arg1, arg2):
    print("Very Important things happened")
    return arg1 + arg2

@logger_decorator
def math_func(*args):
    return sum(args)

# !!! without syntax sugar !!!
# decorated_func = decorator(another_function)

# another_function()
# another_function(10, "10")

result = math_func(1, 2, 3, 4, 5, 5,  6)
print(result)


def cast_type(required_type=None): # int
    def inner_decorator(function): # divide
        def wrapper(*args, **kwargs): # args = (10, 3), kwargs = {}
            result = function(*args, **kwargs)
            if required_type:
                return required_type(result)
            return result
        return wrapper
    return inner_decorator

@cast_type()
def divide(x, y):
    return x / y


result = divide(10, 2)
print(result, type(result))