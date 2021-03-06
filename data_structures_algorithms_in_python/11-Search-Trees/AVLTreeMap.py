from TreeMap import TreeMap

class AVLTreeMap(TreeMap):
    """Sorted map implementation using an AVL Tree"""

    # --- nested _Node class
    class _Node(TreeMap._node):
        """Node class for AVL maintains height value for balancing"""
        __slots__ = '_height'

        def __init__(self, element, parent=None, left=None, right=None):
            super().__init__(element, parent, left, right)
            self._height = 0 # Gets recomputed during balanacing 

        def left_height(self):
            return self._left._height if self._left is not None else 0
        
        def right_height(self):
            return self._right._height if self._right is not None else 0

    # --- positional-based utility methods
    def _recompute_height(self, p):
        p._node._height = 1 + max(p._node.left_height(), p._node.right_height()) # Access the Position's _node

    def _isbalanced(self, p):
        return (abs(p._node.left_height() - p._node.right_height()) <= 1)

    def _tall_child(self, p, favourleft=False): #The third param controls the tiebreaker
        # Notice favour left and the greater than sign.
        # If left = right and not favouring left will return right
        # If left = right and favouring left will return left
        if p._node.left_height() + (1 if favourleft else 0) > p._node.right_height():
            return self.left(p)
        else:
            return self.right(p)

    def _tall_grandchild(self, p):
        child = self._tall_child(p)
        # check the aligment
        aligment = (child == self.left(p)) # Check if the child is the left of p
        return self._tall_child(child, aligment) # if child id left, pass it in

    def _rebalance(self, p):
        while p is not None:
            old_height = p._node._height
            if not self._isbalanced(p): # detect if any imbalance
                # Need to do trinode restructure. after the restructure reassign p as the new root
                # Recalculate the heights for new roots children
                p = self._restructure(self._tall_grandchild(p))
                self._recompute_height(self.left(p))
                self._recompute_height(self.right(p))
            
            # calculate the height 
            self._recompute_height(p)
            if p._node._height == old_height:
                # If the height of the subtree has not changed, rest of the AVL tree remains intact. Stop looping\
                # This will be the case for insertaion
                p = None
            else:
                # This MAY be the case for deletion
                p = self.parent(p) # else keep looping on the parent
    
    # --- override balancing hooks
    def _rebalance_insert(self, p):
        self._rebalance(p)
    
    def _rebalance_delete(self, p):
        # Note that p passed in the parent
        self._rebalance(p)
