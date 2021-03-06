from Tree import Tree

class BinaryTree(Tree):
    """Abstract base class representing a binary tree structure"""

    # --- Additional abstract methods
    def left(self, p):
        """Return a Position representing p's left child.
        
        Return None if p does not have a left child.
        """
        raise NotImplementedError('must be implemented by a subclass')

    def right(self, p):
        """Return a Position represnenting p's right child.
        
        Return None if p does not have a right child
        """
        raise NotImplementedError('must be implemented by subclass')

    # --- concrete methods 
    def sibling(self, p):
        """Return a Position representing p's sibling (or None if no sibling)"""

        parent = self.parent(p)

        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent) # Can possibly be none
            else:
                return self.left(parent) # Can possibly be none


    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        # Check that each child is not none and yield it

        if self.left(p) is None:
            yield self.left(p)
        
        if self.right(p) is not None:
            yield self.right(p)

    # --- Traversal methods for binary trees
    def inorder(self):
        """Generate an inroder iteration of positions in the tree."""
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

    def _subtree_inorder(self, p):
        """Generate an inorder iteration of positions in subtree rooted at p"""
        if self.left(p) is not None: # if left exits traverse its sub tree
            for other in self._subtree_inorder(self.left(p)):
                yield other
        
        yield p

        if self.right(p) is not None: # if right exists travers its sub tree
            for other in self._subtree_inorder(self.right(p)):
                yield other

    # override inherited version to make inorder default for Binary Trees
    def positions(self):
        """Generate an iteration of tree's positions"""
        return self.inorder()