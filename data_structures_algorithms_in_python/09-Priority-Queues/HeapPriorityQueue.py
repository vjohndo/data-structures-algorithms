from PriorityQueueBase import PrioirtyQueueBase

class Empty:
    pass

class HeapPriorityQueue(PrioirtyQueueBase): # base class, defines _Item
    """A min-oriented prioirty queue implemented with a binary heap"""

    #--- nonpublic behiavours 
    def _parent(self, j):
        """Return the parent index"""
        return (j - 1) // 2

    def _left(self, j):
        """Returns the left child index"""
        return 2*j + 1

    def _right(self, j):
        """Returns the right child index"""
        return 2*j + 2

    def _has_left(self, j):
        """Checks if the left child index is within the existing array"""
        return self._left(j) < len(self.data) # Is the left index within the length of the list
    
    def _has_right(self, j):
        """Checks if the right child index is within the existing array"""
        return self._left(j) < len(self.data) # Is the right index within the length of the list 

    def _swap(self, i, j):
        """Swap the elements at indices i and j or array"""
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        """Upheap"""
        parent = self._parent(j) # Find the parent index
        if j > 0 and self._data[j] < self._data[parent]: # Check if that is within the limits of the array and if the parent is NOT less j._data
            self._swap(j, parent) # If so swap the elements
            self._upheap(parent) # Then recur at the position of the parent 

    def _downheap(self, j):
        """Downheap"""
        # Check if left and right exist and find the smallest child, can only downheap if j index has children
        if self._has_left(j):
            left = self._left(j)
            small_child = left # init the left as the small child, will want to check right as well
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right

            if self._data[small_child] < self._data[j]: # Now that we've identified the smallest child, check equality and swap
                self._swap(j, small_child)
                self._downheap(small_child) # Recur at the position of small child

    # --- public behaviours
    def __init__(self):
        """Create a new priority queue"""
        self._data = []

    def __len__(self):
        """Return the number of items in the priority queue"""
        return len(self._data)

    def add(self, key, value):
        """Add a key-value pair to the prioirty queue"""
        self._data.append(self._Item(key, value))
        self._upheap(len(self._data) - 1) # Upheap the newly added position. we know it will be n - 1

    def min(self):
        """Return but do not remove(k,v) tupe with minimum key.
        
        Raise Empty exception if empty
        """
        if self.is_empty():
            raise Empty('Priority queue is empty')
        
        item = self._data[0]
        return (item._key, item._value)

    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key.
        
        Raise Empty exception if empty.
        """
        if self.is_empty():
            raise Empty('Prioirty queue is empty')
        
        self._swap(0, len(self._data) - 1) # Swap the begining and end items.
        item = self._data.pop() # Remove the item from the list we are returning
        self._downheap(0) # Downheap the new root
        
        return (item._key, item._value)