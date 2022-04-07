from typing import List

def feasible(weights: List[int], max_weight: int, d: int) -> int:
    # Easier to compare required days than days left
    # That way you don't have to account for left over packages in algorithm
    req_days = 1
    capacity = max_weight
    i = 0
    n = len(weights)
    while i < n:
        if weights[i] <= capacity:
            capacity -= weights[i]
            i += 1
        else:
            req_days += 1
            capacity = max_weight
    return req_days <= d

def min_max_weight(weights: List[int], d: int) -> bool:
    # Know that the min size will be the max size of package
    min_ptr = max(weights)
    max_ptr = sum(weights)
    boundary_index = max_ptr
    while min_ptr <= max_ptr:
        midpoint = (min_ptr + max_ptr) // 2
        if feasible(weights, midpoint, d):
            boundary_index = midpoint
            max_ptr = midpoint - 1
        else:
            min_ptr = midpoint + 1
    return boundary_index

if __name__ == '__main__':
    weights = [int(x) for x in input().split()]
    d = int(input())
    res = min_max_weight(weights, d)
    print(res)

## My solution

def feasible(max_weight: int, weights: List[int], d:int) -> bool:
    
    days_left = d
    truck_weight = 0
    i = 0
    
    while days_left > 0 and i < len(weights):
        
        if truck_weight + weights[i] > max_weight:
            # Drop day counter and reset truck weight
            days_left -= 1
            truck_weight = 0
        else:
            truck_weight += weights[i]
            i += 1
    
    if i < len(weights):
        return False
    else:
        return True
        

def min_max_weight(weights: List[int], d: int) -> int:
    sum_weights = sum(weights)
    
    left, right = 1, sum_weights
    truck_weight = -1
    
    while left <= right:
        mid = (left + right) // 2
        if feasible(mid, weights, d):
            truck_weight = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return truck_weight
        