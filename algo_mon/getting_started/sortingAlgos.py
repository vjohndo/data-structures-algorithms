from typing import List

# Algo monster version
def sort_list(unsorted_list: List[int]) -> List[int]: # This uses type hinting. unsorted_list will be a List with int and expect a List with ints to be returned
    for i, entry in enumerate(unsorted_list): # want to be able to use the index, hence enumerate
        current = i
        while current > 0 and unsorted_list[current] < unsorted_list[current-1]:
            unsorted_list[current], unsorted_list[current - 1] = unsorted_list[current - 1], unsorted_list[current]
            current -= 1
    return unsorted_list

# Text book version - not inplace as you need additional storage for data
def sort_list(unsorted_list: List[int]) -> List[int]:
    """Sort list of comparable elements in non-decreasing order"""
    for i in range(1,len(unsorted_list)):
        current = unsorted_list[i]
        j = i
        
        while j > 0 and unsorted_list[j-1] > current:
            unsorted_list[j] = unsorted_list[j-1]
            j -= 1
            
        unsorted_list[j] = current
            
    return unsorted_list

def sort_list(unsorted_list: List[int]) -> List[int]:
    """Selection sort."""
    # This implementation is not stable.
    
    i = 0
    
    while i < len(unsorted_list): # Resets the indeces and swaps
        j = i
        min_index = i
        
        while j < len(unsorted_list): # Finds the min of the list
            if unsorted_list[j] < unsorted_list[min_index]:
                min_index = j
            j += 1
        
        
        unsorted_list[min_index], unsorted_list[i] = unsorted_list[i], unsorted_list[min_index]
        i += 1
    
    return unsorted_list

def sort_list(unsorted_list: List[int]) -> List[int]:
    """Selection sort - my own stable implementation + inplace"""
    
    n = len(unsorted_list)
    i = 0
    
    while i < n:
        j = n - 1
        
        while j > i:
            if unsorted_list[j] < unsorted_list[j-1]:
                unsorted_list[j], unsorted_list[j-1] = unsorted_list[j-1], unsorted_list[j]
            j -= 1
        
        i += 1
    
    return unsorted_list

def sort_list(unsorted_list: List[int]) -> List[int]:
    """Selection sort - version2 - my own stable implementation + inplace"""
    
    n = len(unsorted_list)
    
    for i in range(n): # 0, 1, 2, ..., n-1
       
        for j in range(n-1, i, -1): # for n-1, n-2, ..., i+1 i.e. in the unsorted partition
            if unsorted_list[j] < unsorted_list[j-1]:
                unsorted_list[j], unsorted_list[j-1] = unsorted_list[j-1], unsorted_list[j]
    
    return unsorted_list

def sort_list(unsorted_list: List[int]) -> List[int]:
    """Selection sort - AlgoMonster implementation. Not stable. In-place"""
    
    n = len(unsorted_list)
    
    for i in range(n):
        min_index = i # for each outer loop iteration initiate min index at start
        
        for j in range(i , n): # create another loop
            if unsorted_list[j] < unsorted_list[min_index]:
                min_index = j
        
        # swap out the found min index with current index
        unsorted_list[i], unsorted_list[min_index] = unsorted_list[min_index], unsorted_list[i]
    
    return unsorted_list

if __name__ == '__main__':
    # unsorted_list = [int(x) for x in input().split()]
    unsorted_list = [5, 3, 4, 2, 1]
    res = sort_list(unsorted_list)
    print(' '.join(map(str, res)))
