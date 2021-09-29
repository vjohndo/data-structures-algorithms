"""
Decimal to binary converter:
    > Keep dividing by two
    > Track the remainders
    > Pop them than and reverse the order i.e. first remainder will be the rightmost binary number
    > % modulo keeps track of the remainder
    > // dives to the whole number
    > Using modulo and // means you can take the decimal number down to zero
"""

from pythonds3.basic import Stack

def divide_by_2(decimal_num):
    rem_stack = Stack()

    # While decimal number is greater than 0
    while decimal_num > 0:
        rem = decimal_num%2
        rem_stack.push(rem)
        decimal_num = decimal_num // 2

    # Now we need to pop all the numbers in the stack to the string
    bin_string = ""
    while not rem_stack.is_empty():
        bin_string = bin_string + str(rem_stack.pop())

    return bin_string

print(divide_by_2(17))
# print(divide_by_2(31))

"""
base converter, instead of divide by two, can we divide a base number passed in as an argument?

e.g. 233 in base 8 is 3*8**2 + 5*8**1 + 5*8**0

"""

def base_converter(decimal_num,base):
    # We need characters to represent up to base 16, but say if we want to go to higher base, would need more "digits"
    # Hex abd base eight are calculated from left to right
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    rem_stack = Stack()

    while decimal_num > 0:
        rem = decimal_num%base
        rem_stack.push(rem)
        decimal_num = decimal_num // base

    base_string = ""
    while not rem_stack.is_empty():
        base_string = base_string + digits[rem_stack.pop()]

    return base_string
        
# print(base_converter(256, 16))
