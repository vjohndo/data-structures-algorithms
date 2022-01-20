from copy import deepcopy

def floyd_warshall(g):
    """Return a new graph that is the transitive clusre of g."""

    closure = deepcopy(g) # imported from the copy module
    verts = list(closure.vertices()) # make an indexable list
    n = len(verts)
    for k in range(n):
        for i in range(n):
            # verify that the edge (i,k) exists inteh partial closure
            # We also check that i and k are not the same i.e. going cyclically back to itself
            if i != k and closure.get_edge(verts[i], verts[k]) is not None:

                # If i exists, go through all possible combination of j
                for j in range(n):
                    # check that i, j, k are not the same
                    if i != j != k and closure.get_edge(verts[k], verts[j]) is not None:
                        #if (k --> j) exists add an edge (k --> j) , unless it's already in the graph)
                        if closure.get_edge(verts[i], verts[j]) is None:
                            closure.insert_edge(verts[i], verts[j])
    return closure

