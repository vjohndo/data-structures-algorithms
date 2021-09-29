"""
Implementing an ordered list
"""

class Node: 
    def __init__(self,node_data):
        self._data = node_data
        self._next = None

    # define properties for data
    def get_data(self):
        return self._data

    def set_data(self,node_data):
        self._data = node_data
    
    data = property(get_data,set_data)

    # define properties for next pointer
    def get_next(self):
        return self._next
    
    def set_next(self, node_next):
        self._next = node_next
    
    next = property(get_next, set_next)

    # define string
    def __str__(self):
        return str(self.data)

class OrderedList:

    # The linked list is effecitvely just a pointer the head
    def __init__(self):
        self.head = None

    # Whether a node is empty of not depends on the head points to anything
    def is_empty(self):
        return not bool(self.head)
    
    # To get size, traverse until there current node is None and return the count
    def size(self):
        count = 0
        current_node = self.head

        while current_node is not None:
            current_node = current_node.next
            count += 1
        
        return count
    
    def remove(self,item):
        current_node = self.head
        previous_node = None

        # Traverse till the end of list until the current node is empty
        while current_node is not None:
            if current_node.data == item:
                break
            previous_node = current_node
            current_node = current_node.next

        # Case if at end of the list
        if current_node is None:
            raise ValueError('{} not in list.'.format(item))
        # Now the current node must have value and previous node is None
        elif previous_node is None: 
            self.head = current_node.next
        # Otherwise you're somewhere in the middle of the list and okay to remove node
        else:
            previous_node.next = current_node.next
    
    # This will work the same as a linked list but at a certain point we can know item is not in list
    # Search returns whether the item is in the list
    def search(self,item):
        current_node = self.head

        while current_node is not None:
            if current_node.data == item:
                return True
            elif current_node.data > item:
                return False

            current_node = current_node.next
            
        return False

    # Will need to go to the right spot to add node
    # It will be the case when current node it none or value greater than existing
    def add(self,item):
        current_node = self.head
        previous_node = None
        new_node = Node(item)

        # Stop traversing if current node is none or we've found a smaller element.
        while current_node is not None and current_node.data < item:
            previous_node = current_node
            current_node = current_node.next
        
        # We will either be at the start on empty, at end with current_node.data < item, or in the middle somewhere:
        # we will always be placing our node before the "current node"
        if previous_node is None:
            # Must be the case that we need to our node before the first node
            new_node.next = self.head
            self.head = new_node
        
        else:
            # Must be somewhere in the middle in which case point the new node to current
            # Otherwise must be at the end of the list... also works with below code to point to nothing.
            new_node.next = current_node
            previous_node.next = new_node

def main():
    my_list = OrderedList()
    my_list.add(31)
    my_list.add(77)
    my_list.add(17)
    my_list.add(93)
    my_list.add(26)
    my_list.add(54)

    print(my_list.size())
    print(my_list.search(93))
    print(my_list.search(100))

main()
