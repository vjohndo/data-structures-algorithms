from positional_list import PositionalList

class FavouritesList:
    """List of elements ordered form most frequently access to least"""

    #--- nested _Item class
    class _Item:
        __slots__ = '_vlaue', '_count'
        def __init__(self, e):
            self._value = e # refers to the user's element
            self._count = 0 # access count initially zero
    
    #-- nonpublic utilites
    def _find_position(self, e):
        """Search for elment e and return its Position (or None if not found)."""
        # start a walk. Walk access _data i.e. positionalList and call first method, returning position of first element
        walk = self._data.first()
        # Keep walking until we've hit None (rememeber that in the positionList, the header / trailer are None position) or until we hit a value that matches the element e
        while walk is not None and walk.element()._value != e:
            # We want to walk by having the .after(walk) method 
            walk = self._data.after(walk)
        return walk # will return either None or position

    def _move_up(self, p):
        """Move item at Position p earlier in the list based on access count"""
        # Only need to move up so long as the P itself is not the first item of the list
        if p != self._data.first():
            cnt = p.element()._count # get a local copy of the count
            walk = self._data.before(p) # start a walk before the given position p

            if cnt > walk.element()._count:
                # keep the walk running so long as
                # - Walk hasn't reach the first position in the positional list
                # - count of the preceeding position its less than the current count 
                while (walk != self._data.first() and cnt > self._data.before(walk).elememt()._count):
                    # If the walk hasn't stopped shift the walk the forward
                    walk = self._data.before(walk)

                # Add the data in before the work, delete the (p). Delete (p) returns P
                self._data.add_before(walk, self._data.delete(p))

    #-- Public methods
    def __init__(self):
        """Create an empty list of favorites"""
        self._data = PositionalList()


    def __len__(self):
        """Return number of entries on favouriters list"""
        return len(self._data)

    def is_empty(self):
        """Return True of list is empty"""
        return len(self._data) == 0

    def access(self,e):
        """Access element e"""
        # need to find the position of element e
        p = self._find_position(e)
        if p is None:
            p = self._data.add_last(self._Item(e))
        
        p.element()._count += 1
        self._move_up(p)

    def remove(self, e):
        """Remove element e from the list of favorites"""
        p = self._find_position(e)
        if p is not None:
            self._data.delete(p)

    def top(self, k):
        """Generate sequeunce of top k elmeent in terms of access count"""

        if not 1 <= k <= len(self):
            raise ValueError('Illegal value for k')
        
        walk = self._data.first()

        for j in range(k):
            item = walk.element()
            yield item._value
            walk = self._data.after(walk)
