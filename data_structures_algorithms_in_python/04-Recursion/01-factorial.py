def factorial(n):

    if n == 1: # base case established
        return 1
    
    return n * factorial(n-1)  # progression to the base case & calling of the original function