class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_height(tree):
    ## Height is calculated from bottom up. we'll need to a post-order traversal
    ## We'll also want to compare left and right heights so let's make two calls
    # Returns -1 if is not a binary tree. The height if it is.
    # Recursive function to find the height of a sub tree
    # We keep calculating height (max height between two subtrees) and checking balance.
    # If unblaanced return -1
    # An None tree has 0 balance of a tree
    if tree is None:
        return 0
    
    left_height = tree_height(tree.left)
    right_height = tree_height(tree.right)
    
    ## After realising we return -1 on an unbalanced tree, we can just pass that back up
    # Will need to use post order i.e. on the way back up to 
    # We will use -1 to say that a tree is unbalanced
    # So if either the left of right tree is unbalanced, return -1
    if left_height is -1 or right_height is -1:
        return -1

    ## Return minus -1 should height difference, we then realise we can short circuit 
    # Otherwise check the difference between left and right subtree
    # if greater than 1, unbalanced
    if abs(left_height - right_height) > 1:
        return -1
    
    # Otherwise, balanced, let's pass up the height
    # I.e. height can only ever be +ve
    # As we are looking for height, increase by 1
    return max(left_height, right_height) + 1

def is_balanced(tree: Node) -> bool:
    return tree_height(tree) != -1

def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == '__main__':
    tree = build_tree(iter(input().split()), int)
    res = is_balanced(tree)
    print('true' if res else 'false')

