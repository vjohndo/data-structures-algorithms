def add(x, y):
    """Add function"""
    return x + y

def subtract(x, y):
    """Subtract Function"""
    return x - y

def multiply(x, y):
    """Multiply Function"""
    return x * y

def divide(x, y):
    """Divide function"""
    if y == 0:
        raise ValueError('Can not divide by zero!')
    return x / y

# Old method of testing
print()