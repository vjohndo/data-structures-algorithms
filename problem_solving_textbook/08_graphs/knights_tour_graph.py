from pythonds3.graphs import Graph, Vertex

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

def knightTour(n, path, u, limit):
    """
    n --> depth of the current tree,
    path --> list of all previously visited nodes,
    u --> vertex we want to explore,
    limit --> the number of nodes in the path
    """

    # set the color of the node we are visiting to grey
    u.setColor('gray')

    # Add this node to the path path as we've now visited it
    path.append(u)

    # it we haven't hit the limit of nodes in our path
    # we will keep recursively 
    # ELSE we will escape this until our path has exhaused all routes
    if n < limit:

        # Get a list of neightbours connections as (key, reference node)
        # nbrList = list(u.getConnections())
        
        ## This would just go in order of neighbours
        ## We can implement a heuristic
        nbrList = orderByAvail(u)
        

        # initalise some variables for our while loop
        """ i --> index, done --> whether it's done"""
        i = 0 
        done = False

        while i < len(nbrList) and not done:
            
            # if the node hasn't been explored i.e. color is white
            if nbrList[i].getColor() == 'white':

                # determine the "doneness by exploring the next level for each vertex
                # notice how it stack frames would keep digging down the depths
                done = knightTour(n+1, path, nbrList[i], limit)

        # So after we've explored the depth and we've reached the last node and done is still false?
        # time to backtrack
        if not done:
            # pop the vertex
            path.pop()

            # "unexplore that node", we leave it avaialble to be explored again along another potential path
            u.setColor('white')

    else: 
        done = True
    
    return done

def orderByAvail(n):

    # Contrains a results lists
    resList = []

    # For the vertex in question, go through of it's connections
    for v in n.getConnection():

        # if it has not been visted
        if v.getColor() == 'white':

            # initialise the number of connections that vertex has (starts 0)
            c = 0

            # Go through each of the connected vertices
            for w in v.getConnections():

                # If the color is white i.e. it can still be explored
                if v.getColor() == 'white':

                    # Increase the "legal" connections counter
                    c = c + 1

            # Add it to the list 
            resList.append((c,v))

    # sort it based on x & x[0]
    resList.sort(key=lambda x: x[0])

    # return a list of vertices, by pulling out the vertex i.e. (c,v)[1]
    return [y[1] for y in resList]                