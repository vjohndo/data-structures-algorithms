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
