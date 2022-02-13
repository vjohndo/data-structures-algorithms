from turtle import st


class Range:
    """A class that mimic's the built-in range class."""

    def __init__(self, start, stop=None, step=1):
        """Initialize a Range instance.
        
        Semantics is similar to built-in range class.
        """

        if step == 0:
            raise ValueError('step cannot be zero')

        if stop is None: # special case of range(n), will convert it to range(0, n)
            start, stop = 0, start

        # Calculate the effective length once
        # stop - start // step. Could have case stop = 1, start = 0, step = 2, then stop - start // step = 0
        # (step - 1) // step is always < 1. It is added to count for case when start - stop < step
        self._length = max(0, (stop - start + step - 1) // step)

        # need knowledge of start and step (but not stop) to support __getitem__
        self._start = start
        self._step = step

    def __len__(self):
        """Return number of entries in the range."""
        return self._length

    def __getitem__(self, k):
        """Return entry at index k (using standard interpretation if negative)."""
        if k < 0:
            k += len(self)

        if not 0 <= k < self.length:
            raise IndexError('index out of range')

        return self._start + k * self._step    