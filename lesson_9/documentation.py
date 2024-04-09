# help(len)
# print("----------")
# print(len.__doc__)

def multiply(value: float | int, multiplier: float | int) -> float | int:
    """
    Function to get math result of value multiplied by multiplier

    :param value: main value which you want to multiply
    :param multiplier: secondary value on which you want to multiply
    :return: result integer of float value
    """

    return value * multiplier


multiply(10, 2)

help(multiply)