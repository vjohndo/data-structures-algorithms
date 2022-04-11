class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def visible_tree_node(root: Node) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    return 0

def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == '__main__':
    root = build_tree(iter(input().split()), int)
    res = visible_tree_node(root)
    print(res)

### 

def visible_tree_node(root: Node) -> int:
    def dfs(root, max_seen):
        
        if root is None:
            return 0
        
        # Keep track of the total and we'll add to it on our recursive calls
        total = 0
        if root.val >= max_seen:
            total += 1
            max_seen = root.val
            
        # Rather than define a variable, calculate max in function
        total += dfs(root.left, max_seen)
        total += dfs(root.right, max_seen)
        
        return total
                     
    return dfs(root, -float('inf'))