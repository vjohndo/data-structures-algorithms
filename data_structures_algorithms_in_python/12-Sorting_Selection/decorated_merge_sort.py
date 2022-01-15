class _Item:
    pass

def merge_sort():
    pass

def decorated_merge_sort(data, key = None):
    """Demonstration of the decorate-sort-undecorate pattern"""
    if key is not None:
        for j in range(len(data)):
            data[j] = _Item(key(data[j]), data[j]) # decorate each element to now have key + data
    
    merge_sort(data)

    if key is not None:
        for j in range(len(data)):
            data[j] = data[j]._value # undecorate each element