class BinaryHeap:
    def __init__(self):
        self._heap = []

    def _perc_up(self, cur_idx):
        """ Keeps comparing child and parent nodes until top of the list. Will exchange nodes that are out of place based on heap order property """
        # Heap order property -> for every node x with a parent, the parent's key MUST be <= x's key

        # Keep perculating until towards the 0th node... until you get to the 0th node
        while (cur_idx - 1) // 2 >= 0:

            # Complete tree property, parent node is (n -1)//2
            parent_idx = (cur_idx - 1) // 2

            # the current index < parent node 
            if self._heap[cur_idx] < self._heap[parent_idx]:

                # Do an exchange of the nodes
                self._heap[cur_idx], self._heap[parent_idx] = (
                    self._heap[parent_idx],
                    self._heap[cur_idx]
                )

            # set the current index and the parent's index, and this will continue assuming the while loop remains true
            cur_idx = parent_idx

    def insert(self, item):
        """ Insert item at the end of the tree """
        # Add the item to the back of the heap
        # remember we represent the heap as a tree but implement it as an array
        self._heap.append(item)

        # Go to the last index of the array and perculate up
        self._perc_up(len(self._heap)-1)

    def _get_min_child(self, parent_idx):
        """ _perc_down helper function... want to grab the lower value child of the parent"""
        # If the right child index is greater the the last item in the heap (i.e. accounting for the case the right child does not exist.. you can't return none)
        if 2 * parent_idx + 2 > len(self._heap) - 1:
            # Return the right child
            return 2 * parent_idx + 1

        # If the left child is less than the right child
        if self._heap[2 * parent_idx + 1] < self._heap[2*parent_idx + 2]:
            # Return the left child
            return 2 * parent_idx + 1
        
        # Otherwise return the right child (at this point the left child is bigger )
        return 2 * parent_idx + 2

    def _perc_down(self, cur_idx):
        """ delete helper function, percs down item to achieve heap order """
        # recall that in a complete binary tree, the left child is 2p + 1 , right is 2p + 2

        # So long as we are not at a final node remember that the way complete tree order works, 2p + 1 guarantees the next tyree
        while 2*cur_idx + 1 < len(self._heap):

            # The above while loop ensures we haven't progressed to a child node
            # We can always begin by grabbing the minimum child 
            min_child_idx = self._get_min_child(cur_idx)

            # Let's compare the current index with the minimum child
            if self._heap[cur_idx] > self._heap[min_child_idx]:
                self._heap[cur_idx], self._heap[min_child_idx] = self._heap[min_child_idx], self._heap[cur_idx]

            
            else:
                # break the while loop?
                return
            
            # update the current index for the next iteration of the while loop
            cur_idx = min_child_idx


    def delete(self, item):
        """ Removes the smallest item in the list """
        # Grab the root and replace it with the last item in the heap (maintains tree completeness)
        # Now need to push down that "last" item to a proper position to achieve heap order i.e. perc down
        # also want to perc down in a way that maintains tree completeness
    
        # To achieve the first two parts let's swap the first and last index then pop
        self._heap[0], self._heap[-1] = self._heap[-1], self._heap[0]
        result = self._heap.pop()
        self._perc_down(0)
        return result


