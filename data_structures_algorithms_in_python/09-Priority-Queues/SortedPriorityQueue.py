from PriorityQueueBase import PrioirtyQueueBase
from PositionalList import PositionalList

class Empty:
    pass

class SortedPrioirtyQueue(PrioirtyQueueBase):
    """ A min-oriented prioirty queue implemented with a sorted list."""

    def __init__(self):
        """Create a new empty Prioirty Queue."""
        self._data = PositionalList()

    def __len__(self):
        """Return the number ofitems in the priority queue."""
        return len(self._data)

    def add(self, key, value):
        """Add a key-value pair"""
        newest = self._Item(key, value)
        walk = self._data.last() # walk backward in the queue looking for a smaller key

        while walk is not None and newest < walk.element():
            walk = self._data.before(walk) # keep progressing the walk from the back towards the front of the queue 
            # this will stop the walk at hitting the front of the queue / when we've found the first instance of a smaller item

        if walk is None:
            self._data.add_first(newest)

        else: # The case where we've found the first instance of a smaller item in the queue
            self._data.add_after(walk, newest)

    def min(self):
        """Return but do not remove (l,v) tupe with minimum key"""
        if self.is_empty():
            raise Empty('Prioirty queue is empty.')
        
        p = self._data.first() # returns the position of the positional list
        item = p.element # returns the item stored as the element in the position

        return (item._key, item._value)

    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key."""
        if self.is_empty():
            raise Empty('Prioirty queue is empty.')
        
        item = self._data.delete(self._data.first())
        return (item._key, item._value)
    
