


# --- Graph class
class Graph:
    """Representation of a simple graph using an adjacency map."""

        # --- nested Vertex class
    class Vertex: 
        """Lightweight vertext structure for a graph."""
        __slots__ = '_elements'

        def __init__(self, x):
            """Do not call constructor directly. Use Graph's insert_vertex(x)."""
            self._element = x
        
        def element(self):
            """Return element associated wtih this vertex."""
            return self._element
        
        def __hash__(self):
            return hash(id(self)) # hash the identity of an object.  # ID --> This is an integer that is unique for the given object and remains constant during its lifetime.

    # --- nested Edge class
    class Edge:
        """Lightweight edge structure for a graph"""
        __slots__ = '_origin', '_destination', '_element'

    def __init__(self, u, v, x):
        """Do not call constructor directly. Use Graph's insert_edge(u,v,x)."""
        self._origin = u
        self._destination = v
        self._element = x # note that this is the element of the edge

    def endpoints(self):
        """Return (u,v) tuple for vertices u and v"""
        return (self._origin, self._destination)

    def opposite(self, v):
        """Return the vertix that is opposte v on this edge"""
        return self._destination if v is self._origin else self._origin
    
    def element(self):
        """Return element associated with this edge"""
        return self._element

    def __hash__(self):
        return hash( (self._origin, self._destination) ) # hash the set. remember hash can take in immutables including set.

    def __init__(self, directed=False):
        """Create an empty graph (undirected, by default)
        
        Graph is directed if optional pareamter is set to True
        """
        self._outgoing = {}
        self._incoming = {} if directed else self._outgoing # Reference the same map

    ### Note that we represent maintain a list of vertices and edges via a top-level dictionary. 
    ### We extend this and use an additional dictionary so the we have a dedicated dictionary for outgoing and incoming (in the directed case)
    ### We can just set the second to reference the first dictionary if it's the undirected case

    def is_directed(self):
        """Return True if this is a directed graph; False if undirected
        
        Property is based on the original declaration of the graph, not its contents
        """
        return self._incoming is not self._outgoing # Check if outgoing and incoming are the same dictionary

    def vertex_count(self):
        """Return the number of vertices in the graph"""
        return len(self._outgoing)
    
    def vertices(self):
        """Return an iteration of all vertices of the graph"""
        return self._outgoing.keys()

    def edge_count(self, v):
        """Return the number of edges in the graph"""
        # go through each vertex in the graph, and get the size of the incidence map
        total = sum(len(self._outgoing[v]) for v in self._outgoing)

        # an undirected graph maeans that the edges points both ways do don't double count the incoming and outcoming
        return total if self.is_directed() else total // 2

    def edges(self):
        """Return a set of all edges of the graph."""
        result = set() # prevents any double counting due to undirected graphs
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values()) # means up updating of a set
            # an undirected graph would have _outgoing double counting but because we've used set, that prevents any upddates
        return result
    
    def get_edge(self, u, v):
        """Return the edge from u to v, or Nont if not adjacent."""
        # Go to the u vertex in the outgoing map
        return self._outgoing[u].get(v)

    def degree(self, v, outgoing=True):
        """Return number of (outgoing) edges incident to vertex v in the graph
        
        If the graph is directed, optional paramter used to count incoming edges
        """
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])

    def incident_edges(self, v, outgoing=True):
        """
        Return all (outgoing_ edges incident to vertex v in the graph.
        
        If graph is directed, optional paramter used to request incoming edges
        """
        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[v].values():
            yield edge
        
    def insert_vertex(self, x=None):
        """Insert and return a new Vertex with element x."""
        v = self.Vertex(x) # v stores the information, 
        # Remember that _outgoing is a top-level dictionary 
        self._outgoing[v] = {} # Create the incidence collection
        if self.is_directed():
            self._incoming[v] = {} # will need a distinct map for incoming edges too
        return v

    def insert_edge(self, u, v, x=None):
        """Insert and return a new Edge from u to v with auxiliary element x."""
        e = self.Edge(u, v, x)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e