"""
infix-to-postfix and postfix evaluation
"""

from pythonds3.basic import Stack

def infix_to_postfix_evaluate(infix_expression):
    # purifier
    try:
        parse_stack = Stack()
        for char in infix_expression:
            if char not in '1234567890+-()*/ ':
                raise TypeError('Expect computable chars but got {}'.format(char))
            elif char in '1234567890+-()*/':
                parse_stack.push(char)

        # start with a space as we'll pop that any way
        token_list = " "

        while not parse_stack.is_empty():

            popped_char = parse_stack.pop()

            if popped_char == "*" and token_list[0] == "*":
                token_list = popped_char + token_list
            elif popped_char not in '1234567890':
                token_list = f" {popped_char} " + token_list
            else:
                token_list = popped_char + token_list
                    
        operands = list('+-*/()')
        operands.append('**')
        token_list = token_list.split()
        print('tken_list',token_list)

        # precedence table 
        precedence = {
            "(": 1,
            "**": 4,
            "*": 3,
            "/": 3,
            "+": 2,
            "-": 2
        }
        operator_stack = Stack()
        postfix_list = []

        for char in token_list:
            if char not in operands:
                postfix_list.append(char)
            
            # must have the 
            elif char == "(":
                operator_stack.push(char)

            elif char == ")":
                # Unload all operands if "("
                popped_char = operator_stack.pop()
                    
                while popped_char != "(":
                    postfix_list.append(popped_char)
                    popped_char = operator_stack.pop()
                    
            # Otherwise unload all operands of higher or equal precedence
            else:
                while not operator_stack.is_empty() and precedence[operator_stack.peek()] >= precedence[char]:
                    popped_char = operator_stack.pop()
                    postfix_list.append(popped_char) 
                operator_stack.push(char)

        while not operator_stack.is_empty():
            postfix_list.append(operator_stack.pop())

        # At this point the post fix list is all good to go. 
        # Will reuse that above stack
        operand_stack = operator_stack
        for token in postfix_list:
            if token in operands:
                operator_2 = float(operand_stack.pop())
                operator_1 = float(operand_stack.pop())
                if token == "+":
                    result = operator_1 + operator_2
                elif token == "-":
                    result = operator_1 - operator_2
                elif token == "/":
                    result = operator_1 / operator_2
                elif token == "*":
                    result = operator_1 * operator_2
                elif token == "**":
                    result = operator_1 ** operator_2
                operand_stack.push(result)
            else:
                operand_stack.push(token)

        return operand_stack.pop()
    except:
        raise RuntimeError('CHECK YOUR INPUT')


print(infix_to_postfix_evaluate("( 7 + 8 ) / ( 3 + *** 2 )"))