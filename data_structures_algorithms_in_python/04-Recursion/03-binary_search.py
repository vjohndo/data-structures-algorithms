def binary_search(data, target, low, high):
    """Return True if target is found in indicated portion of Python List"""

    # Progresses to base case by
    #   1) target = data[mid]
    #   2) target < data[mid]
    #   3) targer > data[mid]
    # An unsucessful search will results in "low" < "high"

    if low > high:
        # Notice on the if statements that that lead to recursion
        # We are passing in mid +- 1? Eventually if the target is not in the list
        # We will get the a point where the low and mid will be the same index
        # And the next recursion call will have low > high
        return False

    else:
        mid = (low + high) // 2 # Have to use floor division incase we get  
        if target == data[mid]:
            return True
        elif target < data[mid]:
            # Recur on the left portion of the middle
            return binary_search(data, target, low, mid - 1)
        else: # target > data[mid]
            return binary_search(data, target, mid + 1, high)