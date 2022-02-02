from pickletools import read_uint1


def add(x, y):
    """Add function"""
    return x + y

def subtract(x, y):
    """Subtract Function"""
    return x - y

def divide(x, y):
    """Divide function"""
    if y == 0:
        raise ValueError('Can not divide by zero!')
    return x / y