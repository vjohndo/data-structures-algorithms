def wordFreq(filename):
    freq = {}
    for piece in open(filename).read().lower().split(): # Split by default splits on space
        # Only consider alphabetic characters within this piece
        word = ''.join(c for c in piece if c.isalpha()) # isalpha returns true if all chars are a-z
        if word: # Require at least one alphabetic character
            freq[word] = 1 + freq.get(word, 0) # get returns word, otherwise defaults to 0

    max_word = ''
    max_count = 0
    for (w,c) in freq.items(): 
        if c > max_count:
            max_word = w
            max_count = c

    print('The most frequent word is', max_word)
    print('Its number of occurences is', max_count)

