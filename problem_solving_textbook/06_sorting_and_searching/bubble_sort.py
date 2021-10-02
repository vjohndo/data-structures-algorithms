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

