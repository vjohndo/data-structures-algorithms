""" 
Infix to prefix conversion

"""

from pythonds3.basic import Stack

def infix_to_postfix(infix_expr):

    # Let's first create a dictionary that contains precedence levels for each operand
    # "(" --> 1will always let others ops go first, (more waiting for ")" to come along ) -- >1
    # "+-" --> 2 always will let "/*" go first
    # "/*" --> always goes before everything
    # ")" --> None, doesn't matter, if this is coming, it'll engage it's own logic

    prec = {"/" : 3,
            "*" : 3,
            "+" : 2,
            "-" : 2,
            "(" : 1,
            ")" : None
            }

    # Let's define a stack that we can put operands into
    op_stack = Stack()
    
    # We'll also need a finally list to join together after all of this
    postfix_list = []

    # Let's take the string and split it, note we are using split because we don't want to capture spaces
    token_list = infix_expr.split()

    # now we'll go through each token in the list
    for token in token_list:
        # if the token is an operand, append it the postfix list
        if not token in prec.keys():
            postfix_list.append(token)
        elif token == "(" :
            op_stack.push(token)
        elif token == ")" :
            # Need to keep popping until you popped the "(" i.e. you've gotten out all the , make sure you append operands
            top_token = op_stack.pop()
            while top_token != "(":
                postfix_list.append(top_token)
                top_token = op_stack.pop()
        else:
            # pop out all operands, will need to peek at it's precedence level BUt what if it's there's nothing in the stack
            # i.e. this is the first time you're calling it ... is_empty.. so if it's not empty you can keep popping
            while (not op_stack.is_empty()) and (prec[op_stack.peek()] >= prec[token]):
                postfix_list.append(op_stack.pop())
            # after clearing all the lower precedence operands, add it the stack.
            op_stack.push(token)
    
    # Now dump the rest of the stack
    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())
    
    # Finally let's join the sting
    return " ".join(postfix_list)

print(infix_to_postfix("A * B + C * D"))
print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))
