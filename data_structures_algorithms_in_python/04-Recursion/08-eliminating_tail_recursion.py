def binary_search_iterative(data, target):
    """Return True if target is found in the given Python list."""

    # The while loop keeps running and we change the candidate namespace to make it work

    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target == data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False

def reverse_iterative(S):
    """Reverse elements in sequence S"""
    start, stop = 0, len(S)
    while start < stop - 1:
        S[start], S[stop-1] = S[stop-1], S[start]
        start, stop = start + 1, stop - 1 # By narrowing the rance we can will eventually fail the while loop condition
        