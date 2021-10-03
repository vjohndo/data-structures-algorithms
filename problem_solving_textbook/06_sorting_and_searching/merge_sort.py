def merge_sort(a_list):
    # Merge sort breaks down a list to two halves and once the base case is met, merges them back in to the ORIGINAL list

    print("Splitting", a_list)
    
    # Base case is do nothing, if the length of the list is less than or equal to one, we already have a sorted list

    # Progression to the base case is achieved via splitting
    if len(a_list) > 1:
        mid = len(a_list) // 2
        # Add in the start and end so slice becomes O(1) as we specfiy the start and end
        start = 0
        end = len(a_list)
        
        left_half = a_list[start:mid]
        right_half = a_list[mid:end]

        merge_sort(left_half)
        merge_sort(right_half)

        # At this point, we will have split down to a "left_half" and "right_half" sub list 
        # the below code will combine these sub lists back

        # Let's define some counters that tracks the current positions in three lists we need to manage
        # i looks after the 'left_half' --> current index within the sub list to be merged
        # j looks after the 'right_half' --> current index within the sub list to be merged
        # k looks after the merged array --> current index in the merged list to have an item assigned

        i, j, k = 0, 0, 0

        # so long as i and j are less than the length of the sorted sub array 
        while i < len(left_half) and j < len(right_half):
            """For the case where we have two lists"""

            # should the current index in the left half be greater, add to merged list and increment i
            # notice how this is <= to ensure the function is stable MAINTAINS the order of duplicate items 
            # I.e. we want the LHS to go first if there is an equal item in the RHS 
            if left_half[i] <= right_half[j]:
                a_list[k] = left_half[i]
                i = i + 1

            # otherwise add the right hald to the merge list and increment j
            else:
                a_list[k] = right_half[j]
                j = j + 1

            # would have added something to the merged list so increase the counter
            k = k + 1

        while i < len(left_half):
            """ For the case where only the left side has items to add"""
            a_list[k] = left_half[i]
            i = i + 1
            k = k + 1


        while j < len(right_half):
            """ For the case where only the right side has items to ad"""
            a_list[k] = right_half[j]
            j = j + 1
            k = k + 1
        
        print("Merging", a_list)
        
a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
merge_sort(a_list)
print(a_list)