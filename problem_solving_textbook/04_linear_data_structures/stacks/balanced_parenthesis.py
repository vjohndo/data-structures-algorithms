"""
Try to implement the same this by now for a gener case that in cludes different symbols

"""

from pythonds3.basic import Stack

# Let's create a matches function
# We can use index and strings to make this easy
def matches(open_symbol, close_symbol):
    open_symbols = "([{"
    close_symbols = ")]}"

    return open_symbols.index(open_symbol) == close_symbols.index(close_symbol)

def balance_checker(symbol_string):

    s = Stack()

    for symbol in symbol_string:
        # If the symbol is an opening bracket
        if symbol in "[{(":
            s.push(symbol)
        else:
            if s.is_empty():
                return False
            else:
                # At this point we should probably create a helper function
                # We want to use pop as we MUST have the last open bracket match the close bracket, no point in meeking
                # Notice how we have defined the order of the parameters
                if not matches(s.pop(),symbol):
                    return False
    
    return s.is_empty()

print(balance_checker('{({([][])}())}'))
print(balance_checker('[{()]'))
