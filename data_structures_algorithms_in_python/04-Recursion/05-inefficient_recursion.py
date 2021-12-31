def unique(S, start, stop):
    """ Return true is there are no duplicate elements in slice S[start:stop]"""
    # We now that a single element is arbitrarily unique.

    if stop - start <= 1: return True
    elif not unique(S, start, stop-1): 
        return False
    elif not unique(S, start+1, stop):
        return False
    else: return S[start] != S[stop-1]

def bad_fibonacci(n):
    if n <= 1:
        return n
    else:
        return bad_fibonacci(n-1) + bad_fibonacci(n-1)

    # This is bad.. we are spawning two additional calls for every call of fib
    # this results in an exponentional function O(n^2)

# Let's improve the fibonacci call by 

def good_fibonacci(n):
    """ Return pair of Fib number, F(n) and F(n-1) """

    # This one is O(n), there will be a max of n recursion traces, all operations within each trace for O(1).

    if n <= 1:
        return (n,0) # base case for n <= 1, 
    else:
        (a,b) = good_fibonacci(n-1) # Get the fib number, were a is fib(j-1) and b is fin(j-2)

    return (a + b, a) # return ( fib(j-1), fib(j-2))


print(good_fibonacci(7))