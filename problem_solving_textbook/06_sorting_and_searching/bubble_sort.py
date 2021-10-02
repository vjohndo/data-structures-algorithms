def bubble_sort(a_list):
    """ Basic Bubble Sort """
    # At the start we will need to consider whole array n
    # however after each pass, we know we've placed another number in the right spot and can increment to n-1
    for i in range(len(a_list) - 1, 0, -1):

        # Go through each index that is still "unsorted"
        for j in range(i):

            # should the next index be larger, do a swap using a temp assigment
            if a_list[j] > a_list[j+1]:
                temp = a_list[j]
                a_list[j] = a_list[j+1]
                a_list[j + 1] = temp

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubble_sort(a_list)
print(a_list)

def bubble_sort_short(a_list):
    for i in range(len(a_list)-1,0,-1):

        # Initialise a variable to track if exchanges have been made
        # Assume that no exchanges have been so that for each pass, if there have been no exchanges
        # We can break from the outer for loop (don't break from the inner for loop!)
        exchanges = False

        # Make a first pass and check to keep track of whether an exchange was made
        for j in range(i):

            if a_list[j] > a_list[j+1]:
                exchanges = True
                a_list[j] , a_list[j+1] = a_list[j+1], a_list[j]

        # After this pass, if no exchanges were made, list must sorted, break!
        if not exchanges:
            break

a_list = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
bubble_sort_short(a_list)
print(a_list)

