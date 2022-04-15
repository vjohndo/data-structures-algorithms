class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_binary_tree(tree: Node) -> Node:
    if tree is None:
        return None
    return Node(tree.val, invert_binary_tree(tree.right), invert_binary_tree(tree.left))

def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

def format_tree(node):
    if node is None:
        yield 'x'
        return
    yield str(node.val)
    yield from format_tree(node.left)
    yield from format_tree(node.right)

if __name__ == '__main__':
    tree = build_tree(iter(input().split()), int)
    res = invert_binary_tree(tree)
    print(' '.join(format_tree(res)))

## Blind implementation
def invert_binary_tree(tree: Node) -> Node:
    # This implementation is actually inplace
    def dfs(node):
        if node:
            dfs(node.left)
            dfs(node.right)
            
            node.left, node.right = node.right, node.left
            
    dfs(tree)
    
    return tree
    
