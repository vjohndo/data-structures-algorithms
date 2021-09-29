"""
Takes a string as a parameter and returns True
"""

def is_palindrome(expression):
    ## Data validation helper ##
    # consider writing these as seperate helper functions.. this would not be a pure function.
    valid_chars = 'abcdefghijklmnopqrstuvwxyz'
    list_chars = [x.lower() for x in expression if x.lower() in valid_chars]

    # If it's even it or empty
    if len(list_chars) % 2 == 0 or len(list_chars) <= 0:
        return False


    ## RECURSION PART ##
    # BASE CASE -> we know this number is even
    if len(list_chars) == 1:
        return True
    
    # PROGRESS TO BASE CASE -> Pass in middle of the list and combine all trues/false from the stack frames
    else:
        front_back_same = list_chars[0] == list_chars[-1]
        if front_back_same:
            
            return front_back_same and is_palindrome(" ".join(list_chars[1:-1]))
        else:
            # Quick escape if false at any point
            return False
        
    
print(is_palindrome('Wassamassaw'))
print(is_palindrome('kayak'))
print(is_palindrome('aibohphobia'))
print(is_palindrome('iaubelifuhbalse'))
print(is_palindrome('Waafsefasefassamassaw'))
print(is_palindrome('Wassamfasefaseassaw'))
print(is_palindrome('Wassamasefaseassaw'))
print(is_palindrome('Wassamafasefaesssaw'))
