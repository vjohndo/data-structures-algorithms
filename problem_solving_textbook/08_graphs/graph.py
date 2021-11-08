class Vertex:
    """ A vertex object has a key and has references to nodes it is connected to """
    def __init__(self, key):
        self.id = key
        # This dictionary keeps track of vertices to which it is connected and weight of each edge
        # {v1: 4, v2: 8 etc..}
        # the id of the neighbour is the key and the weight of the path is the value.
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight = 0):
        # assign a new key-value pair in the connected to dictionary
        self.connectedTo[nbr] = weight
    
    def __str__(self):
        # dunder str shows the id + str for every id in connection
        return str(self.id) + ' connectedTo:' + str([x.id for x in self.connectedTo])
    
    def getConnections(self):
        # recall that name of the neighbours are the keys of the connectedTo dictionary
        return self.connectedTo.keys()

    def getId(self):
        return self.id
    
    def getWeight(self, nbr):
        # Given a neighbour returns the weight of the connection
        return self.connectedTo[nbr]


class Graph:
    ''' A graph contains a collection of vertices. We've defined each Vertex such that trakcs it's own edges to neighbours.'''
    def __init__(self):
        # A list containing all the vertices
        self.vertList = {}
        # the number of vertices in the graph 
        self.numVertices = 0

    def addVertex(self, key):
        # In crease the number of vertices in the graph
        self.numVertices += 1
        # Create a new vertex instance using the key
        # All a vertex is an id (info payload) + and a the connections to other nodes 
        newVertex = Vertex(key)
        # Create a new key value pair in the vertList index
        self.vertList[key] = newVertex

    def getVertex(self, n):
        # check if the item exists in the graph
        if n in self.vertList:
            # if so return it
            return self.vertList[n]
        else:
            # otherwise return none
            return None

    def __contains__(self, n):
        # to make the built in operation "n in GRAPH" work.
        return n in self.vertList
    
    def addEdge(self,f,t,weight=0):
        # To add a edge, we will input a "from vertex" a "to vertex" and a weight
        
        # if "from" is not in self.vertlist add it
        if f not in self.vertList: 
            nv = self.addVertex(f)

        # if "to" is in self.vertlis add it
        if t not in self.vertList:
            nv = self.addVertex(t)

        # now from the "from" vertex, add neighbour ... i.e. connect the vertex by passing in the "to" vertex and the weight
        self.vertList[f].addNeighbor(self.vertList[t], weight)
    
    def getVertices(self):
        # return all the keys... this returns a dictionary keys object
        return self.vertList.keys()
    
    def __iter__(self):
        # returns an iterable obeject comprised of the values in teh vertlist
        return iter(self.vertList.values())

# Initialise a graph
g = Graph()

# Add in values
for i in range(6):
    g.addVertex(i)
g.vertList

# Add in all the edges
g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
g.addEdge(5,2,1)

# for each item in graph 'g' (which iterates through the vertList.values)
for v in g:
    # for each vertex in the graph... go through all the connections for that vertex. 
    for w in v.getConnections():
        #  print the vertex id, and all of it's connected vertices
        print("( %s , %s )" % (v.getId(), w.getId()))