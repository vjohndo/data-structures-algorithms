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

def sort_list(unsorted_list: List[int]) -> List[int]:
    """Bubble sort - my own implementation"""
    
    swapped = True
  
    while swapped:
        swapped = False
        i = 0
        
        while i < len(unsorted_list) - 1:
            if unsorted_list[i] > unsorted_list[i + 1]:
                unsorted_list[i], unsorted_list[i + 1] = unsorted_list[i + 1], unsorted_list[i]
                swapped = True
            i += 1
    
    return unsorted_list

def sort_list(unsorted_list: List[int]) -> List[int]:
    """Bubble sort - algo monster"""
    # Want to iteration from 1 --> n, 1 --> n-1, 1 --> n-2 etc. 
    # so use reverse range
    n = len(unsorted_list)
    for i in reversed(range(n)): 
        swapped = False
        for j in range(i):
            if unsorted_list[j] > unsorted_list[j + 1]:
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
                swapped = True
        if not swapped:
            return unsorted_list # early return if was can sort it before all iterations
    
    return unsorted_list # if it takes the final iteration to sort the list
    

def sort_list(unsorted_list: List[int]) -> List[int]:
    """Merge sort implementation. Algo monster"""
    
    n = len(unsorted_list)
    if n <= 1: # base case, will only return on single, all other activation frames will have merge sort
        return unsorted_list
    
    # Midpoint will be used to track poiners on left_list and right_list 
    midpoint = n // 2
    # split the list into two...
    # left list upto (but not including) but not including midpoint
    # right list from midpoint until the end
    left_list, right_list = sort_list(unsorted_list[:midpoint]), sort_list(unsorted_list[midpoint:])
    result_list = []
    left_pointer, right_pointer = 0, 0
    
    # The left and right pointers are the for the left and right list
    # the conditions are set up so that the while loop keeps running until all sublists have added to results
    while left_pointer < midpoint or right_pointer < n - midpoint: # right pointer to go through all nodes not captured in midpoint
        # notice that by having the or in the while loop, we need to account for that in our control logic
        if left_pointer == midpoint: # all left pointer exhausted add in right
            result_list.append(right_list[right_pointer])
            right_pointer += 1
        elif right_pointer == n - midpoint: # all right pointer exhausted add in left
            result_list.append(left_list[left_pointer])
            left_pointer += 1
        elif left_list[left_pointer] <= right_list[right_pointer]: # notice how it is <= for stability. left will receive priority
            result_list.append(left_list[left_pointer])
            left_pointer += 1
        else:
            result_list.append(right_list[right_pointer])
            right_pointer += 1
        
    return result_list

def sort_list_interval(unsorted_list: List[int], start: int, end: int) -> List[int]:
    """
    Quick sort implementation.
    
    end    upto but not including. it will be the len(List). look at the helper function.
    start  including
    """

    # If there's 1 item or less return 1
    # right inclusivity --> a[i:i] ==> len(a) = 0
    if end - start <= 1: # If the starting index and end index dif is <= 1. I.e. start and end pointers will be refer to the same element.
        return # We are doing this inplace so need to actually return anything but need to exit the recursion.
    
    pivot = unsorted_list[end-1] 
    start_ptr = start
    end_ptr = end - 1
    
    while start_ptr < end_ptr:
        while unsorted_list[start_ptr] < pivot and start_ptr < end_ptr: # notice how we use "<" to keep the sort stable? If we land on a value equal it doesn't count.
            start_ptr += 1
        while unsorted_list[end_ptr] >= pivot and start_ptr < end_ptr: # notice how >= to maintain stability. If we land on a value = to pivot. we will leave the right marker here to swap. As the left marker progresses, the pivot will definitely be infront
            end_ptr -= 1
        if start_ptr == end_ptr: # already created a left and right side 
            break # do no progress the loop and no need to swap anymore.

        # we swap with the start first because it will always move first (look at the order of the while loop)
        unsorted_list[start_ptr], unsorted_list[end_ptr] = unsorted_list[end_ptr], unsorted_list[start_ptr]
        
    # swap the pivot
    unsorted_list[start_ptr], unsorted_list[end - 1] = unsorted_list[end - 1], unsorted_list[start_ptr]
    
    # now sort the left and right intervals
    sort_list_interval(unsorted_list, start, start_ptr)
    sort_list_interval(unsorted_list, start_ptr + 1, end)
    
        
def sort_list(unsorted_list: List[int]) -> List[int]:
    sort_list_interval(unsorted_list, 0, len(unsorted_list))
    return unsorted_list

if __name__ == '__main__':
    # unsorted_list = [int(x) for x in input().split()]
    unsorted_list = [5, 3, 4, 2, 1]
    res = sort_list(unsorted_list)
    print(' '.join(map(str, res)))
