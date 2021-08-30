"""
Lessons learnt:

- property() -->  defines properties so you can automatically invoke get, set, del methods when calling the property. 
- much like we have "=" and "is", we may have something like "!=" and "is not"
- "=" "!=" is an equality test while "is" and "is not" is an identity check... ARE THEY THE SAME OBJECT

-  # express the value error as the veriable ve and print it...
    except ValueError as ve:
        print(ve)

Need to make a linked list:

To make a linked list we build a node:
    > comprises of datafield
    > comprises of reference



"""
from os import curdir


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
        self.tail = None

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
        ### From the future, let's add in a tail... will break on POP. and REMOVE. 
        if temp.next is None:
            self.tail = temp
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

    # need to udpate to work with tail
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

    """ 
    append, insert, index, pop. 

    All need to account for a change in the 
    """
    def append(self,item):
        temp = Node(item)
        current = self.tail
        current.next = temp
        self.tail = temp
        
        # current = self.head
        # temp = Node(item)
        # # if it so happens that linked list is empty, the head will point to none
        # # otherwise traverse to the end of the linked list until we're pointing to none
        # while current.next is not None:
        #     current = current.next
        
        # current.next = temp

    # need to udpate to work with tail
    def insert(self,index,item):
        current_node = self.head
        previous_node = None
        new_node = Node(item)
        count = 0

        # Keep traversing until the count == index or we've reached a pointer that points to None (start / end)
        while current_node is not None:
            # Note that we don't include count == index in the while loop conditions as we need to keep the state of previous and current
            # I.e. don't want to complete the inchworming upon landing on the correct index
            if count == index:
                break
            previous_node = current_node
            current_node = current_node.next
            count += 1
        
        # The above while loop breaks upon reaching the index, or being at a none node... let's account for these scenarios
        if previous_node is None:
            # That means the head is pointing that the item to swap in place
            # do a hot swap.
            new_node.next = current_node
            self.head = new_node
        elif current_node is None:
            # That means we've traversed to the send of the list and the index is not here
            # Following how lists work we will add it now
            previous_node.next = new_node
        else:
            # Should be all good to make a swap
            new_node.next = current_node
            previous_node.next = new_node

    def index(self,index_expression):
        current_node = self.head
        count = 0

        while current_node is not None:
            if current_node.data == index_expression:
                return count
            count += 1
            current_node = current_node.next

        raise ValueError('{} not in index'.format(index_expression))

    # need to udpate to work with tail
    def pop(self,index = None):
        
        current_node = self.head
        previous_node = None

        if index is None:
            while current_node.next is not None:
                previous_node = current_node
                current_node = current_node.next

            if current_node is None and previous_node is None:
                raise IndexError(' pop from empty list')
            elif previous_node is None:
                # case if you're at the head
                self.head = current_node.next
            else:
                previous_node.next = None

            
        else:
            count = 0
            while current_node is not None:
                if count == index:
                    break
                previous_node = current_node
                current_node = current_node.next

            if previous_node is None and current_node is None:
                raise IndexError('pop from empty list')
            elif previous_node is None:
                # That means you gotta reassing the head
                self.head = current_node.next
            elif current_node is None:
                raise IndexError('{} not an index in list'.format(index))
            else:
                previous_node.next = current_node.next



    def checkList(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
        

def check():
    my_list = UnorderedList()

    my_list.add(31)
    my_list.append(32)
    my_list.checkList()
    # try:
    #     print('index',my_list.index('BANG'))

    # # express the value error as the veriable ve and print it
    # except ValueError as ve:
    #     print(ve)

check()

    

def main():
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
# main()