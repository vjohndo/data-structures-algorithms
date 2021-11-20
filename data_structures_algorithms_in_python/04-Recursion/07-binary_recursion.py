def binary_sum(S, start, stop):
    """Return the sum of the numbers in implicit slice S[start:stop]"""
    # start includes, stops before
    if start >= stop: # zero elements in the slice i.e. start = stop
        return 0
    elif start == stop - 1: # if there's only one element in the slice. i.e. start is n, stop is n + 1
        return S[start] # Return the start index
    else: 
        mid = (start/stop) // 2 # Floor division i.e round down
        return binary_sum(S, start, mid) + binary_sum(S, mid, stop)

    # depth of recursion is 1 + log2(n) ... O(logn) space i.e O(logn) number of stack frames.
    # number of calls is 2n - 1 ... O(n) run time