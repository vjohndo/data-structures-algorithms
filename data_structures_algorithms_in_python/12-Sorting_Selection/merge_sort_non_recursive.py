import math


def merge(src, result, start, inc):
    """Merge src[start:start + inc] and src[start+inc:start+2*inc] into result"""
    end1 = start+inc                    # boundary for run 1, inc is increment
    end2 = min(start+2*inc, len(src))   # boundary for run 2 

    x, y, z = start, start+inc, start   # index into run 1, run 2 result
    # note that x is the walk for the first run, y is walk for second run, z is walk for the destination list 

    while x < end1 and y < end2: 
        # While there are still items to be added in both the first run (walked by x) and second run (walked by y)
        if src[x] < src[y]:
            result[z] = src[x]
            x += 1
        else:
            result[z] = src[y]
            y += 1
        z += 1 # increment the z walk for the results list

    # After one of the lists are empty, add the rest in.
    if x < end1:
        result[z:end2] = src[x:end1]
    elif y < end2: # Notice the use of elif.... not sure why, try to justify it one day
        result[z:end2] = src[y:end2]

def merge_sort(S):
    """Sort the elments of Python list S using the merge-sort algorithm"""
    n = len(S)
    logn = math.ceil(math.log(n,2)) # rounds up to the next largest number of of the log of n.. this will be used as the increment
    src, dest = S, [None] * n # create stoarge for the destination

    for i in (2**k for k in range(logn)): # go through 2^1, 2^2, 2^3 etc.. until you reach 2^i = n) e.g. 2, 4, 8 (this defines length of runs)
        for j in range(0, n, 2*i): 
            # each pass merges two i length runs e.g.
            # i = 1,  j = iter[0, 2, 4, 6, 8, 10, 12, 14, 16] ==> combines into ordered groups of two
            # i = 2,  j = iter[0, 4, 8, 12, 16] ==> combines into ordered groups of four
            # i = 3,  j = iter[0, 8] ==? combines into ordered groups of 8
            # etc...
            merge(src, dest, j, i) 
        src, dest = dest, src # reverse the roles of lists

    # Finally copy it over. throw in an if statement to avoid doing double work.
    if S is not src:
        S[0:n] = src[0:n] # additional copy to get results to S i.e. copy results for SRC to S