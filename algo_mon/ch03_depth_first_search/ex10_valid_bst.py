class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def valid_bst(root: Node) -> bool:
    # 1) Need post-order info on whether the left and right subtrees are valid BSTs
    # 2) Remeber that anything on the left subtree MUST be 
    def dfs(root, min_val, max_val):
        if not root:
            return True
        
        if not (min_val <= root.val <= max_val):
            return False
        
        # Then check if the left and right are within the ranges
        return dfs(root.left, min_val, root.val) and dfs(root.right, root.val, max_val)
        
    
    return dfs(root, -float("inf"), float("inf"))

def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == '__main__':
    root = build_tree(iter(input().split()), int)
    res = valid_bst(root)
    print('true' if res else 'false')

## My incorrect attempt:
# 1) All on the left must be left, all on the right must be right
# Pass down information to help node return T/F

def valid_bst(root: Node) -> bool:
    # My incorrect attempt.
    def dfs(root):
        if root is None:
            # an empty BST is true
            return Node(None)
        
        left = dfs(root.left)
        right = dfs(root.right)
        
        if not left or not right:
            return None
        
        if not left.val and not right.val:
            return root
        elif not left.val and right.val > root.val:
            return root
        elif left.val < root.val and not right.val:
            return root
        elif left.val < root.val and right.val > root.val:
            return root
       
        return None         
    
    return bool(dfs(root))