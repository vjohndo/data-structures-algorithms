from re import L
from base.HeapPriorityQueue import HeapPriorityQueue

class Partition:
    pass

def MST_Kruskal(g):
    """Compute a minimum spanning tree of a graph using Kruskal's algorithm.
    
    Return a list of edges that comprise the MST.

    The elmeents ofthe graph's edges are assumed to weights
    """
    tree = []
    pq = HeapPriorityQueue() # don't need to adjust hte netires in the queue
    forest = Partition() # Partitions will be defined later and they keep track of forest clusters
    position = {} # map each not to its Partition entry

    for v in g.vertices():
        # go through each vertice in the graph and make them a Partition
        position[v] = forest.make_group(v)

    for e in g.edges():
        pq.add(e.element(), e) # edge's element is assumed to be its weight

    size = g.vertex_count()

    while len(tree) != size - 1 and not pq.is_empty():
        # Tree not spanning and unprocessed edges remain
        weight, edge = pq.remove_min()
        u,v = edge.endpoints()
        a = forest.find(position[u])
        b = forest.find(position[v])

        if a != b:
            tree.append(edge)
            forest.union(a, b)

    return tree