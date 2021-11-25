class GameEntry:
    """Represents one entry from a list of high scores"""

    def __init__(self, name, score):
        self._name = name
        self._score = score

    def get_name(self):
        return self._name

    def get_score(self):
        return self._score
    
    def __str__(self):
        return '({0},{1})'.format(self._name, self._score) # return a score e.g. (John, 99)

class ScoreBoard:
    """Fixed-length sequence of high score in nondecreasing order"""

    def __init__(self, capacity = 10):
        """initalise scoreboard with a capacity of 10 by default. All entries start at none"""
        self._board = [None] * capacity # We initialise the board to prevent the need for resizing
        self._n = 0 # number of actual entries in the board

    def __getitem__(self, k):
        """Return entry at index k"""
        return self._board[k]

    def __str__(self):
        """Return string representation of the high score list"""
        # On each new line, print the string representation of the "GameEntry" instance, ranging from 0 to the J'th index.
        return '\n'.join(str(self._board[j] for j in range(self._n)))

    def add(self, entry):
        """Consider adding entry to high score"""

        # Get the score of the entry to be added in
        score = entry.get_score()

        # Check this score to see if there's still capacity 
        # Check this score against the last entry in the score board 
        good = self._n < len(self._board) or score > self._board[-1].get_score()

        if good: 
            if self._n < len(self._board): 
                self._n += 1 # We will definitely be increasing n, could potentially 

            j = self._n - 1 # Let's initialise an insertion point j

            # Now we can loop through list, until we find a preceeding score greater than the score 
            # Remeber that at this stage we know the score will at least be greater than the n'th number
            # That means we have shift numbers right
            while j > 0 and self._board[j-1].get_score() < score:
                
                # Reassign the index right 
                self._board[j] = self._board[j-1]
                
                # Increment down
                j -= 1

            # Once we've broken out of the loop, the index j will be for an empty cell.
            self._board[j] = entry  

        

        


