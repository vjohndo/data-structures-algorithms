class Empty(Exception):
    pass

class ArrayStack:
    """LIFO Stack implementation using the Python List as underlying storage"""

    def __init__(self):
        """create an empty stack"""
        self._data = [] # nonplublic list instance

    def __len__(self):
        """Return the number of elements in the stack"""
        return len(self._data)

    def is_empty(self):
        """Return True if the stack is empty"""
        return len(self._data) == 0

    def push(self, e):
        """Add element to the top of the stack"""
        self._data.append(e)

    def top(self):
        """Return (but do not remove) the leemnt at the top of the stack"""

        if self.is_empty(): 
            raise Empty('Stack is empty')

        return self._data

    def pop(self):
        if self.is_empty():
            raise Empty('stack is empty')

        return self._data.pop()
