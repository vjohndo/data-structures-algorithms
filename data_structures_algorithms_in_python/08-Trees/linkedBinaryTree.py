from BinaryTree import BinaryTree

class LinkedBinaryTree(BinaryTree):
    """Linked representation of a binary tree structure"""

    class _Node:
        """Light weight non public class for storing a node"""
        __slots__ = '_element', '_parent', '_left', '_right'

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position:
        """Public class, an abstraction (of the node) representing the location of a single element"""

        def __init__(self, container, node):
            """Costructor should not be invoked by user"""
            self._container = container
            self._node = node

        def element(self):
            """Return the element stored at this Position"""
            return self._node._element # Returns the _Node _element

        def __eq__(self, other):
            """Return True if other is a Position representing the same location"""
            return type(other) is type(self) and other._node is self._node
            
        # def __ne__ has already been inherited from the Abstract Base Class

    # --- utility methods
    def _validate(self, p):
        """Return associated node, if position is valid"""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        
        if p._container is not self:
            raise ValueError('p does not belong to this container')

        if p._node._parent is p._node: # this is a convention for deprecated nodes
            raise ValueError('p is no longer valid')

        return p._node

    def _make_position(self, node):
        """Return Position instance for given noe (or None if no node)."""
        # useful for wraping the node and returning it as a position
        return self.Position(node) if node is not None else None

    # --- binary tree constructor
    def __init__(self):
        """Create an initiall empty binary tree"""
        self._root = None
        self._size = 0

    def root(self):
        """Return the root Position of the tree (or None if tree is mpety)"""
        return self._make_position(self._root)

    def parent(self, p):
        """Return the Position of p's parent (or None if p is root)"""
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        """Return the Position of p's left child (or None if no left child"""
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        """Return the Position of p's right child (or None if no left child)"""
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        """Return the number of children of Position p."""
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        
        return count

    # --- Update methods, notice that they are all nonpublic
    def _add_root(self, e):
        """Place element e at the root of an empty tree and return new Position
        
        Raise ValueError if tree nonempty
        """
        if self._root is not None:
            raise ValueError('Root exists')
        
        self._size = 1
        self._root = self._Node(e)

        return self._make_position(self._root)

    def _add_left(self, p, e):
        """Cretae a new left child for Postion p, storing element e
        
        Return the Position of new node
        Raise ValueError if Postion p is invalid of p already has a left child.
        """
        node = self._validate(p)

        if node._left is not None:
            raise ValueError('Left child exists')
        
        self._size += 1
        node._left = self._Node(e, node) # recall that out concrete implementation has node __init__(self, element, parent, left, right)

        return self._make_position(node._left)

    def _add_right(self, p, e):
        """Create a new right child for position p, storing element e
        
        Return the Position of new node
        Riase ValueError is Position p is invalid of p already has a right child
        """

        node = self._validate(p)

        if node._right is not None:
            raise ValueError('Right child exists')

        self._size += 1
        node._right = self._Node(e, node)

        return self._make_position(node._right)

    def _replace(self, p, e):
        """Replace the element at position p with e, and return old elmeent"""
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def _delete(self, p):
        """Delete the node at Position p, and replace it with its child if any.
        
        Return the element that had been stored at Position p.
        Raise ValueError if Position p is invalid or p has two children
        """
        node = self._validate(p)
        if self.num_children(p) == 2: 
            raise ValueError('p has two children')
        
        # Grab the left node child node if it exists, otherwise grab the right node (if it too exists, otherwise it will be None)
        child = node._left if node._left else node._right


        # If the child is not None, we need to link it to the parent of the node node we are deleting
        if child is not None:
            child._parent = node._parent # the link "up" the tree

        # Node need to link the parent the child
        if node is self._root:
            self._root = child # Case where the node to be deleted was the root. Need to point the root to the child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child # If the node to be deleted was a left child of parent, replace
            else:
                parent._right = child # If the node to be delted was a right child of parent, replace
            
        self._size -= 1

        node._parent = node # convention for deprecated node
        
        return node._element


    def _attach(self, p, t1, t2):
        """Attach trees t1 and t2 as left and right subtrees of extrenal p."""
        node = self._validate(p)

        if not self.is_leaf(p):
            raise ValueError('position must be lead')

        if not type(self) is type(t1) is type(t2): # all 3 trees must be same type
            raise TypeError('Tree types must match')

        self._size += len(t1) + len(t2)

        if not t1.is_empty():
            t1._root._parent = node # where node is the node we are attaching t1 to
            node._left = t1._root

            # Then set the t1 tree instance to empty
            t1._root = None
            t1._size = 0

        if not t2.is_empty():
            t2._root._parent = node 
            node._right = t2._root

            # Then set the t2 tree instance to empty
            t2._root = None
            t2._size = 0