"""
Post fix operations...
    > operands go onto stack
    > Then once an operator comes along, perform the operation and put the rsult back into the stack
    > After everything, there should be only one operand on the stack and that is the result 
    > Becareful about the order of the operands for division
"""

from pythonds3.basic import Stack

def do_math(op,op1,op2):
    if op == "/":
        return op1 / op2
    elif op == "*":
        return op1 * op2
    elif op == "-":
        return op1 - op2
    elif op == "+":
        return op1 + op2

def postfix_eval(postfix_expr):
    operand_stack = Stack()
    token_list = postfix_expr.split()

    for token in token_list:
        # if the token is an operand, push into the stack
        if not token in "+-*/":
            operand_stack.push(float(token))
        else:
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            result = do_math(token,operand1,operand2)
            operand_stack.push(result)
    
    return operand_stack.pop()

print(postfix_eval("7 8 + 3 2 + /"))
