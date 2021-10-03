def selection_sort(a_list):
    
    # We start by considering the first item in the list as being sorted, hence range from 1 instead of 0
    for i in range(1, len(a_list)):
        
        # Grab the current value (we are effectively pulling it out of the list)
        insertion_value = a_list[i]

        # Grab the current position (we can shift right an existing value of the sub list to this position)
        current_position = i

        # Go through the sublist and check, but prgressing backwards
        # While there is still space and the next value is > current value
        # Note that next value is progression in this direction <--
        # Note that we have current_position > 0 because the shifting right mechanism does the assignment to our current cell... if we are on the 0th index, can't do that assigment
        while current_position > 0 and a_list[current_position - 1] > insertion_value:
            
            # Shift the value right and increment to the next position
            a_list[current_position] = a_list[current_position - 1]
            current_position -= 1

        # If we're out of that loop, that means the next position is either small or None
        # the current position will have already been shifted right so make the assignment
        a_list[current_position] = insertion_value



        

    

        
