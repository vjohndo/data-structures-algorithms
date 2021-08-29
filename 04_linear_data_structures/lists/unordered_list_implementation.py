"""
Lessons learnt:

- property() -->  defines properties so you can automatically invoke get, set, del methods when calling the property. 
- much like we have "=" and "is", we may have something like "!=" and "is not"
- "=" "!=" is an equality test while "is" and "is not" is an identity check... ARE THEY THE SAME OBJECT

Need to make a linked list:

To make a linked list we build a node:
    > comprises of datafield
    > comprises of reference



"""
class Node: 
    def __init__(self, node_data):
        self._data = node_data
        self._next = None
    
    def get_data(self):
        return self._data

    def set_data(self, node_data):
        self._data = node_data

    # the property(fget, fset, fdel, doc) method helps define properties for python classes.. automatically invotes functions as you call the property
    data = property(get_data,set_data)

    def get_next(self):
        return self._next
    
    def set_next(self, node_next):
        self._next = node_next
    
    # will automatically invoke get_next if you call object.next, automatical invokes set_next if you assign object.next = next_node
    next = property(get_next, set_next)

    def __str__(self):
        """ String """
        return str(self._data)


"""
Now that we have a node class, we can build our list class
    > As long as we know where our first node is we can traverse the links to find the other nodes
    > That is why the UnorderedList class must walways maintain a refernece to the head i.e. first node
    > The class itself does not contain any reference to the next node 
"""

class UnorderedList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        # if the head doesn't point to anything, it must be empty
        # this is also why using None is very helpful... initialising the list __init__ will still be consitent if the list is empty
        return self.head == None
    
    def add(self,item):
        # we want to be able to add items
        # but if we have to traverse all the links to add something, that can be quite annoying
        # how about we add it to the existing pointer of the head, and then update the head to point at this node
        # first item added will be the last item in a linked list 
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

        # if you reverse the order, i.e. assign the head first, reference to the rest of the nodes will be lost forever.

    """
    Size, search, remove --> all use linked list traversal i.e. visiting each nde 
    """

    def size(self):
        # Will need to keep count of nodes that occured 
        current = self.head
        count = 0
        # We will eventually be linked to a None or potentially there is None already
        # not that we can use "is not" as we are checking are they referring the the SAME obejct, instead of and equal object
        while current is not None:
            count = count + 1
            current = current.next # going to the next node

        return count

    def search(self, item):
        current = self.head
        # We need to ask each node if the data is equal to item we are after
        while current is not None:
            if current.data == item:
                return True
            # then move the next node
            current = current.next
        
        # However if we get the end of the list "None" that means the item isn't there
        return False

    def remove(self, item):
        current = self.head
        # we can't go backwards in a linked list so we'll bring a reference to the previous node with us
        previous = None

        while current is not None:
            if current.data == item:
                # if we find a match, stop traversing. we have everything needed in current and previous to remove now
                break
            # Inch warming, previous moves up to current, then the current moves to the next 
            previous = current
            current = current.next
        
        # This will only be the case if we've broken or reached the end of the linked list
        if current is None:
            # clause for if we've reached the end of the list
            raise ValueError("{} is not in the list".format(item))
        if previous is None: 
            # clause for if previous is None i.e. it's the first item in the list
            self.head = current.next
        else:
            # clause for any other intermediate items
            # say if we are removing the last item, it would work as current.next is pointint to None.
            previous.next = current.next

my_list = UnorderedList()

my_list.add(31)
my_list.add(77)
my_list.add(17)
my_list.add(93)
my_list.add(26)
my_list.add(54)

print(my_list.size())
print(my_list.search(93))
print(my_list.search(100))

my_list.add(100)
print(my_list.search(100))
print(my_list.size())

my_list.remove(54)
print(my_list.size())
my_list.remove(93)
print(my_list.size())
my_list.remove(31)
print(my_list.size())
print(my_list.search(93))

try:
    my_list.remove(27)
except ValueError as ve:
    print(ve)






