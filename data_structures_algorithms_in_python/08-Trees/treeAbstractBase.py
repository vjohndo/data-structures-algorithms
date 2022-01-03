class Tree:
    """Abstract base class representing a tree structure"""

    #---- nested Position class
    class Position:
        """An abstraction representing the location of a single element."""
        def element(self):
            """Return the element stored at this position"""
            raise NotImplementedError("must be implemented by subclass")

        def __eq__(self, other):
            """Return True if other Position represents the same location"""
            raise NotImplementedError("must be implemented by subclass")

        def __ne__(self, other):
            """Return True if other does not represent the same location"""
            return not (self == other)

    
    # --- Abstract methods that concrete subclass must support
    def root(self):
        """Return Position representing the tree's root (or Nont if empty)"""
        raise NotImplementedError('must be implemented by subclass')

    def parent(self, p):
        """Return Position representing p's parent (or None if p is root)."""
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self, p):
        """Return the number of children that Position p has."""
        raise NotImplementedError('must be implemented by subclass')

    def children(self, p):
        """Generate an iteration of Positions representing p's children"""
        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        """Return the total number of elements in the tree"""
        raise NotImplementedError('must be implemented by subclass')

    #--- Concrete methods implemented in this class
    def is_root(self, p):
        """Return True if Positino p represents the root of the tree."""
        return self.root() == p

    def is_leaf(self, p):
        """Return true if Position p does not have any children"""
        return self.num_children(p) == 0

    def is_empty(self):
        """Return True if the tree is empty"""
        return len(self) == 0

    # --- Additional methods
    def depth(self, p):
        """Return the number of levels separating Position p from the root."""
        if self.is_root(): 
            return 0 # Base case
        else:
            return 1 + self.depth(self.parent(p)) # Progress to parent

    def _height1(self):
        """Return the height of tree."""
        # positions would need to be defined
        # then for each position, if it is a leaf calculate the depth
        # then get the max of each of those depths
        # This is inefficient as say you have a linearly linked tree, it would traverse all the up to the top of the tree at each level
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

    def _height2(self, p):
        """Return the height of hte subtree rooted a position p"""
        if self.is_leaf(p):
            return 0

        else:
            return 1 + max(self._height2(c) for c in self.children(p))

    def height(self, p=None):
        """Return the height of the subtree rooted at Posotion p.
        
        If p is None, return the hright of the entire tree.
        """
        if p is None:
            p = self.root()

        return self._height2(p)