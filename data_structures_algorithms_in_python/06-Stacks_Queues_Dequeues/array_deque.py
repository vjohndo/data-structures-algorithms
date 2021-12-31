class Empty:
    """Error class upon empty"""
    pass

class ArrayDeque:
    """FIFO queue implementation using a Python list as underlying storage."""
    
    # Want to moderate the capacity for all new queues
    # We will create a "class data memeber"
    # This is shared among all instances of the class
    DEFAULT_CAPACITY = 10

    def __init__(self):
        """Create an empty queue"""

        # Create an empty queue, using the default capacity which is a class data member
        self._data = [None] * ArrayDeque.DEFAULT_CAPACITY
        self._size = 0 # size is 0 upon instantiation
        self._front = 0 # front of queue index is 0 upon instantiation

    def __len__(self):
        """Return the number of elements in the queue"""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty"""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element of the front of the queue
        
        Raise Empty exception if the queue is empty
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def last(self):
        """ Return (but do not remove) the last element of deque
        
        Raise Empty exeception if the deque is empty
        """
        if self.is_empty():
            raise Empty('Queue is empty')

        return self._data[(self._front + self._size - 1) % len(self._data)]


    def delete_first(self):
        """Remove and return the first element of the queue
        
        Reaise Empty exception if the queue is empty
        """

        if self.is_empty():
            raise Empty('Queue is empty')
        
        # We will need to reassign self._size and self._front
        # Since we will change front we need to grab the reference to the front of queue first
        answer = self._data[self._front]

        # We can now remove point the cell of the list to none
        # also helpful for garbage collection i.e. python maintains a count of references to an object.  Should references be 0, python can recalin that for memeory 
        self._data[self._front] = None

        # We can change the front index number by the size of the list
        self._front = (self.first + 1) % len(self._data)

        # We can now also reduce the size of the queue by 1
        self._size -= 1

        # future implementation should consider resizing the array 
        # optimal strategy is to hald the size of the array should the size of the queue hit 1/4 capacity
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data)//2)

        return answer

    def delete_last(self):
        """Remove and return the last element of the queue
        
        Reaise Empty exception if the queue is empty
        """

        if self.is_empty():
            raise Empty('Queue is empty')
        
        # We will need to reassign self._size and self._front
        # Since we will change front we need to grab the reference to the front of queue first
        answer = self._data[(self._front + self._size - 1) % len(self._data)]

        # We can now remove point the cell of the list to none
        # also helpful for garbage collection i.e. python maintains a count of references to an object.  Should references be 0, python can recalin that for memeory 
        self._data[(self._front + self._size - 1) % len(self._data)] = None

        # We can now also reduce the size of the queue by 1
        self._size -= 1

        # future implementation should consider resizing the array 
        # optimal strategy is to hald the size of the array should the size of the queue hit 1/4 capacity
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data)//2)

        return answer

    def add_last(self, e):
        """Add an element to the back of queue"""

        # Check if we are at the limit of the array
        if self._size == len(self._data):
            
            # We will need to resize... we'll define this later
            self._resize(2 * len(self._data))

        # Go to the next available index 
        avail = (self._front + self._size) % len(self._data)
        
        # Now you can define the next index
        self._data[avail] = e

        # Increase the size 
        self._size += 1
    
    def add_first(self, e):
        """Add an element to the front of queue"""

        # Check if we are at the limit of the array
        if self._size == len(self._data):
            
            # We will need to resize... we'll define this later
            self._resize(2 * len(self._data))

        # Go to the next available index at front 
        avail = (self._front - 1) % len(self._data)
        
        # Now you can define the next index
        self._data[avail] = e

        # Increase the size 
        self._size += 1

    def _resize(self, cap):
        """Resize to a new list of capacity >= len(self)."""
        
        # Keep track of the old data
        old = self._data
        
        # Redefine a new list with bigger capacity
        self._data = [None] * cap

        walk = self._front

        # we need to move the old entries into the new array and make sure the modular arithmatic (circular array logic) works
        # Let's iterate through the queue, however, only consider existing elements
        for k in range(self._size):

            # reassign kth index of _data (0, 1, 2, 3, ..) to old k of old (f, f+1, etc.)
            self._data[k] = old[walk]

            # Will need to redefine walk to become circular 
            walk = (walk + 1) % len(old)

        # front has been realigned
        self._front = 0