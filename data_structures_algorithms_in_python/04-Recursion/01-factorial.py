def factorial(n):

    # This is O(1)
    if n == 1: # base case established
        return 1
    
    # factorial() is activated n times, each of which is O(1) hence this would be O(n)
    return n * factorial(n-1)  # progression to the base case & calling of the original function