"""

Practical demonstration of linear vs quadratic 

"""

arb_list = [1,6545,2,424,523,53,-1,2]

import time
from random import randrange

# Linear implementation O(n) = n
def lin_min(num_list):
    min_n_lin = num_list[0]
    for num in num_list:
        if num < min_n_lin:
            min_n_lin = num

    return min_n_lin

# Quadratic implementation O(n) = n^2
def quad_min(num_list):
    min_n_quad = num_list[0]
    for num in num_list:
        isSmallest = True
        # Needs to go through all other numbers and return only if it's the smallest
        # as soon as it is bigger than any number it's not the smallest... this is the type of check you should keep a lookout for
        for other_num in num_list:
            if num > other_num:
                isSmallest = False
                
        if isSmallest:
            min_n_quad = num
    
    return min_n_quad

print(lin_min(arb_list))
print(quad_min(arb_list))


# Time tester
for listSize in range(1000,10001,1000): #1000, 2000, 3000, etc..
    
    alist = [randrange(100000) for x in range(listSize)]
    start = time.time()
    print(lin_min(alist))
    end = time.time()
    print("size: %d time: %f" % (listSize,end-start))