from typing import List

def find_boundary(arr: List[bool]) -> int:
    left, right = 0, len(arr) - 1
    # Instead of modifying the loop logic
    # We keep track of the boundary index... default is -1
    boundary_index = -1

    while left <= right:
        mid = (left + right) // 2
        # In this while loop we aren't concerend with espacing early
        # We want to keep it iterating until we reach the boundary
        # Effectively each iteration of the loop is a smaller version of the problem
        # e.g. [F, F, T, T, T, T] --> [F, F, T] --> [F, T] --> [T]
        if arr[mid]:
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return boundary_index

if __name__ == '__main__':
    arr = [x == "true" for x in input().split()]
    res = find_boundary(arr)
    print(res)

### My implementation

def find_boundary(arr: List[bool]) -> int:
    left, right = 0, len(arr) - 1
    boundary_index = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid]:
            # My method modifies the loop logic 
            if mid == 0 or arr[mid-1] is False:
                return mid
            else:
                right = mid - 1
        else:
            left = mid + 1

    return -1

