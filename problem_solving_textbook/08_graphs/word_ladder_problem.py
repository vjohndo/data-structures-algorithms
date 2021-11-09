from pythonds3.graphs import Graph
from pythonds3.basic import Queue

def buildGraph(wordFile):

    d = {}

    # Create an instance of graph
    # a graph contains a list of vertices
    # A vertices has an id (data) and a dictionary containing connections to neighbours
    g = Graph()

    # Open the wordfile in read only mode - returns a file object
    wfile = open(wordFile,'r')

    # create buckets of words that differ by one letter
    # the wordFile imported contains e.g. nope.
    for line in wfile:
        
        # slice from start upto last character (probably a line break or something? which is why it's not including last chacter)
        word = line[:-1]

        # Iterate an "_" through each space in the work.
        for i in range(len(word)):
            # Create a bucket it does not already exist nope -> _ope, n_pe, no_e, nop_
            bucket = word[:i] + '_' + word[i+1:] 
            if bucket in d:
                d[bucket].append(word)
            else:
                # if the item does not exist as a unqie bucket make it.
                d[bucket] = [word]

    # At this point we'll have a buckets in the dictionary d
    # add vertices and edges for words in the same bucket
    
    # for each bucket in the dictionary
    for bucket in d.keys():

        # Go through each word in the bucket of the dictionary
        for word1 in d[bucket]:

            # And for that word, go through all the words again
            for word2 in d[bucket]:

                # If it's not the same connect word1 to word2
                # the reason why we do these nested loops is that the edges go in both directions e.g. consider a set of vertices A, B, C
                # The connections would look like this: A-->B, A-->C, B-->A, B-->C, C-->A, C-->B
                if word1 != word2:
                    g.addEdge(word1,word2)
    return g


def bfs(g, start):
    """ 
    Search function, takes in a graph and a starting vertex
    """

    # Set the distance and predecessor nodes to 0 and None respoective
    start.setDistance(0)
    start.setPred(None)

    # Initialise a verticies queue which will handle our actions
    # Then add the starting vertex to the queue
    vertQueue = Queue()
    vertQueue.enqueue(start)

    # We will now start processing the vert queue
    while (vertQueue.size() > 0):

        # Set the current vert as the next item on the queue
        currentVert = vertQueue.dequeue()

        # Iterate through the adjacency list of the vertex
        for nbr in currentVert.getConnections():
            
            # If the neighbour's color is white i.e. if we haven't visited the node yet
            if (nbr.getColor() == "white"):

                # Set the unvisted neighbours color to gray
                nbr.setColor('gray')

                # Set the distance from the starting node as the current verticies distance + 1
                nbr.setDistance(currentVert.getDistance() + 1)

                # Set the predecessor vertex to the "current node"
                # By setting this up we are no longer required to start from "starter node"
                nbr.setPred(currentVert)

                # Then add the item back in the queue 
                vertQueue.enqueue(nbr)

            # If the neighbour's color is not white, it must be grey for it to have been in the queue 
            # If it's grey it would have already been explored, therefore a short path exists to this node
            # We don't need to add in the explored node to the queue as there will already be an entry into the queue ready for expansion

            # After going through all the neighbours the current node will have been fully explored and we can set it to black
            currentVert.setColor('black')


def traverse(y):
    x = y 
    while (x.getPred()):
        print(x.getId())
        x = x.getPred()
    print(x.getId())

traverse(g.getVertext('sage'))


