from MapBase import MapBase

class SortedTableMap(MapBase):
    """Map implementation using a sorted table"""

    # --- non public behaviors 
    def _find_index(self, k, low, high):
        """Return index of the left most item with key greater than or equal to k. 
        
        Return high + 1 if no such item qualifies.

        That is, j will be returned such that:
            all items of slice table[low:j] have key < k
            all items of slice table[j:high + 1] have key >= k
        """
        
        if high < low:
            return high + 1 # if no element qualifies, return the leemnt just beyond where that missing element would be
        else:
            mid = (low + high) // 2
            if k == self._table[mid]._key: # trying to use find on an empty array would result in indexerror
                return mid
            elif k < self._table[mid]:
                return self._find_index(k, low, mid-1) # Note: may return mid (i.e. it will be passed in to next frame as high, then returned high + 1)
            else:
                return self._find_index(k, mid+1, high) # answer is right of mid 

    # --- public behaviours
    def __init__(self):
        """Create an empty map."""
        self._table = []

    def __len__(self):
        """Return number of items in the map."""
        return len(self._table)

    def __getitem__(self, k):
        """Return value associated with key k (raise KeyError if not found)."""
        j = self._find_index(k, 0, len(self._table) - 1)

        # Rememeber that find index will return the index just beyond the missing target
        # if jth index is not an index in the range of table or if the returned index in the table is not k
        # raise a value error (note that we have the first condition j == len(self._table as we want to raise our own KeyError, not python's one for list))
        if j == len(self._table) or self._table[j]._key != k:
            raise KeyError('Key Error: ' + repr(k))

        return self._table[j]._value # We store at the index of the table items which contain key, value pairs

    def __setitem__(self, k, v):
        """Assign value v to key k, overwriting existing value if present"""
        j = self._find_index(k, 0, len(self._table) - 1)
        if j < len(self._table) or self._table[j]._key ==k: # I f the index is within valid range or key is equal to k
            self._table[j]._value = v # reassign the value
        else:
            # need to make a new key
            self._table.insert(k, self._Item(k,v))

    def __delitem__(self, k):
        """Remove item associated with key k (raise KeyError if not found)."""
        j = self._find_index(k, 0, len(self._table) - 1)
        if j == len(self._table) or self._table[j]._key != k:
            raise KeyError('Key Error: ' + repr(k))
        
        self._table.pop(j)

    def __iter__(self):
        """Generate keys of map ordered from maximum to minimum"""
        for item in reversed(self._table):
            yield item._key

    def find_min(self):
        """Return (key,value) pair with minimum key (or None if empty)."""
        if len(self._table) > 0:
            return (self._table[-1]._key, self._table[-1]._value)
        else: 
            return None
    
    def find_ge(self, k):
        """Return (key, value) paair with least key greater than or equal to k."""
        j = self._find_index(k , 0, len(self._table) - 1)
        if j < len(self._table):
            # only if there is still at least one element beyond is there a greater than or equal to item
            return (self._table[j]._key, self._table[j]._value)
        else:
            return None

    def find_le(self, k):
        """Return (key, value) pair with the greatest key less than or equal to k"""
        """This is a selfmade version, should check"""
        # find the jth index of k
        j = self._find_index(k, 0, len(self._table)-1)

        if j > 0 and self._table[j]._key != k: # Check that we have a don't matching key but still return positive j
            # Then we want to return the value below with decremented index
            return (self._table[j-1]._key, self._table[j-1]._value)
        elif self._table[j]._key == k: 
            return (self._table[j]._key, self._table[j]._value)
        else:
            return None

    def find_le2(self, k):
        """Return (key, value) pair with the greatest key less than or equal to k"""
        """This is a selfmade version, should check"""
        # find the jth index of k
        j = self._find_index(k, 0, len(self._table)-1)

        if self._table[j]._key != k: # Check that we have a don't matching key
            j -= 1 # Then decrement j
        if j >= 0: # Now J will either be at the less than value or the is the equal value, but chance that j is -1
            return (self._table[j]._key, self._table[j]._value)
        else: # J must have been -1 i.e. no key less than or equal to k
            return None

    def find_le3(self, k):
        """Return (key, value) pair with the greatest key less than or equal to k"""
        """This is a selfmade version, should check"""
        # find the jth index of k
        j = self._find_index(k, 0, len(self._table)-1)

        if self._table[j]._key == k: # Check that it's a match. 
            j += 1 # Then we'll increase it by 1 as we'll be decrasing it by one in the next stal
        if j > 0: # Now J will either be at the less than value or the is the equal value, but chance that j is -1
            return (self._table[j-1]._key, self._table[j-1]._value)
        else: # J must have been -1 i.e. no key less than or equal to k
            return None

    def find_lt(self, k):
        """Return (key, value) pair with greatest key strictly less than k."""
        j = self._find_index(k, 0, len(self._table)-1)
        if j > 0: # so long as there is still at least one item for which we are greater
            return (self._table[j-1]._key, self._table[j-1]._value)
        else:
            return None
    
    def find_gt(self, k):
        """Return (key, value) pair with least key strictly greater than k."""
        j = self._find_index(k, 0, len(self._table) - 1)
        
        if j < len(self._table) and self._table[j]._key == k: # Check that there is a match.
            j += 1 # If it is a match we want to return j += 1

        # If there isn't a match it will return an index beyond which _find_index would have already returned
        # Now we need to check that we are not returning something outside the range of the array
        if j < len(self.table): 
            return (self._table[j]._key, self._table[j]._value)
        
        # Otherwise there is nothing in the list that matches the criteria
        else:
            return None

    def find_range(self, start, stop):
        """Iterate all (key, value) pairs such that start <= key < stop
        
        If start is None, iteration begins with minimum key of map.
        If stop is None, iteration contiues through the maximum key of map.
        """
        # First find start
        if start is None:
            j = 0
        else:
            j = self._find_index(start, 0, len(self._table) -1)

        # Then iterate through until we've found stop.
        # I.e. until the we've hit the end or we've found a key greater than the stop
        while j < len(self._table) and (stop is None or self._table[j]._key < stop):
            yield (self._table[j]._key, self._table[j]._value)
            j += 1
        
