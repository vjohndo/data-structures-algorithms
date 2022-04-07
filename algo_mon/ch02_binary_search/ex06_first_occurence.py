from typing import List

def find_first_occurrence(arr: List[int], target: int) -> int:
    
    left, right = 0, len(arr) - 1
    nearest_index = -1
    
    # [1, 3, 3, 3, 3, 4] ==> [1,3]
    # [0, 1, 2, 3, 4, 5] ==> [0,1]
    
    while left <= right:
        mid = (left + right) // 2
        # If it's a matched we update the nearest index
        # We will need to continue the binary search as there may be a smaller working index
        if arr[mid] == target:
            nearest_index = mid
            right = mid - 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    
    return nearest_index
