from pythonds3.trees.avl_tree import AVLTreeNode


class TreeNode:
    """ 
    Tree node instance, provides many helper functions 

    > May want to pass in nodes with parent and child hence left, right, parent 

    """

    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        # points to smaller child
        self.left_child = left
        # points to bigger child
        self.right_child = right
        # keeps track of parent node, useful for the delete function
        self.parent = parent

    def is_left_child(self):
        # Does a parent exist and does the parent's left child this specific instance of the TreeNode
        return self.parent and self.parent.left_child is self

    def is_right_child(self):
        # Does a parent exist and does the paresn't right child this specific instance of the TreeNode
        return self.parent and self.parent.right_child is self

    def is_root(self):
        # Only the root does not have a parent. So does this cell have a parent
        return not self.parent

    def is_leaf(self):
        # Leaf nodes have no childrent, return ! should any child be referenced
        return not (self.right_child or self.left_child)

    def has_a_child(self):
        # Is there a left or right child
        return self.right_child or self.left_child

    def has_children(self):
        # Do both instances of the child exist
        return self.right_child and self.left_child

    def replace_value(self, key, value, left, right):
        # replace all the children 
        self.key = key
        self.value = value
        self.left_child = left
        self.right_child = right

        # If we've created/editted the left child 
        if self.left_child:

            # Set that child's parent reference to this instance of TreeNode
            self.left_child.parent = self

        # If we've created/editted the right child
        if self.right_child:

            # Set that child's reference to this instance of Parent
            self.right_child.parent = self

class BinarySearchTree:
    """ used to define a tree node """
    def __init__(self):
        # Root refers to the an instance of TreeNode or None if it is empty
        self.root = None
        # Refers to the size of the tree
        self.size = 0

    def __len__(self):
        # dunder length function that describes the length of the tree
        return self.size

    def size(self):
        # returns the size of the function
        return self.size

    def __iter__(self):
        # dunder method that creates an iteratble function.
        # it in facts calls upon the iterable function defined by the tree node instance
        return self.root.__iter__()

    def _put(self, key, value, current_node):
        # if the key to be added to the tree is less than the current node
        if key < current_node.value:
            # if the current node has a left child
            if current_node.left_child:
                # pass the the key into the put helper again
                self._put(key, value, current_node.left_child)
            else:
                # else you've reached a leaf node and create an instance of the tree node with the key, value, parent
                current_node.left_child = TreeNode(key, value, parent=current_node)

        # other wise the key is greater than current node, pass the key along and run the helper function again on the right chil
        else:
            if current_node.right_child:
                self._put(key, value, current_node.right_child)
            else:
                # base case, you've reached a leaf node
                current_node.right_child = TreeNode(key, value, parent=current_node)


    def put(self, key, value):
        """ Checks if there's a root"""
        # if so pass the key value through the helper function
        if self.root:
            # Note that this a recursive function and will arguments will track the "current node"
            self._put(key, value, self.root)
        else:
            # Create a new tree instance if there's no root.
            self.root = TreeNode(key, value)

        self.size += 1

    def __setitem__(self, key, value):
        self.put(key,value)

    def _get(self, key, current_node):

        # Base case 1, if the current node is empty, return none
        if not current_node:
            return None

        # Base case 2, if the current node matches the key, return it
        if current_node.key == key:
            return current_node

        # Progression to base case, but calling the function on the next child
        if key < current_node.key:
            return self._get(key, current_node.left_child)
        else:
            return self._get(key, current_node.right_child)

    def get(self, key):
        # If the tree is not empty
        if self.root: 

            # find the result by calling the _get(key, current_node)
            # handy to have the _get helper function as we can use it with __getitem__
            result = self._get(key, self.root)

            # if that results is not None return the results value
            if result: 
                return result.value

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        return bool(self._put(key,self.root))

    def find_min(self):
        current = self
        # While a left child exists, keep reassigning until you've found the leftmost node in the tree
        while current.left_child:
            current = current.left_child
        return current
    
    def find_successor(self):
        # Default is no successor should the node not have a right child
        successor = None
        if self.right_child:
            # Go and find the minimum value on the right sub tree. Noting the min will be left most and have at most a single node
            successor = self.right_child.find_min()
        else:
            # For casees where the parent exists
            if self.parent:
                if self.is_left_child():
                    successor = self.parent
                else:
                    # We will need to fund the successor EXLCUDING the existing node. Remove it's reference from the parent
                    self.parent.right_child = None
                    # Run the code in the parent
                    successor = self.parent.find_successor()
                    # Then reassign the child 
                    self.parent.right_child = self
        return self

    def splice_out(self):
        """ Cuts the successor out of the binary tree - we always gurantee the sucessor has at most one child"""
        if self.is_leaf():
            # If it's a leaf, remove the parents reference to it. Will be either left or right
            if self.is_left_child():
                self.parent.left_child = None
            # Otherwise it must the right child of the parent
            else:
                self.parent.right_child = None
        
        # We only want splice working on nodes with a single child - we guarantee that the successor has at most one child
        elif self.has_a_child():
            
            # check for if it's a left child
            if self.left_child():
                # check whether the node itself if a leeft or right child
                if self.is_left_child():
                    self.parent.left_child = self.left_child
                else:
                    self.parent.right_child = self.left_child

                # Update the successors parent refernece
                self.left_child.parent = self.parent
            
            # else it must be the case the hte node is has a right child
            else:
                if self.is_left_child():
                    self.parent.left_child = self.right_child
                else:
                    self.parent.right_child = self.right_child

                # Update the successors parent refernece
                self.right_child.parent = self.parent

    

    def _delete(self, current_node):
        """ Helper fuction that deals with a tree with more than 1 node"""

        # Case where the node is a leaf, go back up to the parent and remove the reference
        if current_node.is_leaf():
            if current_node == current_node.parent.left_child:
                current_node.parent.left_child = None
            else:
                current_node.parent.right_child = None

        # In the case where the node has two children
        elif current_node.has_children():
            successor = current_node.find_successor()
            successor.splice_out()
            current_node.key = successor.key
            current_node.value = successor.value
        
        # Otherwise now there is only the case were there is only one child
        # We must connect the parent of the node to delete to the child of hte node to delete
        # However we must be assign it to either the left or right child reference of the parent node
        else:
            # If the left child exists for the node to be deleted
            if current_node.get_left_child():

                # If the node to be deleted is it self a left child
                if current_node.is_left_child():
                    
                    # Reference the current nodes child and current node parents together
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.left_child
                
                # If the node to be deleted is it self a righr child, 
                elif current_node.is_right_child():

                    # Reference the deleted nodes child and parents together
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.left_child

                # Otherwise we are dealing wih to root node
                else:
                    current_node.replace_value(
                        current_node.left_child.key,
                        current_node.left_child.value,
                        current_node.left_child.left_child,
                        current_node.left_child.right_child,
                    )

            # It must be the case the node to be deleted has a right child only
            else:
                    # If the node to be deleted is itself a left child
                    # check again to see whether the node to be deleted is a left/right child of it's parent
                    if current_node.is_left_child():
                        current_node.right_child.parent = current_node.parent
                        current_node.parent.left_child = current_node.right_child
                    
                    elif current_node.is_right_child():
                        current_node.right_child.parent = current_node.parent
                        current_node.parent.right_child = current_node.right_child


                    # Otherwise it's the root node, replace it with the child
                    else:
                        current_node.replace_value(
                            current_node.right_child.key,
                            current_node.right_child.value,
                            current_node.right_child.left_child,
                            current_node.right_child.right_child,
                        )

    def delete(self, key): 
        if self.size > 1:
            node_to_remove = self._get(key, self.root)
            # Use the helper _get function to find the node, should it exist
            if node_to_remove:
                # Let's abstract from the actual delete and through that all in a helper function for the time being 
                self._delete(node_to_remove)
                self.size = self.size - 1

            else: 
                raise KeyError("Error, key not in tree")

        # Otherwise if there is only one item in the function, set key to none
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1

        # Otherwise key is not in the tree

        else: 
            raise KeyError("Error, key not in tree")

    def __delitem__(self, key):
        """ Dunder delete method """
        self.delete(key)

    def __iter__(self):
        # recurssive, __iter__ overrides "for x in" function
        # need to review "inorder function"
        # remember you are currently sitting on the "self" node which potentially has a left and right child
        if self:
            if self.left_child:
                # you are calling __iter__ on the self.left_child.... all the way until the base case NONE!
                for elem in self.left_child:
                    # After hitting the base case you can finally return the child. at first it will be the left most child
                    yield elem
            # return the centre node i.e. self i.e. the root
            yield self.key
            # progress down the right tree
            if self.right_child:
                for elem in self.right_child:
                    yield elem
    

class AVLTree(BinarySearchTree):
    def _put(self, key, value, current_node):
        if key < current_node.key:
            if current_node.left_child:
                self._put(self, key, value, current_node.left_child)
            else:
                current_node.left_child = AVLTreeNode(key, value, 0, parent=current_node)
                # After finding a place to put the child node, need to update the load balance recursively.
                self.update_balance(current_node.left_child)

        else:
            if current_node.right_child:
                self._put(self, key, value, current_node.right_child)
            else:
                current_node.right_child = AVLTreeNode(key, value, 0, parent=current_node)
                self.update_balance(current_node.right_child)
    
    def update_balance(self, node):
        """ Recussive procedure """
        # BASE 1: root node
        # BASE 2: balance factor of parent --> 0
        # Is the node unbalanced
        if node.balance_factor > 1 or node.balance_factor < 1:
            # rebalance the node and escape
            self.rebalance(node)
            # need to return something to to previous stack frame
            return 
        
        # elsif node has a parent
        if node.parent:

            # plus or minus the parent's balance factor depending on left/right child
            if node.is_left_child:
                node.parent.balance_factor += 1
            else:
                node.parent.balance_factor -= 1

            # should parent's balance factor != 0, update the balance
            # note how this progresses towards the root node i.e. base case
            if node.parent.balance_factor != 0:
                self.update_balance(node.parent)