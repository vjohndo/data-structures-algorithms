class PrioirtyQueueBase:
    """Abstract base class for a prioirty queue"""

    class Empty:
        pass

    class _Item:
        """Lightweight composite to store priority queue items"""
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            """Lightweight composite to store priorty queus items """
            self._key = k
            self._value = v

        def __lt__(self, other):
            """Compares Items based on keys"""
            return self._key < other._key

    def is_empty(self):
        """Return True if the prioirty queue is empty"""
        # This is a concrete method assuming abstract len
        return len(self) == 0 
        