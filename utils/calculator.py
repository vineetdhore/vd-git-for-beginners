def add_nums(a, b):
    """Returns the sum of two numbers."""
    return a + b

def subtract_nums(a, b):
    """Returns the difference of two numbers."""
    return a - b

def multiply_nums(a, b):
    """Returns the product of two numbers."""
    return a * b    

def divide_nums(a, b):
    """Returns the quotient of two numbers. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

