from collections import MutableMapping

class MapBase(MutableMapping):
    """Abstract base class that includes nonpublic _Item class
    
    Extends the mutablemapping class which we just need to redfine the 5 core implementation
    """

    # --- nested _Item class
    class _Item:
        """Lightweight composite to store key-value paris as map items."""
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __eq__(self, other):
            return self._key == other._key # compares items based on their keys

        def __ne__(self, other):
            return not (self == other)

        def __lt__(self, other):
            return self._key < other._key # compare items based on their keys

    
