import sys

# Initialise an empty array
data = []

# Go through 26 iterations of 
for k in range(27): # Put in a value of n that is fixed
    a = len(data) # Get the length of references in the referential list
    b = sys.getsizeof(data) # Get the size of the data
    print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a,b))
    data.append(None)