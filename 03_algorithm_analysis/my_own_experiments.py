"""
lessons learned: deleting something is considered: del alist[i], del adict[i]
{{ }} for string to out put { }

1) Set up a loop that increments 
for x in range(100000,10000001,100000)

2) import timeit, to track the function time

3) import random, this will us pick a random index value 

4

"""

import timeit
import random

"""
Devise an experiement to verify that the list index operator is O(1)
"""
def experiment1():
    for i in range(10000,1000001,20000):
        test = timeit.Timer(f'incrementing_list[random.randrange({i})]', 
                        "from __main__ import random, experiment1, incrementing_list1")

        # Takes the range, can converts it to a list
        global incrementing_list1 
        incrementing_list1 = list(range(i))
        list_timer = test.timeit(number=1000)

        print(f"{i}, {list_timer}")

# experiment1()
"""
Devise an experiment to verify that get items and set item are O(1) for dictionaries
"""

def experiment2():
    for i in range(10000,10000001,20000):
        test_get = timeit.Timer(f"incrementing_dict2.get(random.randrange({i}))",
                            "from __main__ import random, experiment2, incrementing_dict2")
        test_set = timeit.Timer(f"incrementing_dict2[random.randrange({i})] = random.randrange({i})",
                            "from __main__ import random, experiment2, incrementing_dict2")

        global incrementing_dict2
        incrementing_dict2 = {num:None for num in range(i)}
        dict_time_get = test_get.timeit(number=1000)
        dict_time_set = test_set.timeit(number=1000)

        print(f"{i}: get time {dict_time_get} | set time {dict_time_set}")

# experiment2()

"""
Devise an experiement that compares the performance of the del operator on lists and dictionaries
    > As you loop the through the timit, it deletes values and may randomly call on deleted keys.
    > As the dictionary will be pass by reference... this is an issue.
    > Following tests try to circumvent this.
"""

# This experiment fails as dct.keys() is O(n)
def experiment3():
    for i in range(10000,200001,20000):
        # creating object.keys is O(n)... fail.. let's try 
        lst_test = timeit.Timer(f"del lst_object3[random.choice(range(len(lst_object3)))]",
                            'from __main__ import random, experiment3, lst_object3')
        
        global lst_object3
        lst_object3 = list(range(i)) 
        lst_time = lst_test.timeit(number = 1000)

        dct_test = timeit.Timer(f"del dct_object3[random.choice(list(dct_object3.keys()))]",
                            'from __main__ import random, experiment3, dct_object3')

        global dct_object3
        dct_object3 = {num:None for num in range(i)}
        dct_time = dct_test.timeit(number = 1000)

        print(f"{i}: list-time = {lst_time} || dict-time = {dct_time}")

# I try to regenerate the list & dict objects but both are O(n) and I would not be able to demonstrate a constant relationship
def experiment3A():
    for i in range(10000,200001,20000):
        lst_test = timeit.Timer(f"del list(range({i}))[random.randrange({i})]",
                                'from __main__ import random')
        
        lst_time = lst_test.timeit(number = 1000)


        # generating a new dictionary is O(n)
        dct_test = timeit.Timer(f"del {{num:None for num in range({i})}}[random.randrange({i})]",
                                'from __main__ import random')
        
        dct_time = dct_test.timeit(number = 1000)
        
        print(f"{i}: list-time = {lst_time} || dict-time = {dct_time}")
        
# experiment3A() - Success, after each deletion, add back something to the object which is stil and O(1) event. 
def experiment3B():
    for i in range(10000,1000001,20000):
        
        global index3b
        index3b = random.randrange(i)
        
        global lst_object3b
        lst_object3b = list(range(i))
        lst_test = timeit.Timer(f"del lst_object3b[index3b] \nlst_object3b.append(index3b)",
                                'from __main__ import random, lst_object3b, index3b')
        
        lst_time = lst_test.timeit(number = 100000)

        global dct_object3b
        dct_object3b = {num:None for num in range(i)}

        dct_test = timeit.Timer(f"del dct_object3b[index3b]\ndct_object3b[index3b] = None",
                                'from __main__ import random, dct_object3b, index3b')
        
        dct_time = dct_test.timeit(number = 100000)
        
        print(f"{i}: list-time = {lst_time} || dict-time = {dct_time}")
        
# experiment3B()

"""
# Given a list of number in random order write and algorithm that works in O(nlog(n)) to kind the kth smallest num
"""
def experiment4():
    for i in range(10000,10000001,20000):
        # Generate a global list object and through each loop create a list
        global lst4
        lst4 = list(range(i))
        random.shuffle(lst4)

        lst_test = timeit.Timer("lst4.sort()\nlst4[0]","from __main__ import lst4")
        lst_time = lst_test.timeit(number = 1000)

        print(f"{i}: list-min-time = {lst_time}")

# experiment4()
    
"""
Can you imporve the algorithm form the proveious prblem to be linear? Explain...
    > Count and compare, counting is a O(n)
"""

def experiment5():
    for i in range(10000,10000001,20000):
         # Generate a global list object and through each loop create a list
        global lst5
        lst5 = list(range(i))
        random.shuffle(lst5)

        lst_test = timeit.Timer("experiment5c(lst5)","from __main__ import lst5, experiment5c")
        lst_time = lst_test.timeit(number = 1000)

        lst_test_2 = timeit.Timer("experiment5b(lst5)","from __main__ import lst5, experiment5b")
        lst_time_2 = lst_test_2.timeit(number = 1000)


        print(f"{i}: list-min-time O(nlog(n)) = {lst_time} || list-min-time O(n) = {lst_time_2}")

def experiment5a(lst):
    min_int = lst[0]
    for x in lst:
        if x < min_int:
            min_int = x
    return min_int

def experiment5b(lst):
    return min(lst)

def experiment5c(lst):
    lst.sort()
    return lst[0]

rand_list = [-123,424,424,424020,-123,43]
print(experiment5b(rand_list))
print(experiment5c(rand_list))

experiment5()