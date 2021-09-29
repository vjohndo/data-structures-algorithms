""" 
Goal is to write a boolean function that takes two strings and returns whether they are anagrams
> lessons learned:
    - Always think, can you init a variable to make this easier to do?
    - When tracking items:
        > count and compare the iterables
        > sort and compare
        > checklist 
        > ord converts a character inti it's unicode code
"""

import time

# MY ATTEMPT: with list popper ... loses out to to sorter
# Could initialise a variable that checks if the character is not in anagram its of
def anagramChecker(str1,str2):
    
    start = time.time()

    if len(str1) != len(str2): # good idea to make function that checks if length is the same
        end = time.time()
        return False,end-start

    str2_list = list(str2) # can just pass into a list class instead of [x for x in str2]

    for char1 in str1:
        isOkay = False # variable to break on no match [from anagramSolution 1]

        for i,char2 in enumerate(str2_list):
            # print(char1,char2)
            if char1 == char2:
                str2_list.pop(i)
                isOkay = True
                break
        
        if isOkay == False:
            break # variable to break on no match [from anagramSolution 1]
    
    if len(str2_list) == 0:
        end = time.time()
        return True,end-start
    else:
        end = time.time()
        return False,end-start
    
    

print(anagramChecker('earth','htrae')) 

# Solution 1: Checklist
def anagramSolution1(s1,s2):

    start = time.time()

    stillOK = True # stillOK variable 
    if len(s1) != len(s2):
        stillOK = False # if not the same length, set to false

    alist = list(s2) # pass the string to a list
    pos1 = 0 # init a counter variable

    while pos1 < len(s1) and stillOK: 
        pos2 = 0
        found = False # init a found variable, setting it to false, looking a match, at which case we will set to true
        while pos2 < len(alist) and not found: # loop through the second string, stop if not yet found 
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1 # increment the counter

        if found:
            alist[pos2] = None # after looping through the second string, if found set the current list item to None i.e. CHECK IT OFF THE LIST.
        else:
            stillOK = False # nothing is found and not okay, no more looping
        
        pos1 = pos1 + 1

    end = time.time()

    return stillOK,end-start

print(anagramSolution1('earth','htrae'))
    
# Solution 2: Sort & Compare
def anagramSolution2(s1,s2):

    """
    sort is either n^2 or nlog(n), while loop on it's own would be n
    """

    start = time.time()

    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if alist2[pos] != alist2[pos]:
            return False

        pos = pos + 1

    end = time.time()
    return matches,end-start

print(anagramSolution2('earth','htrae'))


# Solution 3: Brute force n!...

# Solution 4: Count and compare, but at the cost of storage time complexity O(n) = n, T(n) = 2n + 26

def anagramSolution4(s1,s2):

    start = time.time()

    # Create a list with length 26 to store characters
    c1 = [0]*26
    c2 = [0]*26

    # ord converts a string to it's unicode value
    # position sets the index for the c1/c2 lists by reducing the unicode value of a
    # then at that position of the c1/c2 list, add the counter
    for i in range(len(s1)):
        pos = ord(s1[i])-ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i])-ord('a')
        c2[pos] = c2[pos] + 1

    # go through each index of the list and make sure they are matching. 
    j = 0
    stillOK = True
    while j<26 and stillOK:
        if c1[j] == c2[j]:
            j = j + 1
        else:
            stillOK = False
    
    end = time.time()

    return stillOK,end-start

print(anagramSolution4('earth','htrae'))