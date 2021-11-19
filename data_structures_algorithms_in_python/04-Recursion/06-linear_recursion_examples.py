def linear_sum(S, n):
    """ Return the sum of the first n numbers of sequence S """
    # Base case when n == 0 i.e. index == -1
    if n == 0: 
        return 0
    else:
        # Returns dum of the remaining index + sequence S[n-1] index. Note that n-1 as n will be an integer
        return linear_sum(S, n-1) + S[n-1]

print(linear_sum([4, 3, 6, 2, 8], 5))

def reverse(S, start, stop):
    """ Reverse elements in implicit slice S[start:stop] """
    if start < stop - 1:    # Base case when start == stop - 1 & start == stop i.e. when there is less than two elements in the sequence
        S[start], S[stop-1] = S[stop-1], S[start] # swap the start and stop 
        reverse(S, start + 1, stop -1)

a = [4, 3, 6, 2, 8, 9, 5]
reverse(a, 0, 7)
print(a)

def power(x, n):
    """Compute the value x**n for integer n."""
    # Performs O(n)
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)
    
def power2(x,n):
    """Compute the value x**n for integer n"""
    if n == 0:
        return 1
    else:
        partial = power(x, n // 2) # skip through the doing linear recursion call # this would keep halving the inputs on each recursion call. O(log(n))
        result = partial * partial # this is ^2 part
        if n % 2 == 1: # if n is odd, include a extra factor of x+

            result *= x
        return result 