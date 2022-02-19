from typing import List

def sort_list(unsorted_list: List[int]) -> List[int]: # This uses type hinting. unsorted_list will be a List with int and expect a List with ints to be returned
    for i, entry in enumerate(unsorted_list): # want to be able to use the index, hence enumerate
        current = i
        while current > 0 and unsorted_list[current] < unsorted_list[current-1]:
            unsorted_list[current], unsorted_list[current - 1] = unsorted_list[current - 1], unsorted_list[current]
            current -= 1
    return unsorted_list

if __name__ == '__main__':
    # unsorted_list = [int(x) for x in input().split()]
    unsorted_list = [5, 3, 4, 2, 1]
    res = sort_list(unsorted_list)
    print(' '.join(map(str, res)))
