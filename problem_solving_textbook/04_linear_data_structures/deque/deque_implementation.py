class Deque:
    """
    We can implement a deque in python using lists
    """

    def __init__(self):
        """ Creates a new deque """
        self._items = []

    def is_empty(self):
        """ Checks if the queue is empty """
        return not bool(len(self._items))
    
    def add_front(self,item):
        self._items.append(item)
    
    def add_rear(self,item):
        self._items.insert(0, item)
    
    def remove_front(self):
        self._items.pop()
    
    def remove_rear(self):
        self._items.pop(0)
    
    def size(self):
        return len(self._items)

    