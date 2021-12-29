from array_stack import ArrayStack

def is_matched_html(raw):
    """Return True if all HTML tages are propertly matched; False otherwise"""

    # instantiate an array
    S = ArrayStack()
    
    # finds the first occurence of the specified value, -1 if otherwise 
    # the find method can be used to find second and third values by defning start values e.g. raw.find('<', j + 1), raw.find('<', j + 2)
    j = raw.find('<')

    # so long as we can keep finding an opening tag
    while j != -1:

        # find the closing tag, starting from the next index
        k = raw.find('>', j+1)

        # If we can't find the next tag, return false
        if k == -1: 
            return False

        # we have identified as the string slice between starting from j+1 up to but not including k, at k, the closing tag presides
        tag = raw[j+1:k]
        
        # check that this tag is not closing
        if not tag.startswith('/'):
            # if so you can push to the stack
            S.push(tag)

        # otherwise if it's closing tag i.e. tag = /sometag
        else: 
            # If there's nothing in the stack, return false. We haven't seen a corresponding opening tag yet
            if S.is_empty():
                return False

            # Otherwise let's check it against what's at the top of the stack
            # If the remaining section of the array is = to the pop return false
            if tag[1:] != S.pop():
                return False 

        # find the next opening tag
        j = raw.find('<', k+1)
    
    # if we've gone through the whole sequence and j is now returungin -1
    # return the boolean of whether the list is empty or not. 
    return S.is_empty()

        
