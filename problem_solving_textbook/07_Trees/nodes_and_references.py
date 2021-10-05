class BinaryTree:
    """
    Node for binary tree
    
    Init variables are for:
    root_object

    """
    def __init__(self, root_obj):
        self.key = root_obj
        self.left_child = None
        self.right_child = None


    def insert_right(self, new_node):
        if self.right_child is None:
            # Create a new instance of the binary tree
            self.right_child = BinaryTree(new_node)
        
        else:
            # Create a new instance of the binary tree
            new_child = BinaryTree(new_node)
            
            # Point to the current right child
            new_child.right_child = self.right_child

            # Reassign right_child to the new node.. linked list style
            self.right_child = new_child

    def insert_left(self, new_node):
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        else:
            new_child = BinaryTree(new_node)
            new_child.right_child = self.left_child
            self.left_child = new_child

    # Defining accessor methods
    def get_root_val(self):
        return self.key
    
    def set_root_val(self, new_obj):
        self.key = new_obj

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

a_tree = BinaryTree("a")
print(a_tree.get_root_val())
print(a_tree.get_left_child())
a_tree.insert_left("b")
print(a_tree.get_left_child())
print(a_tree.get_left_child().get_root_val())
a_tree.insert_right("c")
print(a_tree.get_right_child())
print(a_tree.get_right_child().get_root_val())
a_tree.get_right_child().set_root_val("hello")
print(a_tree.get_right_child().get_root_val())


def build_tree():
    a_tree = BinaryTree("a")
    a_tree.insert_left("b")
    a_tree.get_left_child().insert_right("d")

    a_tree.insert_right("c")
    a_tree.get_right_child().insert_right("f")
    a_tree.get_right_child().insert_left("e")

    return a_tree

a = build_tree()

print(a.get_right_child().get_left_child().get_root_val())