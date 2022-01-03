class Empty:
    pass

class _DoublyLinkedBase:
    """A base class providing a doubly linked list representation"""

    class _Node:
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        """Create an empty list"""
        
        # Create the header and trailer sentinels and point them to each other
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header

        self._size = 0

    def __len__(self):
        """Return the number of elements in the list"""
        return self._size

    def is_empty(self):
        """Return true if the list is empty"""
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """Add element e between two existing nodes and return a new node"""
        newewst = self._Node(e, predecessor, successor)
        predecessor._next = newewst
        successor._next = predecessor
        self._size += 1
        return newewst

    def _delete_node(self, node):
        """Delete nonsentinel node from the list and return its element"""
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1

        element = node._element
        # Need to deprecate the node i.e. help with garbage collection
        node._prev = node._next = node._element = None

        return element


class LinkedDeque(_DoublyLinkedBase): # Note the use of inheritance
    """Double-ended queue inmplementation based on a doubly linked list"""

    def first(self):
        """Return but do not remove the element at the front of the deque"""
        if self.is_empty():
            raise Empty('Deque is empty')

        return self._header._next._element # recall that the real item is just after the header
    
    def last(self):
        """Return (but do not remove) the element at the back of the deque"""
        if self.is_empty():
            raise Empty("Deque is empty")

        return self._trailer._prev._element

    def insert_first(self, e):
        """Add an element to the front of the deque"""
        self._insert_between(e, self._header, self._header._next)

    def insert_last(self, e):
        """Add an element to the back of the deque"""
        self._insert_between(e, self._trailer._prev, self._trailer)

    def delete_first(self):
        """Remove and return the element from the front of the deque
        
        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty("Deque is empty")

        return self._delete_node(self._header._next)

    def delete_last(self):
        """Remove and return the element from the back of the deque
        
        Raise Empty exception if the deque is empty
        """
        if self.is_empty():
            raise Empty("Deque is empty")

        return self._delete_node(self._trailer._prev)

