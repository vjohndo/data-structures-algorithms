def sumOfN(n):
    theSum = 0
    for i in range(1,n+1):
        theSum += i
    return theSum

print(sumOfN(10))

import time

def sumOfN2(n):
    start = time.time()

    theSum = 0
    for i in range(1,n+1):
        theSum = theSum + i
    
    end = time.time()

    return theSum,end-start

print('Algo1: For Loop')
for i in range(5):
    print("Sum is %d required %10.7f seconds"%sumOfN2(10000))


# Compare this to a closed equation:
def sumOfN3(n):
    start = time.time()

    theSum = n*(n+1)/2

    end = time.time()

    return theSum,end-start

print('Algo2: Sum of notation')
for i in range(5):
    print("Sum is %d required %10.7f seconds"%sumOfN3(10000))


# Also if we try different amounts for N, they still take very limited time.
print('Algo2: Sum of notation - linear properties')
for i in [1000,10000,1000000]:
    print("Sum is %d required %10.7f seconds"%sumOfN3(i))
