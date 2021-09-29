"""
Trying to convert an integer say 10 to "10" in decimal or "1010" in binary
    > We've looked at this problem iteratively before but recursion is much more elegant
"""

def to_str(n, base):
    # Convert string is used with base case
    convert_string = "0123456789ABCDEF"

    # Should we get down to a single digit number we can easily escape conversion by converting single digit to corresponding string
    # Note single digit could mean "ABCDEF" in hex.
    if n < base:
        return convert_string[n]
    
    # We want to divide the string by the base
    # We know that as you're constructing a number in base from STACKS you're effective inserting like this.. stack_item3 + stack_item2 + stack_item1
    else:
        # I.e. give me back (WHAT EVER THE TO_STR(quotient1  is) + Remainder_1
                                # (WHAT EVER THE TO_STR(quotient2 is) + Remainder_2 + Remainder_1
                                    # (WHAT EVER THE TO_STR(quotient3 is) + Remainder_3 + Remainder_2 + Remainder_1
        return to_str(n // base, base) + convert_string[n % base]