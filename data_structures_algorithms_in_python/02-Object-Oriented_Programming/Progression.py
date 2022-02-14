class Progression:
    """Iterator producing a generic progression.
    
    Default iterator produces whole numbers 0, 1, 2
    """

    def __init__(self, start=0):
        """Initialise current to the first value of the progression."""

        self._current = start
    
    def _advance(self):
        """Update self._current to a new value.
        
        This should be overriden by a subclass to customise progression.

        By convention, if current is set to None, this designates the end of a finite progression
        """
        self._current += 1

    def __next__(self):
        """Return the next element, or else raise StopIteration error."""
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        """By convention, an iterator must return itself as an iterator"""
        return self
    
    def print_progression(self, n):
        """Print next n values of the progression."""
        print(' '.join(str(next(self)) for j in range(n)))

class ArithmeticProgression(Progression):
    """Iterator producing an arithmetetic progression
    
    increment   the fixed constant to add to each term (default 1)
    start       the first term of the prgression (default 0)
    """
    def __init__(self, increment=1, start=0):
        super().__init__(start)
        self._increment = increment

    def _advance(self):
        """Update current value by adding the dixed increment"""
        self._current += self._increment

class GeometricProgression(Progression):
    """Create a new geometric progression.
    
    base    the fixed constant multiplied to each term (default 2)
    start   the first term of the progression (default 1)
    """
    def __init__(self, base=2, start=1):
        super().__init__(start)
        self._base = base

    def _advance(self):
        """Update current value by multiplying it by the base value."""
        self._current *= self._base

class FibonacciProgression(Progression):
    """Iterator producing a generalised Fibonacci progression"""
    def __init__(self, first=0, second=1):
        """Create a new fibonacci progression
        
        first   the first term of the progression (default 0)
        second  the second term of the progression (default 1)
        """
        super().__init__(first)
        self._prev = second - 1 #value preceding first
    
    def _advance(self):
        """Update current value by taking sum of previous two."""
        self._current = self._current + self._prev
        self._prev, self._current = self._current, self._current + self._prev

# Basic testing    
if __name__ == "__main__":
    a = Progression()
    a.print_progression(50)
