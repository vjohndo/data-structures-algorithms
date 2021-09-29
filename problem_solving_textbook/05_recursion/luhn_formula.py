"""
Write a program that can take a number and determine whether or not it is valid per the Luhn formula.
    1) Counting from rightmost digit (which is the check digit) and moving left, double the value of every second digit. 
    2) For any digits that thus become 10 or more, subtract 9 from the result.
    3) Add all these digits together.
    4) If the total ends in 0 it is a valid number
"""

def num_to_str(number):
    return str(number)

def luhn_recursion(digit_str,odd_step = True):
   
    # Base case if the string is length 1, return it
    if len(digit_str) <= 1:
        if odd_step:
            return digit_str
        else:
            # convert to int, double, take the last digit
            doubled_int = int(digit_str)*2
            if doubled_int >= 10:
                return str(doubled_int-9)
            else:
                return str(doubled_int)
    
    # Progress to base case by slicing string and alternating luhn
    else:
        if odd_step:
            return luhn_recursion(digit_str[:-1], not odd_step) + digit_str[-1]
        else:
            doubled_int = int(digit_str[-1])*2
            if doubled_int >= 10:
                return luhn_recursion(digit_str[:-1], not odd_step) + str(doubled_int-9)
            else:
                return luhn_recursion(digit_str[:-1], not odd_step) + str(doubled_int)

def string_sum(string):
    
    # Base case 
    if len(string) <= 1:
        return int(string)
    
    # Progress to base by slicing string
    else:
        return int(string[0]) + string_sum(string[1:])

def mod_10_check(sum):
    if sum % 10 == 0:
        return True
    else:
        return False

def luhn(num_input):
    num_str = num_to_str(num_input)
    converted_str = luhn_recursion(num_str)
    summed_nums = string_sum(converted_str)
    return mod_10_check(summed_nums)

print(luhn(3554)) # False
print(luhn(8763)) # True