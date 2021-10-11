class BinarySearchTree:
    """ used to define a tree node """
    def __init__(self):
        # Root refers to the an instance of TreeNode or None if it is empty
        self.root = None
        # Refers to the size of the tree
        self.size = 0

    def __len__(self):
        # dunder length function that describes the length of the tree
        return self.size

    def size(self):
        # returns the size of the function
        return self.size

    def __iter__(self):
        # dunder method that creates an iteratble function.
        # it in facts calls upon the iterable function defined by the tree node instance
        return self.root.__iter__()

class TreeNode:
    """ 
    Tree node instance, provides many helper functions 

    > May want to pass in nodes with parent and child hence left, right, parent 

    """

    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        # points to smaller child
        self.left_child = left
        # points to bigger child
        self.right_child = right
        # keeps track of parent node, useful for the delete function
        self.parent = parent

    def is_left_child(self):
        # Does a parent exist and does the parent's left child this specific instance of the TreeNode
        return self.parent and self.parent.left_child is self

    def is_right_child(self):
        # Does a parent exist and does the paresn't right child this specific instance of the TreeNode
        return self.parent and self.parent.right_child is self

    def is_root(self):
        # Only the root does not have a parent. So does this cell have a parent
        return not self.parent

    def is_leaf(self):
        # Leaf nodes have no childrent, return ! should any child be referenced
        return not (self.right_child or self.left_child)

    def has_a_child(self):
        # Is there a left or right child
        return self.right_child or self.left_child

    def has_children(self):
        # Do both instances of the child exist
        return self.right_child and self.left_child

    def replace_value(self, key, value, left, right):
        # replace all the children 
        self.key = key
        self.value = value
        self.left_child = left
        self.right_child = right

        # If we've created/editted the left child 
        if self.left_child:

            # Set that child's parent reference to this instance of TreeNode
            self.left_child.parent = self

        # If we've created/editted the right child
        if self.right_child:

            # Set that child's reference to this instance of Parent
            self.right_child.parent = self