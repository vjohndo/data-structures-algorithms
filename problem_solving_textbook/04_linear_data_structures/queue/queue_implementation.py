"""
Queue implementation:
    > We can use lists to build a queue ADT
"""

class Queue:

    def __init__(self):
        """ Create a new queue """
        self._items = []

    def is_empty(self):
        """ Checks if the queue is empty, remember that an empty list is falsey """
        return not bool(self._items)

    def enqueue(self,item):
        """ We will add items to the start of the queue """
        self._items.insert(0, item)

    def dequeue(self):
        """ Removes the item at the front of the queue """
        return self._items.pop()
    
    def size(self):
        """ Gets the nuber of items in the queue """
        return len(self._items)