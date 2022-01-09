from HashMapBase import HashMapBase

class ProbeHashMap(HashMapBase):
    
    # We declare a class-level attribute as a sentinal
    # We use a build in object class, just need to differentiate from other objects
    _AVAIL = object()

    def _is_available(self, j):
        """Return True if index j is available in the table"""
        # I.e. check if the table is none or slot is available
        return self._table[j] is None or self._table[j] is ProbeHashMap._AVAIL

    def _find_slot(self, j, k):
        """Seach for key k in bucket at index j. 
        
        Return (success, index) tuble described as follows:
        If match was found, success if True and index denotes its location 
        """
        firstAvail = None # Init firstAvail as None
        while True: # Keep looping
            if self._is_available(j): # If the space is empty / available:
                if firstAvail is None: 
                    firstAvail = j # Set firstAvail as jth index
                if self._table[j] is None: # Notice how we are only stopping the search on is None
                    return (False, firstAvail)
            elif k == self._table[j]._key: # If the bucket is an object
                return(True, j)
            j = (j + 1) % len(self._table) # Keep looking cyclically

    def _bucket_getitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('Key Error: ' + repr(k))
        return self._table[s]._value

    def _bucket_setitem(self, j, k, v):
        found, s = self._find_slot(j, k)
        if not found: # No item exists in the map, time to inser a new item.
            self._table[s] = self._Item(k,v)
            self._n += 1
        else: # Item has been found and we need to update the avalue 
            self._table[s]._value = v

    def _bucket_delitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found: 
            raise KeyError('Key Error: ' + repr(k))
        self._table[s] = ProbeHashMap._AVAIL # Mark as vacated using the class-level attribute

    def __iter__(self):
        for j in range(len(self._table)):
            # Check if the index is available i.e. None or _AVAIL
            if not self._is_available(j):
                yield self._table[j]._key
 