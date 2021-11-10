from pythonds3.graphs import Graph

def knightGraph(bdSize):
    # Create an instance of the class
    ktGraph = Graph()

    # Go through each row and each column
    for row in range(bdSize):
        for col in range(bdSize):

            # Set the nodeId based on the row and col of the given node
            nodeId = posToNodeId(row, col, bdSize)
            newPositions = generateLegalMoves(row, col, bdSize)


def posToNodeId(row, column, board_size):
    # Multiply the row by the board size and add the column to get an ordered linear number
    return (row * board_size) + column

def generateLegalMoves(x,y,bdSize):
    # initliase list containing possible new moves
    newMoves = []
    
    # Let's look at all possible offsets, permutation of 1 and 2
    moveOffsets = [(-1,-2), (1,2), (-1,2), (1,-2), (2,1), (-2,-1), (2,-1), (-2,1)]

    # Go through each of the possible move sets
    for i in moveOffsets: 

        # Assign what the new X,Y coordinates would be
        newX = x + i[0]
        newY = y + i[1]

        # If that is a legal move, add it to the new moves list 
        if legalCoord(newX, bdSize) and legalCoord(newY, bdSize):
            newMoves.append((newX, newY))
    
    return newMoves

def legalCoord(x,bdSize):
    if x >= 0 and x <= bdSize:
        return True
    else:
        return False

