from Tree import Tree

T = Tree()

# Preorder traversal to print out a list
for p in T.preorder():
    print(p.element)

# Preorder traversal to print out indent
# The trick is to pass through d as the depth
def preorder_indent(T, p, d):
    print(2 * d * ' ' + str(p.element()))
    for c in T.children(p):
        # Call preorder on each of the children, now with a higher depth level which spits out the correct depth
        preorder_indent(T, c, d+1) 

preorder_indent(T, T.root(), 0)
