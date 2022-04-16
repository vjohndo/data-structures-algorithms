class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def flatten_tree(tree: Node) -> Node:
    # If it is an empty tree, return None
    if tree is None:
        return None
    
    head_node = Node(tree.val)
    tail_node = head_node
    tree_stack = [tree.right, tree.left] # Notice how right goes in first as we wanna pop and work on left first 
    
    while tree_stack:
        top = tree_stack.pop()
        if top is None:
            continue #Skip this iteration
        
        tail_node.right = Node(top.val)
        tail_node = tail_node.right
        # Notice how right goes in first as we wanna pop and work on left first
        # This means that as we go down the tree, we're going to pop left, add right & left, pop left, add right & left etc.
        tree_stack.append(top.right) 
        tree_stack.append(top.left)
        
    return head_node

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
    res = flatten_tree(tree)
    print(' '.join(format_tree(res)))