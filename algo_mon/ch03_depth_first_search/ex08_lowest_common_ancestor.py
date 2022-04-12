class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lca(root, node1, node2):
    # How to breakdown the problem #
    # What is the simpliest case:
    # # A node is a descendant of itself
    # # What is the deepest node with v & w as descendants
    # # We want to pass the state of LCA up until we 
    
    
    # If root is none, we couldn't find LCA in the tree
    if not root:
        return None
    
    # If a node is itself an ancestor, it must be the lowest common ancestor
    # - other node will be below it
    if root == node1 or root == node2:
        return root
    
    # Done with pre-order check, need information from the bottom up now
    # Will need to do recurssion on left and right subtree
    left = lca(root.left, node1, node2)
    right = lca(root.right, node1, node2)
    
    # If we've found LCA in both left and right subtree,
    # LCA can't be in both, the root must be true
    if left and right:
        return root
    
    # If only left, LCA found in left subtree
    # pass up the LCA state on left
    if left:
        return left
    
    # If only right, LCA found in right subtree
    # pass up the LCA state on right
    if right:
        return right
    
    # If we can't find it return null
    return None
    
    
    

if __name__ == "__main__":
    # driver code, do not modify
    def build_tree(nodes):
        val = next(nodes)
        if not val or val == 'x': return
        cur = Node(val)
        cur.left = build_tree(nodes)
        cur.right = build_tree(nodes)
        return cur
    def find_node(root, target):
        if not root: return
        if root.val == target: return root
        return find_node(root.left, target) or find_node(root.right, target)
    s = input().split()
    root = build_tree(iter(s))
    node1 = find_node(root, input())
    node2 = find_node(root, input())
    ans = lca(root, node1, node2)
    if not ans: print('null')
    else: print(ans.val)