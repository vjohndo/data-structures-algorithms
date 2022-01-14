from TreeMap import TreeMap

class RebBlackTreeMap(TreeMap):
    """Sorted map implementation using a red-black tree."""
    
    class _Node(TreeMap._Node):
        """Node class for red-black tree maintains bit that denots color."""
        
        __slots__ = '_red' # additional data member to the Node class

        def __init__(self, element, parent=None, left=None, right=None):
            super().__init__(element, parent, left, right)
            self._red = True # New node is red by default


    # --- Positional-based utility methods
    # Consider a nonexistent child to be trivially black
    def _set_red(self, p):
        # P is a position, from the position access the node, from the node access the _red instance variable
        p._node._red = True

    def _set_black(self, p):
        p._node._red = False

    def _set_color(self, p, make_red):
        # self_color will be passed with a conditional as a third argument
        p._node._red = make_red

    def _is_red(self, p):
        return p is not None and p._node._red
    
    def _is_red_leaf(self, p):
        return self._is_red(p) and self.is_leaf(p)

    def _get_red_child(self, p):
        """Return a red child of p (or Nont if no such child)."""
        for child in (self.left(p), self.right(p)):
            if self._is_red(child):
                return child
        return None


    # --- Support for insertions
    # Overwrite the hooks to implement support for insertions 
    def _rebalance_insert(self, p):
        self._resolve_red(p)

    def _resolve_red(self, p):
        if self.is_root(p): # always make the root black
            self._set_black(p)
        else:
            parent = self.parent(p)
            # check if 'double red' two cases for a mishappened 4-node and overflown 5-node
            if self._is_red(parent):
                uncle = self.sibling(parent) # Method inherited from Binary Tree >> LinkedBinaryTree >> TreeMap
                if not self._is_red(uncle):
                    # if uncle's sibling is black or none, trinode restructure
                    middle = self._restructure(p) # Method for restructuring returns the new "root"
                    self._set_black(middle)
                    self._set_red(self.left(middle))
                    self._set_red(self.right(middle))
                else:
                    # Else must be the overfull state --> recolor and try again on the new grandparent
                    # Rememeber that the child is being added to the parent, parent is on the same level as uncle
                    grand = self.parent(parent)
                    self._set_red(grand) 
                    self._set_black(self.left(grand))
                    self._set_black(self.right(grand))
                    self._resolve_red(grand)
            # If not a double-red, no further action required

    # --- Support for deletions
    def _rebalance_delete(self, p):
        # Remember that p being passed in the parent of the node that was just removed
        # It would have already connected the removed's child node to the removed's parent
        # There can only be three main types of cases: No child, 1 child, 2 children.
        if len(self) == 1:
            # Always ensure that the root is black 
            self._set_black(self.root())
        elif p is not None:
            n = self.num_children(p)
            # if n == 0: it was definitely a red leaf (case after insertion and any deletion)

            if n == 1:
                # next() retrieves the nextitem from an iterator, recall that children() returns an iterator
                # I.e. retrieve the only child of of this tree
                c = next(self.children(p)) # One of the children will be None
                if not self._is_red_leaf(c):
                    # If the removed child was a black leaf, by necessity, it's sibling MUST have been black leaf too
                    # A removed black leaf means a deficit has been caused 
                    self._fix_deficit(p, c) # p ==> parent, c ==> child of p i.e. the heavier subtree
                # If the only child is red, no deficit has been created, it's sibling must have been red too
                # Remember if we are dealing with LEAF nodes for deletion, 
                # if a node had TWO leaf children they must both be black (after a restructuring) or both red (fresh insertions)
            
            elif n == 2:
                # Removed node had 1 red child, and it can be promoted
                # We can guarantee it is red because the null subtree must have had black depth of 0, 
                if self._is_red_leaf(self.left(p)):
                    self._set_black(self.left(p))
                else:
                    self._set_black(self.right(p))

    def _fix_deficit(self, z, y):
        """Resoolve black deficit at z, where y is the root of z's heavier subtree"""
        if not self._is_red(y): 
            x = self._get_red_child(y)
            if x is not None: # i.e. x has a red child --> restruct and recolor
                old_color = self._is_red(z)
                middle = self._restructure(x)
                self._set_color(middle, old_color)
                self._set_black(self.left(middle))
                self._set_black(self.right(middle))
            else: # Case 2: y is black, but no red child --> recolor
                self._set_red(y)
                if self._is_red(z):
                    self._set_black(z) # set the parent to black, terminating any unbalanced
                elif not self.is_root(z):
                    # will need to recur upward as the local subtree, rooted at z has just had it's black depth reduced by 1
                    self._fix_deficit(self.parent(z), self.sibling(z))

        else: # Case 3; y is red
            self._rotate(y)
            self._set_black(y)
            self._set_red(z)
            
            # Need to reapply the algorithm with the root at z and heavy subtree (which is inbetween y, z)
            if z == self.right(y):
                self._fix_deficit(z, self.left(z))
            else:
                self._fix_deficit(z, self.right(z))