# "(", add a new node as the left child of the current node, and descend to the left child.

# ["+", "-", "/", "*"], current node root = operator. new node as the right child and descend to it.

# Number, set the root value of the current node to the number and return to the parent.

# ")", go to the parent of the current node.

# We will need a stack and a binary tree:

import operator

class Stack:

    def __init__(self):
        self._items = []

    def is_empty(self):
        return not bool(self._items)
    
    def push(self, item):
        self._items.append(item)
    
    def pop(self):
        return self._items.pop()
    
    def peek(self):
        return self._items[-1]
    
    def size(self):
        return len(self._items)

class BinaryTree:
    def __init__(self, key):
        self._key = key
        self._child_left = None
        self._child_right = None

    def get_root_val(self):
        return self._key

    def set_root_val(self, key):
        self._key = key

    root = property(get_root_val, set_root_val)

    def get_child_left(self):
        return self._child_left

    def set_child_left(self, node):
        self._child_left = node
    
    child_left = property(get_child_left, set_child_left)

    def get_child_right(self):
        """Get right child"""
        return self._child_right

    def set_child_right(self, node):
        """Set right child"""
        self._child_right = node

    child_right = property(get_child_right, set_child_right)

    def is_left(self):
        return (not self._child_left) and (not self._child_right)

    def insert_right(self, new_node):
        # Only want to be able to add in a new node if it's a binary tree

        if isinstance(new_node, BinaryTree):
            new_subtree = new_node
        else:
            new_subtree = BinaryTree(new_node)


        # Since self._child_right can only be a None or a Binary Tree
        if self._child_right:
            
            # If the self._child_right exists, make it a child of the new subtree
            new_subtree.set_child_left(self._child_right)

        # Now you can add in the new sub tree as a child 
        self._child_right = new_subtree

    def insert_left(self, new_node):
        if isinstance(new_node, BinaryTree):
            new_subtree = new_node
        else:
            new_subtree = BinaryTree(new_node)

        # reassign to existing left child as new node's left child if needed
        if self._child_left:
            new_subtree.set_child_right(self._child_right)
        
        self._child_left = new_subtree

    def postorder(self):
        """Post-order tree traversal"""
        if self._child_left:
            self._child_left.postorder()
        if self._child_right:
            self._child_right.postorder()
        print(self._key, end=" ")

def build_parse_tree(fp_expr):
    fp_list = fp_expr.split()
    parent_stack = Stack()

    expression_tree = BinaryTree("")
    parent_stack.push(expression_tree)
    current_tree = expression_tree

    for token in fp_list:
        if token == "(":
            current_tree.insert_left("")
            parent_stack.push(current_tree)
            current_tree = current_tree.child_left

        elif token in ['+','-','/','*']:
            current_tree.root = token
            current_tree.insert_right("")
            parent_stack.push(current_tree)
            current_tree = current_tree.child_right

        elif token == ")":
            current_tree = parent_stack.pop()
        
        elif token not in ["+", "-", "*", "/", ")"]:
            # So it's not an operator, must be an operand
            try:
                current_tree.root = int(token)
                current_tree = parent_stack.pop()
            except:
                raise ValueError("token '{}' is not a valid integer".format(token))

    return expression_tree

pt = build_parse_tree("( ( 10 + 5 ) * 3 )")
pt.postorder()

def evaluate(parse_tree):
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
    }

    left_child = parse_tree.child_left
    right_child = parse_tree.child_right

    # If both the left and right child exist... i.e. not a leaf load
    if left_child and right_child:
        operator_function = operators[parse_tree.root]
        return operator_function(evaluate(left_child), evaluate(right_child))
    else:
        # Base case, this is not a leaf node, return
        return parse_tree.root

print("=",evaluate(pt))