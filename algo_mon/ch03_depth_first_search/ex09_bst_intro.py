class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find(tree, val):
    if tree is None:
        return False
    if tree.val == val:
        return True
    elif tree.val < val:
        return find(tree.right, val)
    else:
        return find(tree.left, val)

def insert(tree, val):
    if tree is None:
        return Node(val)
    if tree.val < val:
        tree.right = insert(tree.right, val)
    elif tree.val > val:
        tree.left = insert(tree.left, val)
    return tree

# 
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find(tree, val):
    if tree is None:
        return None

    if tree.val == val:
        return True

    elif tree.val < val:
        return find(tree.left, val)

    else:
        return find(tree.right, val)

def insert(tree, val):
    # Once it finds an empty spot, insert the node
    if tree is None:
        # Generate the node at the end so it can be 
        # passed back up the tree for insertion
        return Node(val)
    elif tree.val < val:
        # Assign the left to left subtree
        # will attach a Node if there was previously 
        tree.left = insert(tree.left, val)
    elif tree.val > val:
        tree.right = insert(tree.right, val)
    
    return tree