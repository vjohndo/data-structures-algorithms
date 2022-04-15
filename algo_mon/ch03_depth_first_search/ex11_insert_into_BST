class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert_bst(bst: Node, val: int) -> Node:
    # My own blind implementation, this is actually an inplace function
    # if statement on values matching is uncessary 
    def dfs(node, val):
        if node is None:
            return Node(val)
        
        # This control is superfluous 
        if node.val == val:
            return node
        
        # recusrive cases:
        if val < node.val:
            node.left = dfs(node.left, val)
        elif val > node.val:
            node.right = dfs(node.right, val)
        return node
        
    return dfs(bst, val)

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
    bst = build_tree(iter(input().split()), int)
    val = int(input())
    res = insert_bst(bst, val)
    print(' '.join(format_tree(res)))
