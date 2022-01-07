class EulerTour:
    """Abstract base class for performing Euler tour of a tree
    
    _hook_previst and _hook_postvisit may be overriden by subclass
    """

    def __init__(self, tree):
        """Prepare an Euler tour template for a given tree"""
        self._tree = tree

    def tree(self):
        """Return reference to the tree being traversed."""
        return self._tree

    def execute(self):
        """Perform the tour and return any result from post vist of root"""
        if len(self._tree) > 0:
            return self._tour(self._tree.root(), 0, [])

    def _tour(self, p, d, path):
        """Perform tour of subtree rooted at Position p.
        
        P       Position of current node being visited
        d       depth of p in the tree
        path    list of indicies of children on path from root to p
        """
        self._hook_previsit(p, d, path)  # We also maintain the recursive depth of a tree, based on our experience in the other tree traversal applications
        results = []        
        path.append(0)      # Add new index to end of path before recursion. Similar to the labelling we want to maintain the recursive path through a tree

        for c in self._tree.children(p):
            results.append(self._tour(c, d+1, path)) 
            path[-1] += 1

        path.pop()

        answer = self._hook_postvist(p, d, path, results) # Notice how we are returning the post visit results

        return answer


    def _hook_previsit(self, p, d, path):
        # Function is called immediately before p's subtrees are traversed
        pass

    def _hook_postvist(self, p, d, path, results):
        # Function is called after all subtrees have been traversed
        pass




# --- Euler Tour Framework Reimplementations

class PreorderPrintIndentedTour(EulerTour):
    def _hook_previsit(self, p, d, path):
        print(2*d*' ' + str(p.element))

from Tree import Tree

T = Tree()

tour = PreorderPrintIndentedTour(T) # where T is a given T
tour.execute()

class PerorderPrintIndentedLabeledTour(EulerTour):
    def _hook_previsit(self, p, d, path):
        label = '.'.join(str(j+1) for j in path)
        print(2*d*' ' + label, p.element())


class ParenthesizeTour(EulerTour):
    # notice that use the public tree() method to access the tree
    def _hook_previsit(self, p, d, path):
        if path and path[-1] > 0: # If path exists and the last index in the path is > 0, 'p' must be following a sibling
            print(', ', end='') # So we can print a ', '
        
        # then print the element that we are recurring for
        print(p.element(), end = '')

        if not self.tree().is_leaf(p): # Then open up the parenthesis for any children this node may have
            print(' (', end = '')


    def _hook_postvist(self, p, d, path, results):
        if not self.tree().is_leaf(p): # close the parenthesis up if this node that we are recurring on had children
            print(')', end='')

class DiskSpaceTour(EulerTour):
    def _hook_postvist(self, p, d, path, results):
        return p.element().space + sum(results) # each recursion call on the child will append the results into a reulsts table.




