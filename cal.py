def addition(a, b):
    return a + b

def substraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(x, y):
    if y == 0:
        raise ValueError ("divisor cannot be 0")
    return x / y