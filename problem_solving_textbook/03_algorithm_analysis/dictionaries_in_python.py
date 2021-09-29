"""
Understanding python's implementation of dictionaries by:
> Confirming that contains for list is O(n)
> Confirming that contains for dictionaries is O(1)
> We will learn more about dictionary implementations later in the book

Lessons Learnt:
- DICTIONARY COMPREHENSION!! {j:None for j in range(i)}
-
"""

# Make a list with a range of numbers in it, rane it dictionaries except numbers of keys
# Pick numbers at random to check if numbers are in the list
import timeit
import random

# creating a list of numbers, and checking if random number is in that list (which is will be)
for i in range(10000,1000001,20000):
    t = timeit.Timer("random.randrange(%d) in x"%i, "from __main__ import random,x")

    x = list(range(i))
    lst_time = t.timeit(number=1000)
    x = {j:None for j in range(i)}
    d_time = t.timeit(number=1000)
    print("%d,%10.3f,%10.3f"%(i, lst_time, d_time))


