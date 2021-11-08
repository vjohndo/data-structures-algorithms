from pythonds3.graphs import Graph

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