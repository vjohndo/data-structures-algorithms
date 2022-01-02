from doubly_linked_list import _DoublyLinkedBase

class PositionalList(_DoublyLinkedBase):
    """A sequential container of elements allowing positional access"""

    #--- nested Position class
    class Position:
        """An abstraction representing the location of a single element"""

        def __init__(self, container, node):
            """Constructor should not be invoked by a user"""
            self._container = container # References an actual container i.e. poisitional list instance
            self._node = node # References a node in the container

        def element(self):
            """Return the element stored at this Position"""
            return self._node._element

        def __eq__(self, other):
            """Return True if other is a Position representing the same location"""
            # Check that they are of the same type and that they are infact the same reference
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            """Return True if other does not present the same location"""
            # Note that because we have defined __eq__ above, we can use == operator 
            return not (self == other) 

    # --- Utility Method
    def _validate(self, p):
        """Return position's node, or raise appropriate error if invalid"""
        if not isinstance(p, self.Position): # check if the p is a valid position class
            raise TypeError('p must be a propert Position type')

        if p._container is not self: # check if the p exists within the same positional list
            raise ValueError('p does not belong to this container')

        if p._node._next is None: # check if the p next pointer references something, remember that delete node sets it to none so this helps us recognise deprecated nodes
            raise ValueError('p is no longer valid')

        return p._node

    def _make_position(self, node):
        """Return Position instance for given node (or None if sentinel)."""
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node) #self as in the instance of the positional list and the actual node reference

    
    # --- Accessors
    def first(self):
        """Return the first Position in the list (or None if the list if empty)"""
        return self._make_position(self._header._next)

    def last(self):
        """Return the last position in the list (or None if the list is empty)."""
        return self._make_position(self._trailer._prev)

    def before(self, p):
        """Return the Position just before Position p (or None if p is first)"""
        node = self._validate(p) # Check if p is a Position instance, from this instance of the Position List and is not deprecated
        return self._make_position(node._prev)

    def after(self, p):
        """Return the Position just after Position p"""
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        """Generate a forward iteration of the lements of the list"""
        cursor = self.first()
        while cursor is not None:
            yield cursor.element() # note that yield is like returns but returns a generator... create the iter
            cursor = self.after(cursor)

    # --- Mutators
    # Override inherited version to return Position rather than the Node
    def _insert_between(self, e, predecessor, successor):
        """Add element between existing nodes and return new Position"""
        # Access the super class method insert between
        node = super()._insert_between(e, predecessor, successor)
        # Except now return a position
        return self._make_position(node)

    def add_first(self, e):
        """Insert selement e at the front between the list and return new Position"""
        self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        """Insert element e into list before Position p and return new Position"""
        self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        """Insert element e into list before Position p and return new Position"""
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        """Insert element e into list after Position p and return Position"""
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):
        """Remove and return the element at position P"""
        original = self._validate(p)
        return self._delete_node(original) # use the inherited method

    def replace(self, p, e):
        """Replace the element at Position p with e.
        
        Return the element formerly at Position p
        """
        original = self._validate(p)
        old_value = original._element   # temporarily store old elmeent
        original._element = e           # Replace with new element
        return old_value
    
