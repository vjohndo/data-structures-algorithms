def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    
    # Personal attempt 16.17% faster run time, 73.58% less memoery
    # Iterate through the string
    # Keep track of seen characters using a map
    # Keep track of biggest string
    # problem with dvdf... need to account for d vdf f 
    
    substring_list = [] # Tracks largest lengths
    seen_chars = {} # Tracks seens chars
    temp = [] # temp
    index = 0

    while index < len(s):
        print(index)
        char = s[index]
    
        if char in seen_chars:
            substring_list.append(len(temp))
            index = seen_chars[char] # reindex
            temp = []
            seen_chars = {}
        else: 
            seen_chars[char] = index
            temp.append(char)
        
        index += 1
    
    substring_list.append(len(temp)) # As the for loop finishes it doesn't account for the last temp
    max_length = 0
    
    for length in substring_list: 
        if length > max_length:
            max_length = length
            
    return max_length


print(lengthOfLongestSubstring('dvdf'))