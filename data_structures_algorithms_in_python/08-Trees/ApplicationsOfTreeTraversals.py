from Tree import Tree

T = Tree()

# 1 - Preorder traversal to print out a list
for p in T.preorder():
    print(p.element)

# 2 - Preorder traversal to print out indent with that list
# The trick is to pass through d as the depth
def preorder_indent(T, p, d):
    print(2 * d * ' ' + str(p.element()))
    for c in T.children(p):
        # Call preorder on each of the children, now with a higher depth level which spits out the correct depth
        preorder_indent(T, c, d+1) 

preorder_indent(T, T.root(), 0)

# 3 - Preorder traversal to print out the list as well
def preorder_label(T, p, d, path=[]):
    """Print labeled representation of subtree of T rooted at p at depth d"""
    # Think of path as a stack. depending on the depth of the recursion we can add and pop variables as we go
    label = '.'.join(str(j+1) for j in path)
    print(2*d*' ' + label, p.element())
    path.append(0)

    for c in T.children(p):
        preorder_label(T, c, d+1, path)
        path[-1] += 1 # Go the last path level for this set of iterations with children and increment each time we've recurred
    
    path.pop() # code block must remove the extra entry as it finishes 

# 4 - Parenthetic Representations of a Tree
def parenthesize(T, p):
    """Print parenthesized representation of subtree T rooted at p."""
    # Need to produce opening parenthesis before closing 
    # To do this need to keep track for each instance of the recursion

    print(p.element(), end='') # sets the end to '' so that subsequent prints are not on a new line
    
    if not T.is_leaf(p): # Base case is a leaf node
        first_time = True # The first time we recur to a deeper level, 
        for c in T.children(p): # Returns an iterable of children
            # Determine what is the proper separator
            sep = ' (' if first_time else ','
            print(sep, end='')
            first_time = False
            parenthesize(T,c) # Recir on a lower depth of tree.
        print(')')


# 5 - Computing Disk Space
# We can not compute disk space until after we've looked the children first
# This requires the use of postorder traversal
def disk_space(T, p):
    """Return total disk space for subtree of T rooted at p"""
    subtotal = p.element().space() # Get the space used locally by p
    for c in T.children(p):
        subtotal += disk_space(T, c)

    return subtotal
