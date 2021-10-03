def selection_sort(a_list):
    """This implementation moves the smallest numbers to the front of the list"""
    for i, item in enumerate(a_list):
        # We have kept track of i, item


        # Keep track of the last index, this is where we will make an exchange
        # For now we will initialise it as the last index
        min_index = len(a_list) - 1

        for j in range(i, len(a_list)):
            if a_list[j] < a_list[min_index]:
                min_index = j

        # After discovering what the smallest index, if it's not the start of the sub list
        # Make an exchange
        if min_index != i:
            a_list[min_index], a_list[i] = a_list[i], a_list[min_index]

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selection_sort(a_list)
print(a_list)

def selection_sort2(a_list):
    """Implementation moves the largest number to the end of the list"""
    # Consider which has better performance?
    # This one is probably worse as you need to keep making exchanges near the front which 'ripple' through to the end
    # The front of list implementation will have a reduced ripple area

    # Iterating through the list backwards, 
    for i in range(len(a_list) - 1, 0, -1):

        # Keep track of max index, let's initialise it at the start of the sub list
        max_index = 0

        # Note that range is up to but not including i, since we've deducted one before need to add back in for range to work
        for j in range(i + 1):

            # Go through and identify the max value
            if a_list[j] > a_list[max_index]:
                max_index = j
        
        # Make an exchange so long as the max value isn't already at the end of the list
        if max_index != i:
            a_list[max_index], a_list[i] = a_list[i], a_list[max_index]

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selection_sort2(a_list)
print(a_list)
        