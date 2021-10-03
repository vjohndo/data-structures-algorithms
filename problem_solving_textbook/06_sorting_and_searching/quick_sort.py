def partition(a_list, first, last):
    # Assume the pivot value is the first
    # first and last refer to indexes

    pivot_value = a_list[first]
    left_mark = first + 1
    right_mark = last
    done = False

    # Keep moving markers until these different scenario's are completed
    while not done:

        # keep incrementing the left mark so long as you don't hit a value 
        # we are keeping <= and >= for the next two while loops as we are just moving along the list to find a 
        # index on the wrong side
        while left_mark <= right_mark and a_list[left_mark] <= pivot_value:
            left_mark += 1
        
        while left_mark <= right_mark and a_list[right_mark] >= pivot_value:
            right_mark -= 1
        
        # if we've gotten out of those while loops the marks have swapped side, 
        # it must be the case that everything is on the right side of the pivot
        if left_mark > right_mark:
            done = True

        # Otherwise we'll need to do swaps 
        else:
            a_list[left_mark], a_list[right_mark] = a_list[right_mark], a_list[left_mark]

    # If we've gotten out of the above while loop, we've reached the convergence point
    # swap the pivot value with the right mark (which is presiding on the true convergence point)
    a_list[first], a_list[right_mark] = a_list[right_mark], a_list[first]

    # The right mark it the pivot point / convergence point
    return right_mark


def quick_sort_helper(a_list, first, last):
    # Base case, if the size of the list if > 1 i.e. first and last index are not the same 
    # DO NOTHING

    if first < last:

        # Splitting progresses to the base case.
        split = partition(a_list, first, last)

        # After calling the partition you'll get a "pivoted" list
        # call the helper functions on both of those sides again
        # note that partition is acting on the original array hence why we keep passing through a_list and have split - 1 and split + 1
        quick_sort_helper(a_list, first, split - 1)
        quick_sort_helper(a_list, split+1, last)


def quick_sort(a_list):
    quick_sort_helper(a_list, 0, len(a_list) - 1)

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort(a_list)
print(a_list)