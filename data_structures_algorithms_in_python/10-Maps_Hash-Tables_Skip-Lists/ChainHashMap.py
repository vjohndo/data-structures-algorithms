from HashMapBase import HashMapBase
from UnsortedTableMap import UnsortedTableMap

class ChainHashMap(HashMapBase):
    """Hash map implemented with separate chaining for collision resolution."""

    def _bucket_getitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(k))
        return bucket[k]

    def _bucket_setitem(self, j, k, v):
        if self._table[j] is None:
            self._table[j] = UnsortedTableMap() # Effectively an array

        # Keep track of the existing container at jth index of the table
        oldsize = len(self._table[j])

        # Update at the kth index of the container (which is at the jth index ofthe table)
        # Rememeber that _bucket_setitem is called by __setitem__ which applies the hash function + compression function to generate a key k which is an a index
        self._table[j][k] = v

        # Check if the len has increased, it means we've set a new index 
        if len(self._table[j]) > oldsize:
            self._n += 1

    def _bucket_delitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(k))
        del bucket[k] # uses __delitem__
        
    def __iter__(self):
        for bucket in self._table:
            if bucket is not None: # a nonempty slot 
                for key in bucket:
                    yield key