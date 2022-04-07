from typing import List

def peak_of_mountain_array(arr: List[int]) -> int:
    left, right = 0, len(arr) - 1
    boundary_index = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > arr[mid + 1]:
            boundary_index = mid
            # We know the solution must at least lie to our left,
            # So we bring the right back
            right = mid - 1
        else:
            left = mid + 1

    return boundary_index

if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    res = peak_of_mountain_array(arr)
    print(res)