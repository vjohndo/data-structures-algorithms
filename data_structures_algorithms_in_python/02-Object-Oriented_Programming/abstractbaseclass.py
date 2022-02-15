from abc import ABCMeta, abstractmethod

class Sequence(metaclass=ABCMeta):
    """Our own version of collections.Sequence abstract base class"""

    @abstractmethod # decorator declares the method to be abstract
    def __len__(self):
        """Return the length of the sequence."""

    @abstractmethod
    def __getitem__(self, j):
        """Rturn the element at index j of the sequence"""

    def __contains__(self, val):
        """Return True if val found in the sequence; False otherwise"""
        for j in range(len(self)):
            if self[j] == val:
                return True
        return False

    def index(self, val):
        """Return leftmost index at which val is found (or raise ValueError)"""
        for j in range(len(self)):
            if self[j] == val:                  # left most match
                return j
        raise ValueError('value not in sequence') # never found a match

    def count(self, val):
        """Return the number of elements equal to given value."""
        k = 0
        for j in range(len(self)):
            if self[j] == val:
                k += 1
        return k