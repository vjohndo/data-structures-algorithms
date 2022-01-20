from HeapPriorityQueue import HeapPriorityQueue

class AdaptableHeapPriorityQueue(HeapPriorityQueue):
    """ A location-based priority queue implemented with a binary heap """

    # --- nested Locator class
    class Locator(HeapPriorityQueue._Item):
        """Token for lacting an entry of the prioirty queue,"""
        __slots__ = '_index' # add index as an additional field

        def __inti__(self, k, v, j):
            super().__init__(k,v)
            self._index = j

    
    # --- nonpublic behaviors
    # overrise swap to record new indeces
    def _swap(self, i, j):
        super()._swap(i, j)
        self._data[i]._index = i # swap has been made. go into the heap at i and update the index for the Locator
        self._data[j]._index = j # swap has been made. go into the heap at j and update the index for the Locator

    def _bubble(self, j):
        if j > 0 and self._data[j] < self._data[self._parent(j)]:
            self._upheap(j) # uphea uses swap. swap has already been overwritten to update the index
        else:
            self._downheap(j)

    def add(self, key, value):
        """Add a key-value pair"""

        token = self.Locator(key, value, len(self._data)) # initalize the locator index at the end of the array
        self._data.append(token)
        self._upheap(len(self._data - 1)) # Now that we've added it in, upheap
        return token

    def update(self, loc, newkey, newval):
        """Update the key and value for the entry identified by Locator loc."""
        j = loc._index
        # Check if this loc is actually an index within the heap and if it's actually the correct reference in the heap
        if not( 0 <= j < len(self) and self._data[j] is loc):
            raise ValueError('Invalid Locator')

        loc._key = newkey
        loc._value = newval
        self._bubble(j) # remember that bubble checks the parent and bubbles up / down accordingly

    def remove(self, loc):
        """Remove and return the (k, v) pair identified by Locator loc."""
        j = loc._index
        if not ( 0 <= j < len(self) and self._data[j] is loc):
            raise ValueError('Invalid Locator')

        if j == len(self) - 1: # Item at last position is easy case
            self._data.pop()

        else:
            self._swap(j, len(self) - 1) # swap the last item here 
            self._data.pop() # pop off the target to be removed
            self._bubble(j) # bubble at the jth index

        return (loc._key, loc._value)