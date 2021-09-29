""" 
Pop both ends and compare 
"""

from pythonds3.basic import Deque

def pal_checker(a_string):
    char_deque = Deque()

    for ch in a_string:
        char_deque.add_front(ch)
    
    # Note that there may be a middle letter 
    while char_deque.size() > 1:
        first = char_deque.remove_front()
        second = char_deque.remove_rear()
        if first != second:
            return False

    return True

print(pal_checker("lsdkjfskf"))
print(pal_checker("radar"))
    