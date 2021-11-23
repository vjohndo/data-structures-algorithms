from time import time
def compute_average(n):
    """Performs n appends to an empty list and return average time elapsed"""

    data = []
    start = time()
    for k in range(n):
        data.append(None)
    
    end = time()
    return (end - start) / n

print(compute_average(5000000))