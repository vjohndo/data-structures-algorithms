from base.LinkedBinaryTree import LinkedBinaryTree
from base.MapBase import MapBase

class TreeMap(LinkedBinaryTree, MapBase):
    """Sorted map implementation using a binary search tree"""

    # --- override Position Class
    class Position(LinkedBinaryTree.Position):
        def key(self):
            """Return key of a map's key-value pair."""
            return self.element()._key

        def value(self):
            """Return value of a map's key-value pair."""
            return self.element()._value

    # --- nonpublic utilities
    def _subtree_search(self, p, k):
        """Return position of P's subtree having key k, or last node searched."""
        
        if k == p.key():
            return p
        elif k < p.key():
            if self.left(p) is not None:
                return self._subtree_search(self.left(p), k)
        else:
            if self.right(p) is not None:
                return self._subtree_search(self.right(p), k)
        # Base case, p is passed in as none as there are no children / match found
        return p  

    def _subtree_first_position(self, p):
        """Return Position of first item in subtree rooted at p."""
        walk = p
        while self.left(walk) is not None:
            walk = self.left(walk)
        return walk

    def _subtree_last_position(self, p):
        """Return Position of last item in subtree rooted at p."""
        walk = p 
        while self.right(walk) is not None:
            walk = self.right(walk)
        return walk
    
    def first(self):
        """Return the first Position in the tree (or None if empty)."""
        return self._subtree_first_position(self.root()) if len(self) > 0 else None

    def last(self):
        """Return the last Position in the tree (or None if empty)."""
        return self._subtree_last_position(self.root()) if len(self) > 0 else None

    def before(self, p):
        """Return the Position just before p in the natural order
        
        Return None if p is the first position
        """
        self._validate(p) # inherited from LinkedBinaryTree
        
        # If left child, check the right moset of the left subtree
        if self.left(p): 
            return self._subtree_last_position(self.left(p))
        # Otherwise find the ancestor that has p as in its right subtree
        else:
            walk = p
            above = self.parent(walk) 
            # keep looping until we've hit none (root) or found an ancestor with p in right subtree
            while above is not None and walk == self.left(above):
                walk = above
                above = self.parent(walk)
            return above
        
    def after(self, p):
        """Return then Position just after p in the natural order
        
        Return None if p is the frist position
        """
        self._validate(p) # inherited from LinkedBinaryTree
        if self.right(p):
            # If there is a right child, get the leftmost node in the right child
            return self._subtree_first_position(self.right(p))
        else:
            walk = p
            above = self.parent(walk)
            # Keep looping until None or found an ancestor with p in left subtree
            while above is not None and walk == self.right(above):
                walk = above
                above = self.parent(walk)
            return above
    
    def find_position(self, k):
        """Return position with key k or else neighbor (or Nont if empty)."""
        if self.is_empty():
            return None
        else:
            p = self._subtree_search(self.root(), k)
            self._rebalance_access(p) # hook for balanced tree subclass
            return p
    
    def find_min(self):
        """Return (key, value) pair with min key (or None if empty)"""
        if self.is_empty():
            return None
        else:
            p = self.first() # Go to the left most node
            return (p.key(), p.value())

    def find_ge(self, k):
        """Return (key, value) pair with least key greater than or equal to k.
        
        Return None ifthere does not exist such a key
        """
        if self.is_empty():
            return None
        else:
            p = self.find_position(k)
            if p.key() < k: # may not be be able to find exact k. don't need to have if statement for >= as binary tree goes from parent to child.
                p = self.after(p)
            return (p.key(), p.value()) if p is not None else None

    def find_range(self, start, stop):
        """Iterate all (key, value) pairs sutch that start <= key < stop
        
        
        If start is None, iteration begins with minimum key of map.
        If stop is None, iteration continue sthrough the max key of map.
        """
        if not self.is_empty():
            # Initialise the start if it's not defined
            if start is None:
                p = self.first()

            else:
                p = self.find_position(start)
                # Make start that we are at least start <= p.key()
                if p.key() < start:
                    p = self.after(p)

                #Now start to loop and yield
                while p is not None and (stop is None or p.key() < stop):
                    yield (p.key(), p.value())
                    p = self.after(p)
    
    def __getitem__(self, k):
        """Return value associated with key k (raise KeyError if not found)."""
        if self.is_empty():
            raise KeyError('Key Error: ' + repr(k))
        else:
            p = self._subtree_search(self.root(), k)
            self._rebalance_access(p) # hook for balanced tree subclasses
            if k != p.key():
                raise KeyError('Key Error: ' + repr(k))
            return p.value()

    def __setitem__(self, k, v):
        """Assign value v to key k, overwriting existing value if present"""
        if self.is_empty():
            leaf = self._add_root(self._Item(k, v))
        else:
            p = self._subtree_search(self.root(), k)
            if p.key() == k:
                # Note that a position points to a node. The nodes element should point to a Item which has a key value pair
                p.element()._value = v
                self._rebalance_access(p) # Hook for balanced tree subclasses
                return
            else:
                item = self._Item(k,v)
                if p.key() < k:
                    # Remeber that insertion will always be a leaf node
                    leaf = self._add_right(p, item)
                else:
                    leaf = self._add_left(p, item)
        self._rebalance_insert(leaf) # Hook for balanced tree subclasses

    def __iter__(self):
        """Generate an iteration of all keys in the map in order"""
        p = self.first()
        while p is not None:
            yield p.key()
            p = self.after(p)

    def delete(self, p):
        """Remove the item at given Position."""
        self._validate(p)
        # Procedure for two-child case
        if self.left(p) and self.right(p):
            replacement = self._subtree_last_position(self.left(p))
            self._replace(p, replacement.element())
            p = replacement
        # Not p has at most one child
        parent = self.parent(p) # Needed for the below hook for the balanced tree subclass
        self._delete(p) # Inherited from LinkedBinaryTree, works for 1 child only.
        self._rebalance_delete(parent) # If root is deleted, parent is None 

    def __delitem__(self, k):
        """Remove item assocaited with key k (raise KeyError if not found)."""
        if not self.is_empty():
            p = self._subtree_search(self.root(), k)
            if k == p.key():
                self.delete(p)
                return
            self._rebalance_access(p) # Hook for balanced tree subclass
        raise KeyError('Key Error: ' + repr(k))