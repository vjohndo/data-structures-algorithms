class TicTacToe:
    """Management of a Tic-Tac-Toe game"""

    def __init__(self):
        """Start a new game"""

        # This is best practice to construct a multi-dim array
        self._board = [[' ']*3 for i in range(3)]

        self._player = 'X'


    def mark(self, i, j):
        """Put an X or O mark at position (i,j) for next player's turn"""

        #If the input values aren't within the bounds of the gamespace, exit
        if not (0 <= i <= 2 and 0 <= j <= 2):
            raise ValueError('Invalid Board Position')
        
        #If the position is already taken
        if self._board[i][j] != ' ':
            raise ValueError('Board position occupied')

        # If the game is complete
        if self.winner() is not None:
            raise ValueError('Game is already complete')

        # If we've passed through all those checks, should be good to add in
        self._board[i][j] = self._player

        # Now swap the player  positions
        if self._player == 'X':
            self._player = 'O'
        
        else:
            self._player = 'X'

    def _is_win(self, mark):
        """Check whether the board configuration is a win for the given player"""

        board = self._board

        # Check if for the given mark there is a win condition
        return (mark == board[0][0] == board[0][1] == board[0][2] or 
                mark == board[1][0] == board[1][1] == board[1][2] or 
                mark == board[2][0] == board[2][1] == board[2][2] or 
                mark == board[0][0] == board[1][0] == board[2][0] or 
                mark == board[0][1] == board[1][1] == board[2][1] or 
                mark == board[0][2] == board[1][2] == board[2][2] or 
                mark == board[0][0] == board[1][1] == board[2][2] or 
                mark == board[0][2] == board[1][1] == board[2][0])


    def winner(self):
        """Return mark of winning player, or Nont to indicate a tie"""
        for mark in 'XO':
            if self._is_win(mark):
                return mark
        return None


    def __str__(self):
        """Return string repsentation of current game board."""
        # Goes through each row of board and prints it out.
        rows = ['|'.join(self._board[r]) for r in range(3)]
        return '\n-----\n'.join(rows)
