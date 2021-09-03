"""
Recursion is implemented via stacks and stack frames
Let's try to implement this on our string conversion 
"""
from pythonds3.basic import Stack

def to_str(n,base):
    recursion_stack = Stack()
    convert_string = "0123456789ABCDEF"

    # Until we get down to a zero digit
    while n > 0 :
        if n < base:
            # This is the base case, we can instantly convert the value over
            recursion_stack.push(convert_string[n])
        else:
            # Push the remainder into stack to recreate is
            recursion_stack.push(convert_string[n % base])

        # Need to progress n towrads the base case with floor div //
        n = n // base

    # After creating the stack, let's assemble all the remainders to a string
    recursion_string = ""

    # Using the stack method, keep doing the following until the stak is empty
    while not recursion_stack.is_empty():
        recursion_string = recursion_string + str(recursion_stack.pop())
    
    return recursion_string

print(to_str(1453, 16))

