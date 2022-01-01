#--- Empty error class
class Empty:
    pass


class LinkedStack:
    """LIFO Stack implemetnation using a singly linked list for storage"""

    #--- nested _Node class
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node"""
        __slots__ = '_element', '_next'

        # Node takes in the element and next reference
        def __init__(self, element, next):
            self._element = element
            self._next = next

    #--- stack methods
    def __init__(self):
        """Create an empty stack"""
        self._head = None
        self._size = 0

    def __len__(self):
        """Retusn the number of elements in the stack"""
        return self._size

    def is_empty(self):
        """Return True if the stack is empty"""
        return self._size == 0

    def push(self, e):
        """Add an element to the top of the stack"""
        # Create a new node that element "e" and pointer to the next element 
        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):
        """Return but do not remove element at the top of the stack 
        
        Raise an error if the stack is empty
        """
        if self.is_empty():
            raise Empty('Stack is empty')

        # Note that you actually need to return the element, otherwise you are returning the node
        return self._head._element

    def pop(self):
        """Remove and returm the element from the top of the stack (i.e., LIFO).
        
        Raise empty exception if the stack is empty
        """

        if self.is_empty():
            raise Empty('Stack is empty')

        answer = self._head._element
        self._head = self._head._next
        self._size -= 1

        return answer

    