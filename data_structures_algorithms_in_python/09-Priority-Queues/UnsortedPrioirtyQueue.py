from PriorityQueueBase import PrioirtyQueueBase
from PositionalList import PositionalList

class Empty:
    pass

class UnsortedPrioirtyQueue(PrioirtyQueueBase):
    """A min-oriented prioirty queue implemented with an unsorted list"""

    # --- Non Public Utility
    def _find_min(self):
        """Return Position of item with minimum key."""
        if self.is_empty():
            raise Empty('Prioirty queue is empty')

        small = self._data.first() # stores the position of the smallest seen so far
        walk = self._data.after(small)

        while walk is not None:
            if walk.element() < small.element(): # We've defined the item such that < compares the keys
                small = walk
            
            walk = self._data.after(walk)

        return small



    def __init__(self):
        """Create a new empty Prioirty Queue"""
        self._data = PositionalList()

    def __len__(self):
        """Return the number of items in the priorty queue"""
        return len(self._data)

    def add(self, key, value):
        """Add a key-value pair."""
        self._data.add_last(self._Item(key, value))

    def min(self):
        """Return but do not remove (k,v) tuple with minimum key"""
        p = self._find_min() # Returns the position of 
        item = p.element() # grab the item out, being stored as the element
        return (item._key, item._value)

    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key"""
        p = self._find_min()
        item = self._data.delete(p)
        return (item._key, item._value)
    
