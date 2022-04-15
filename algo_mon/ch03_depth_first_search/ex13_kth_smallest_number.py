class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kth_smallest(bst: Node, k: int) -> int:
    """ We know that root is m + 1th largerst value, where m is size of left subtree
    
    if k = m + 1: root is kth element
    else if k < m + 1: look in right subtree and find smallest value (finding the k - m - 1 which is k - (m + 1))
        That is e.g. if root is m + 1 = 5 and k is 7, we need to the 2nd i.e. 7th - 5th smallest value there
    else if k > m + 1: look in left subtree and find the smallest value there
        That is is m + 1 = 5 and k = 2, we need to find k = 2 in left subtree
    
    O(n) to calculate tree size
    O(k) to find k
    """
    # value i.e. the value of node to be output
    val = None 
    
    def tree_size(tree: Node, existing_k: int):
        """ The purpose of this function is to find the tree size and once we find a size matching k
        exit and output value
        
        Existing k should start at 0
        We use nonlocal val to avoid having to declare a big local variable
        """
        
        nonlocal val
        
        if val is not None: # If we've assigned the val, escape, no need for any more recursion
            return None 
        if tree is None: # If tree is empty return none
            return 0 # Start of returning the size of the tree
        
        # We get the size of the left tree
        # This also covers the case where k < m + 1 of the current root
        left_size = tree_size(tree.left, existing_k) 
        
        if val is not None: # If we've assigned the val, escape, no need for any more recursion
            return None
        if left_size + existing_k + 1 == k: # checking if the root is covered
            val = tree.val
            return None # escape
        
        # It must be the case it's the right 
        right_size = tree_size(tree.right, existing_k + left_size + 1)
        
        if val is not None: # If we've assigned the val, escape, no need for any more recursion
            return None
        
        # Return size of tree, no matches so return the size for the previous call
        return left_size + right_size + 1 
    
    tree_size(bst, 0) # Notice how we call tree size but don't assign. We just want the val
    return val

def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == '__main__':
    bst = build_tree(iter(input().split()), int)
    k = int(input())
    res = kth_smallest(bst, k)
    print(res)

## Effective just calculting the tree size
# wth inorder step to check it kth value + early escapes
    # Effective this is just calcualting the size of the array and at the inorder step, checking if we're at the kth int
    
def kth_smallest(bst: Node, k: int) -> int:
    # Effective this is just calcualting the size of the array and at the inorder step, checking if we're at the kth int
    
    def tree_size(tree):
        if tree is None:
            return 0
        
        left_size = tree_size(tree.left)
        
        right_size = tree_size(tree.right)
        
        return left_size + right_size + 1
    
    return tree_size(bst)
