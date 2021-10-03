def gap_insertion_sort(a_list, start, gap):
    """ Gap insertion sort algorithm """

    # Need to iterate over the list but with that gap
    # Remeber that we assume the first item in an in inertion sort is sorted hence gap + start
    for i in range(start + gap, len(a_list), gap):

        insertion_value = a_list[i]
        current_position = i

    # As this is a sublist, need to make sure we don't traverse beyond start of the sublist0
    while current_position > start and a_list[current_position - gap] > insertion_value:

        a_list[current_position] = a_list[current_position - gap]
        current_position -= gap
    
    a_list[current_position] = insertion_value

def shell_sort(a_list):
    # We are going to keep running multiple passes of shells
    # This sublist count will be based on gap = length/2 but will keep increasing to gap = length4 etc.
    # Eventually this will progress to a gap size of 1 where we would be effectively doing pure insertion sort
    sublist_gap = len(a_list)//2

    while sublist_gap > 0:
        # Note that given the gap i.e. sublist count, we would only need to iterate over the possible sublists which 
        for pos_start in range(sublist_gap):
        # Use the gap insertion sort, supplying the starting position + gap
            gap_insertion_sort(a_list, pos_start, sublist_gap)
        
        print("After increments of size", sublist_gap, "the list is", a_list)

        # Progress towards single gap sublist
        sublist_gap = sublist_gap // 2

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shell_sort(a_list)
print(a_list)
