from typing import List

class Node:
    def __init__(self, val, children=None):
        if children is None:
            children = []
        self.val = val
        self.children = children

def ternary_tree_paths(root: Node) -> List[str]:
    # dfs helper function
    # we'll pass down our existing path
    # and we'll keep a reference to a response which contains strings of paths
    
    def dfs(root, path, res):
        # exit condition, reached lead node, append path to results
        if all(c is None for c in root.children): # List comprehension
            res.append('->'.join(path) + '->' + str(root.val))
            return
        
        # dfs on each non-null child
        for child in root.children:
            dfs(child, path + [str(root.val)], res) # Notice how we're creating a new path list on each call
            
    res = []
    if root: # Only if root exists do we do dfs
        dfs(root, [], res)
    return res
    
def build_tree(nodes, f):
    val = next(nodes)
    num = int(next(nodes))
    children = [build_tree(nodes, f) for _ in range(num)]
    return Node(f(val), children)

if __name__ == '__main__':
    root = build_tree(iter(input().split()), int)
    res = ternary_tree_paths(root)
    for line in res:
        print(line)
