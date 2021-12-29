from array_stack import ArrayStack

def is_matched(expr):
    """Return True if all delimiters are properly matched"""

    # Define opening and respective closing delimiters 
    lefty = '({['
    righty = ')}]'

    # Instantiate 
    S = ArrayStack()

    # Go each character in the expression
    # this would be be an O(n)
    for c in expr:

        # If the character is in the lefty delimiter 
        if c in lefty:
            
            # Push it on to the stack
            S.push(c)

        # if the character is a closing delimeter
        elif c in righty:

            # check if the stack is empty, if so return false
            # this event would trigger if we have too many closing delimiters 
            if S.is_empty():
                return False
            
            # check the indexes of the opening and closing delimiters aren't matched
            # i.e. find the index of the clsoing delimiter within the string
            # then find the index of the opening delimiter within the opening string from the top item in the lefty index
            # becuase indexing is constant as lefty and righty are constant sizes, this is an O(1)
            if righty.index(c) != lefty.index(S.pop()):
                return False

    # After iterating through the expression, return whether the stack is populated
    return S.is_empty()