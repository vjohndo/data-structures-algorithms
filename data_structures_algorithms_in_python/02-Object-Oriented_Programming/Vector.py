class Vector:
    """Represent a vector in multidimensional space."""

    def __init__(self, d):
        """Create d-dimensional vectors of zeroes."""
        self._coords = [0]*d

    def __len__(self):
        """Return the dimension ofthe vector."""
        return len(self._coords)

    def __getitem__(self, j):
        """Return the jth coordinate of vector."""
        return self._coords[j]

    def __setitem__(self, j, val):
        """Set jth coordinate of vector to given value."""
        self._coords[j] = val

    def __add__(self, other):
        """Return sum of two vectors."""
        if len(self) != len(other): # if the length of the vectors don't match, raise error
            raise ValueError('dimensions must agree')
        result = Vector(len(self)) # otherwise instantiate a vector and each position will be sum
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        """Return True if vector has same coordinates as other."""
        return self._coords == other._coords # testing for equivalence

    def __ne__(self, other):
        """Return True if vector differs from other"""
        return not self == other # rely on existing __eq__ defintion

    def __str__(self):
        """Produce string representation of a vector."""
        return '<' + str(self._coords)[1:-1] + '>' # adapt list representation. Note we slice the string [1:-1] to remove the '[' and ']'