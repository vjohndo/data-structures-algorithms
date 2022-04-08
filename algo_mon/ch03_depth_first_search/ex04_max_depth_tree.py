class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_max_depth(root: Node) -> int:
    if root is None:
        return 0
    
    left_max = tree_max_depth(root.left)
    right_max = tree_max_depth(root.right)
    
    return max(left_max, right_max) + 1

def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == '__main__':
    root = build_tree(iter(input().split()), int)
    res = tree_max_depth(root)
    print(res)
