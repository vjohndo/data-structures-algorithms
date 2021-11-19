import os

def disk_usage(path):
    """Return the number of bytes used by a file/folder and any descendents."""
    # Get the direct usage of the input path to start, this includes if it is not a directory.
    total = os.path.getsize(path)

    # If this is a directory i.e. a folder
    if os.path.isdir(path):

        # Go through each child
        for filename in os.listdir(path):

            # Get the path the child
            childpath = os.path.join(path, filename)
            
            # recur on the child i.e. add its disk usage
                # I.e. get the directory total for the child
            total += disk_usage(childpath)

    # Because we are printing before return from recursive call,
    # A recursion trace would be in the order of the nodes visited
    print('{0:<7}'.format(total), path)
    return total