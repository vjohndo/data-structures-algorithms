from linkedBinaryTree import LinkedBinaryTree

class ExpressionTree(LinkedBinaryTree):
    """An arithmetic expression tree"""

    def __init__(self, token, left=None, right=None):
        """Create an expression tree.
        
        In a single parameter form, token should be a leaf value (e.g. '42')
        and the expression tree will have that value at an isolated node
        

        In a three-parameter version, token should be an operator,
        and left and right should be existing Expression Tree instances
        that become the operands for the binary operator 
        """

        super().__init__() # LinkedBinaryTree should be initialised
        if not isinstance(token, str):
            raise TypeError('Token must be a string')

        self._add_root(token) # Method from the LinkedBinaryTree superclass

        if left is not None: # If left is not none, we must be in the in three-parameter form
            if token not in '=-*x/': # Check that the token is an operator
                raise ValueError('token must be valid operator')
            self._attach(self.root(), left, right) # use inherited nonpublic method

    
    def __str__(self):
        """Return string representation of the expression"""
        pieces = [] # sequence of piecewise strings to compose, remmeber it's more effiient to use .join rather concatenating strings
        self._parenthesize_recur(self.root(), pieces)
        return ''.join(pieces)


    def _parenthesize_recur(self, p, result):
        """Append piecewise representation of p's subtree to resulting list"""
        if self.is_leaf(p): # Base case
            result.append(str(p.element())) # leaf value gets outputted

        else: # Otherwise we are dealing with the three-parameter form
            result.append('(') # Opening parenthesis
            self._parenthesize_recur(self.left(p), result) # left subtree
            result.append(p.element()) # Operator
            self._parenthesize_recur(self.right(p), result) # right subtree
            result.append(')')


    def evaluate(self):
        """Return the numeric result of the expression"""
        return self._evaluate_recur(self.root())

    def _evaluate_recur(self, p):
        """Return the numeric result of subtree rooted at p."""
        if self.is_leaf(p):
            return float(p.element())

        else:
            op = p.element()
            left_val = self._evaluate_recur(self.left(p))
            right_val = self._evaluate_recur(self.right(p))
            if op == '+':
                return left_val + right_val
            elif op == '-':
                return left_val - right_val
            elif op == '/':
                return left_val / right_val
            else:
                return left_val * right_val # we treat 'x' or '*' as multiplication
    

def build_expression_tree(tokens):
    """Returns an ExpressionTree based upon a tokenized expression"""
    S = [] # We will use a python list is a stack
    for t in tokens:
        if t in '+-x*/':
            S.append(t) # Push operator into stacks
        elif t not in '()':
            S.append(ExpressionTree(t)) # Push trivial tree storing value
        elif t  == ')':
            # Now compose a new tree from three constituent parts
            right = S.pop()
            op = S.pop()
            left = S.pop()
            S.append(ExpressionTree(op, left, right))

        # Rememeber that we ignore a left parenthesis

    return S.pop()