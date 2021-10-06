from pythonds3.trees import BinaryTree

a = BinaryTree()

def preorder(tree):
    """ Root, Left, Right """
    """ Often have traversal functions as external as you rarely ever just want to traverse for the sake of traversing """
    if tree:
        print(tree.get_root_val())
        preorder(tree.get_left_child())
        preorder(tree.tree.get_right_child())

def postorder(tree):
    if tree:
        postorder(tree.get_left_child())
        postorder(tree.get_right_child())
        print(tree.get_rool_val())
    
def inorder(tree):
    if tree:
        inorder(tree.get_left_child())
        print(tree.get_root_val())
        inorder(tree.get_right_child())


class BinaryTree:
    def __init__(self, key):
        self._key = key
        self._child_left = None
        self._child_right = None

    def get_root_val(self):
        return self._key

    def set_root_val(self, key):
        self._key = key

    root = property(get_root_val, set_root_val)

    def get_child_left(self):
        return self._child_left

    def set_child_left(self, node):
        self._child_left = node
    
    left_child = property(get_child_left, set_child_left)

    def get_child_right(self):
        """Get right child"""
        return self._child_right

    def set_child_right(self, node):
        """Set right child"""
        self._child_right = node

    right_child = property(get_child_right, set_child_right)

    def preorder(self):
        print(self.key)
        if self.left_child:
            self.left_child.preoder()

        if self.right_child:
            self.right_child.preorder()