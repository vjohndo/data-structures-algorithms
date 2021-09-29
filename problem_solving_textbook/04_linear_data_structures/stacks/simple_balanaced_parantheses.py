"""
Application of stacks
    > Consider a series of (()()()())()... is this balanced
    > Let's push onto a stack, and should there be a closed back pop the stack
    > If the stack is empty by the end of it, it should be balanced
"""

from pythonds3.basic import Stack

## Let's define a parenthesis checker
def par_checker(symbol_string):

    # Initialise our stack
    s = Stack()

    # Let's now go through each symbol in the string
    for symbol in symbol_string:
        if symbol == "(":
            s.push(Stack)
        # If we've got a closing parenthesis but the stack is empty, it's unbalanced
        elif s.is_empty():
            return False
        # Otherwise we are fine to pop
        else: 
            s.pop()
    
    # We've now gotten to the end of the loop
    # Need to check if the stack is empty, i.e. all open brackets have been accounted for
    # Since the is_empty() method is already a boolean, can return that directly
    return s.is_empty()

print(par_checker("((()))"))
print(par_checker("((()()))"))
print(par_checker("(()"))
print(par_checker(")("))


        

