import sys
data = []
for k in range(n): # Put in a value of n that is fixed
    a = len(data)
    b = sys.getsizeof(data)
    print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a,b))
    data.append(None)