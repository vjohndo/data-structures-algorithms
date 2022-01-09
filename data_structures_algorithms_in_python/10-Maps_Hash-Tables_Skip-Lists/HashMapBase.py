from MapBase import MapBase
from random import randrange

class HashMapBase(MapBase):
    """Abstract base class for map using hash-table with MAD compression"""

    def __init__(self, cap=11, p =109345121):
        """Create an empty hash-table map."""
        self._table = cap * [None] # Cap is N i.e. the size of the array bucket
        self._n = 0 # Number of entries in the map
        
        # MAD compression is [(ai + b) % p] % N
        # where 'i' is the hash code 
        self._prime = p # Prime number larger than N
        self._scale = 1 + randrange(p-1) # scaling of the hash code 
        self._shift = randrange(p) # shifting of hash code 

    def _hash_function(self, k):
        # Uses the inbuild python hash function 
        # Then applies the MAD compression function to map it the range [0, N-1]
        return (hash(k)*self._scale + self._shift) % self._prime % len(self._table)


    # --- Abstract bucket 
    def _bucket_getitem(self, j, k):
        """Methd searchs bucket j for an item with key k. Returns the value if found or raises a key error"""
        raise NotImplementedError('Needs to be implemented as part of a base class')

    def _bucket_setitem(self, j, k, v):
        """Modify's bucket j so that k becomes associated with value v.
        If the key already exists, new value overwrites the existing value
        Otherwise, a new item is inserted and this method is responsible for incrementing self._n
        """
        raise NotImplementedError('Needs to be implemented as part of a base class')

    def _bucket_delitem(self, j, k):
        """Remove the item from bucket j having key k. Raise a KeyError if no such item exists"""
        raise NotImplementedError('Needs to be implemented as part of a base class')

    def __len__(self):
        return self._n

    def __get__(self, k):
        j = self._hash_function(k)
        return self._bucket_getitem(j, k) # may raise KeyError

    def __setitem__(self, k, v):
        j = self._hash_function(k)
        self._bucket_setitem(j, k, v)
        if self._n > len(self._table) // 2: # Check the load factor <= 0.5
            self._resize(2 * len(self._table) - 1) # Otherwise then need to resize

    def __delitem__(self, k):
        j = self._hash_function(k)
        self._bucket_delitem(j, k)
        self._n -= 1

    def _resize(self, c):
        old = list(self.items())
        self._table = c * [None]
        self._n = 0 
        for (k,v) in old:
            self[k] = v # This uses __setitem__ which will rehash the keys
    
    