# Using a list to develop and understanding of a tree
# Tree will have left and right subtrees for each node
# i.e. this is the following structure: [Root, subtree, subtree]
my_tree = [
    "a",
        ["b",
            ["d", [], []],
            ["e", [], []]
        ],
        ["c", 
            ["f", [], []],
            []
        ],
    ]

def display(my_tree):
    print("left subtree = ", my_tree[1])
    print("root = ", my_tree[0])
    print("right subtree = ", my_tree[2])

display(my_tree)

# Let's make some functions to make it easy to use lists as trees
def make_binary_tree(root):
    """Conctructs a list with a root node and two empty sublists for the children"""
    # Due to the way binary trees always have a left and right child node, we can approach them recrussively, more on that later.
    return [root, [], []]


# Let's try to implement a function that allows to add a child
# But we need to keep track of it and push it down the tree
def insert_left(root, new_child):
    """Inserts node into the tree"""

    # Pop the left child, remember the child will be [] or [something]
    old_child = root.pop(1)

    # if the old child is not empty
    if len(old_child) > 1:
        # Add in the new child, with the old_child as the first child
        root.insert(1, [new_child, old_child, []])

    # Else the node must be empty
    else:
        # Insert in the new node with edges set up for the child node
        root.insert(1, [new_child, [], []])
    
    return root

def insert_right(root, new_child):
    """ splices right node into the tree, should there be an existing node there push it down a level on RHS"""
    old_child = root.pop(2)

    if len(old_child) > 1:
        root.insert(2, [new_child, [], old_child])
    else:
        root.insert(2, [new_child, [], []])

def get_root_val(root):
    return root[0]

def set_root_val(root, new_value):
    root[0] = new_value

def get_left_child(root):
    return root[1]

def get_right_child(root):
    return root[2]


a_tree = make_binary_tree(3)
insert_left(a_tree, 4)
insert_left(a_tree, 5)
insert_right(a_tree, 6)
insert_right(a_tree, 7)
left_child = get_left_child(a_tree)
print(left_child)

set_root_val(left_child, 9)
print(a_tree)
insert_left(left_child, 11)
print(a_tree)
print(get_right_child(get_right_child(a_tree)))


def build_tree():
    exercise_tree = make_binary_tree('a')
    insert_left(exercise_tree,'b')
    insert_right(get_left_child(exercise_tree),'d')

    insert_right(exercise_tree,'c')
    insert_right(get_right_child(exercise_tree),'f')
    insert_left(get_right_child(exercise_tree),'e')

    print(exercise_tree)
    return exercise_tree

build_tree()