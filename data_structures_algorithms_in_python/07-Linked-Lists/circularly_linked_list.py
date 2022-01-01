#--- Empty error class
class Empty:
    pass

class CircularQueue:
    """Queue implementation using circularly linked list for storage"""

    class _Node:
        """Create an empty queue"""
        __slots__ = '_element', '_next'
        
        def __init__(self, element, next):
            self._element = element
            self._next = next


    def __init__(self):
        """Create an empty queue"""
        self._tail = None
        self._size = 0

    def __len__(self):
        """Return the number of elements in the queue"""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty"""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue 
        
        Raise Empty exception if the queue is empty
        """

        if self.is_empty():
            raise Empty('Queue is empty')
        
        # Note that as this is a circularly linked list we can always get back to the head via the tail
        head = self._tail._next
        return head._element

    def dequeue(self):
        """Remove and return the frist element of the queue
        
        Raise Empty exception if the queue is empty
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        
        # need to grab a local copy of the old head as we will be erasing the reference to it from the tail
        oldhead = self._tail._next
        
        if self._size == 1:
            # account for the case with 1 
            # tail will be none
            self._tail = None
        else:
            # Otherwise bypass the old head 
            self._tail._next = oldhead._next
        
        self._size -= 1

        return oldhead._element

    
    def enqueue(self, e):
        """Add an element to the back of the queue"""
        newest = self._Node(e, None)

        if self.is_empty():
            # point the next reference back to itself
            newest._next = newest
        
        else:
            # point the next reference for the newest
            newest._next = self._tail._next
            # point the next reference for the tail
            self._tail._next = newest

        # New node becomes the tail
        self._tail = newest
        
        self._size -= 1

    def rotate(self):
        if self._size > 0:
            self._tail = self._tail._next
