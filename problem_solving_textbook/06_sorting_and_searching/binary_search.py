# The Binary Search
def binary_search(a_list, item):
    """ Goes to middle and removes half without the target item """
    first = 0
    last = len(a_list) - 1

    # So long as the range can searched, keep searching. Otherwise the first and last points will keep shrinking
    while first <= last: 
        midpoint = (first + last) // 2 # Find the middle using floor division, i.e. it always rounds down the index
        if a_list[midpoint] == item:
            return True
        elif item < a_list[midpoint]:
            last = midpoint - 1
        else: # Item must be greater than the mid point, set extents of range to midpoint + 1
            first = midpoint + 1

    # Otherwise we've exhausted the list 
    return False

test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]

print('Version 1')
print(binary_search(test_list, 3))
print(binary_search(test_list, 13))

# The binary search... recursion
def binary_search_rec(a_list, item):

    # BASE 
    if len(a_list) == 0:
        return False
    
    # PROGESS TO BASE CASE
    else:
        midpoint = len(a_list) // 2 # Note how this would round up on even 
        if a_list[midpoint] == item:
            return True
        # We will call on the slice notation, noting that IT MUST slice with positive steps unless we specficy 
        elif a_list[midpoint] >= item:
            return binary_search_rec(a_list[midpoint+1:], item) # Notice how the midpoint is plus 1, slice will be always be at least 1 so if you ever get down to a single number that index 1 willl not exist
        else:
            return binary_search_rec(a_list[:midpoint], item) # Remember that slices call [start:uptobutnotincluding]... will eventuall get [:0] which will return an empty array as this slices from 0 index to -1 index with positive step

test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
test_list2 = [3, 5, 6, 8, 11, 12, 14, 15, 17, 18]

print('Version 2')
print(binary_search_rec(test_list, 3))
print(binary_search_rec(test_list, 13))
print(binary_search_rec(test_list2, 8))

# Including the starting and ending 
def binary_search_rec2(a_list, item):
    """ Appently if you pass the starting and ending indicies for the slice function, it is O(n) = 1 instead of O(n) = k ? """
    first = 0
    last = len(a_list) - 1

    if len(a_list) == 0:
        return False

    else:
        midpoint = (first + last) // 2 
        if a_list[midpoint] == item: 
            return True
        
        elif a_list[midpoint] >= item:
            return binary_search_rec(a_list[midpoint+1:last], item)
        else:
            return binary_search_rec(a_list[first:midpoint], item)

print('Version 3')
print(binary_search_rec(test_list, 3))
print(binary_search_rec(test_list, 13))
print(binary_search_rec(test_list2, 8))