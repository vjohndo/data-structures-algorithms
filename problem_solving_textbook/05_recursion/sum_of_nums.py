"""
STANDARD WAY YOU'VE BEEN DOING SUMS
    > An accumulator
    > Iteration
"""
def list_sum(num_list):
    the_sum = 0

    for i in num_list:
        the_sum = the_sum + i
    
    return the_sum

print(list_sum([1,3,5,7,8]))


"""
THE SUM OF A LIST IS 1st ITEM IN THE LIST + THE SUM OF REMAINING ITEMS
"""

def list_sum_recursive(num_list):
    # Base case
    if len(num_list) == 1:
        # We know that if there is only one item in a list, the sum of that list will be the number
        # This is our base case or escape clause - stops the algorithm from recursing
        return num_list[0]
    else:
        # We'll pull out the first number and pass the rest into the function
        # Note that this step we progress towards a base case and call the function again
        return num_list[0] + list_sum(num_list[1:])

print(list_sum_recursive([1,3,5,7,8]))