from pythonds3.graphs import Graph

class DFSGraph(Graph): 
    def __init__(self):
        super().__init__()
        # Another instance variable that tracks the 
        self.time = 0

    def dfs(self):
        # Go through each vertex in the Graph
        for aVertex in self:

            # Set the color to white and set the predecessor as -1
            # Note that we've added additional instance variables to the vertex for discovery time and finish time
            aVertex.setColor('white')
            aVertex.setPred(-1)
        
        for aVertex in self:

            # Now go through each vertex and do dfsvisit 
            # Unlike previous implementation we want to iterate through each vertex rather than exploring form a start
            # Do not want to run into dead ends, ensure all nodes have been searched 
            if aVertex.getColor() == 'white':
                self.dfsvisit(aVertex)
    
    def dfsvisit(self,startVertex):
        # Set the vertex to gray i.e. it has been explored
        startVertex.setColor('gray')
        
        # Increase the time by one for that vertex
        self.time += 1
        
        # Set the discovery time for the vertext as the current time of the graph
        startVertex.setDiscovery(self.time)
        
        # Go through all the connections of the passed in vertex
        for nextVertx in startVertex.getConnections():

            # If that vertex is white, I.e. it is unexplored
            if nextVertx.getColor() == 'white':

                # update the predecessor as the starting vertex
                nextVertx.setPred(startVertex)

                # Recursivelly call dfsVisit on the nextVertex
                # note that the base case would be the next vertex has already been explored OR that there is no next vertex
                self.dfsvisit(nextVertx)

        # After exploring all the connections, set to black to black
        startVertex.setColor('black')

        # Increase the time by 1, it was an extra step of exploration to set the vertexx to black i.e. deem it fully explored
        self.time += 1

        # Now that the Vertex has been fully explored and colored black, set it 
        startVertex.setFinish(self.time)




