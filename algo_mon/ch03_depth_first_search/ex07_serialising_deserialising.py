class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root: Node) -> str:
    # WRITE YOUR BRILLIANT CODE HERE
    results = []
    
    def dfs(root):
        if root is None:
            results.append('x')
            return
  
        results.append(root.val)
        dfs(root.left)
        dfs(root.right)
        return # superfluous
    
    dfs(root)
    return " ".join(results)
    
def deserialize(s):
    # Given a string, keep returning nodes
    
    # given an iterator to progress
    def dfs(nodes):
        # utilised next and iter!!!
        val = next(nodes) #returns the next value in the nodes iterator
        
        if val == 'x': 
            return
        
        # Reconstruct using preorder
        cur = Node(int(val)) # Create a node with int as value
        cur.left = dfs(nodes) # Set left to the next i (pre order op)
        cur.right = dfs(nodes) # Set the right to the next i (pre order op)
        return cur # Return the completed node to be set as the left and right indexes (post order op)
    
    # iter is an object so can be reffed from inside function
    # it keeps track of the current index for next
    return dfs(iter(s.split()))
        

if __name__ =="__main__":
    # driver code, do not modify
    def build_tree(nodes):
        val = next(nodes)
        if not val or val == 'x': return
        cur = Node(val)
        cur.left = build_tree(nodes)
        cur.right = build_tree(nodes)
        return cur
    def print_tree(root):
        if not root: 
            yield "x"
            return
        yield str(root.val)
        yield from print_tree(root.left)
        yield from print_tree(root.right)
    root = build_tree(iter(input().split()))
    new_root = deserialize(serialize(root))
    print(' '.join(print_tree(new_root)))