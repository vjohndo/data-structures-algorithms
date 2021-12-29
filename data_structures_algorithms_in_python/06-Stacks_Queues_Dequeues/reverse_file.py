from array_stack import ArrayStack

def reverse_file(filename):
    """Overwrite given file with its contents line-by-line reversed"""

    S = ArrayStack()
    original = open(filename) # opens the file and returns a file object. default mode is "r" for read
    for line in original: # Go through each line 
        S.push(line.rstrip('\n')) # Push each line into the Stack and with "rstrip" remove all trailing characters, in this case it will be '\n'
        # strip the new line just in case the final line doesn't have it. We can add it in ourselves at the end

    original.close() 

    output = open(filename, 'w') # Reopen files and overwrites the original with "w" for writing
    while not S.is_empty(): # keep going through the stack until it's empty
        output.write(S.pop() + '\n')

    output.close()

