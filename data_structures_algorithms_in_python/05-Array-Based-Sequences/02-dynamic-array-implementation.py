import ctypes

# Everytime an item is appended at full capacity
# New array B, reassign indexes, set A = B
# Insert new element in the array

class DynamicArray:
    """A dynamic array cllass akin to a simplified Python list."""

    def __init__(self):
        """Create an empty"""
        self._n = 0 # Count of actual elements
        self._capacity = 1 # Track of the current capacity of the array
        self._A = self._make_array(self._capacity) # Makes a low-level array

    def __len__(self):
        """Return number of elements stored in the array."""
        return self._n 

    def __getitem__(self, k):
        """Return element at index k."""
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k] # retrieve from an array

    def append(self, obj):
        """Add object to end of the array"""
        if self._n == self._capacity: # If the capacity has been reached
            self._resize(2*self._capacity) # make an array
        self._A[self._n] = obj # assign the the object to append to the newest index (count will be +1 of index)
        self._n += 1 # increase the actual number of items in array by 1

    def _resize(self, c):
        """Resize internal array to capacity c."""
        B = self._make_array(c) # make a new low level array, to size c (c will have been 2 * existing capcity)
        for k in range(self._n): # Go through each element in the array
            B[k] = self._A[k] # and reassign all the indexes
        self._A = B # set the existing reference to B
        self._capacity = c # set the capacity to the new value given

    def _make_array(self, c):
        """Return new array with capacity c."""
        return (c * ctypes.py_object)() # makes a low level array

    def insert(self, k, value):
        """Insert value at index k, shifting subsequent values rightward"""

        if self._n == self._capacity: # If we've reached the limit
            self._resize(2 * self._capacity) # Resize the list
        
        # Go through the list list and append
        for j in range(self._n, k, -1):
            self._A[j] = self._A[j-1] # shift the right most cells right
        self._A[k] = value # insert the new cell
        self._n += 1 # increase the capacity count by 1
        
    def remove(self, value):
        """Remove first occurence of value (or raise ValueError)"""

        for k in range(self._n):
            if self._A[k] == value:
                for j in range(k, self._n - 1):
                    self._A[j] = self._A[j+1]
                self._A[self._n - 1] = None
                self._n -= 1
                return 
        raise ValueError('value not found')
