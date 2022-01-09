from sys import platform
from SortedTableMap import SortedTableMap

class CostPerforamnceDatabase:
    """Maintain a datase of maximal (cost, performance) pairs"""

    def __init__(self):
        """Create an empty database"""
        self._M = SortedTableMap()

    def best(self, c):
        """Return (cost, performance pair with the largest cost not exceeding c.
        
        Return None if there is no such pair
        """
        self._M.find_le(c)

    def add(self, c, p):
        """Add new entry with cost c and perforamnce p"""
        # Determine if (c,p) is dominated by an existing pair
        other = self._M.find_le(c)
        
        # If other is not none and the performance of the cheaper or equal priced item is better
        if other is not None and other[1] >= p:
            return # do nothing

        # Otherwise we'll add this to the database and remove any that are currently domindated by (c, p)
        self._M[c] = p
        other = self._M.find_gt(c)

        # Until we've hit the end other pairs within the cost range or we've found the next item that isn't dominated
        while other is not None and other[1] <= p:
            del self._M[other[0]] # delete other using the key returned
            other = self._M.find_gt


