# Sliding Window Patten

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


def lengthOfLongestSubstring2(s):

        # Runtime: 60 ms, faster than 49.84% of Python online submissions for Longest Substring Without Repeating Characters.
        # Memory Usage: 13.5 MB, less than 97.20% of Python online submissions for Longest Substring Without Repeating Characters.
        
        if len(s) <= 0:
            return 0
        
        if len(s) == 1:
            return 1
        
        
        start_index = 0
        end_index = 1
        seen_chars = {s[0]: 0}
        max_length = 0
        
        
        while end_index < len(s):
            # Check if that you've seen this before
            # If you have move the next index after, there may be inbetween chars not yet accounted for
            # Let's check if that index is less than our starting index

            if (s[end_index] in seen_chars) and (seen_chars[s[end_index]] >= start_index):
                start_index = seen_chars[s[end_index]] + 1
                print(s[start_index:end_index + 1])
            
            seen_chars[s[end_index]] = end_index

            end_index += 1
            
            if end_index - start_index > max_length:
                
                max_length = end_index - start_index

            
        
        return max_length


# Runtime: 52 ms, faster than 63.94% of Python online submissions for Longest Substring Without Repeating Characters. 
# Memory Usage: 13.7 MB, less than 58.88% of Python online submissions for Longest Substring Without Repeating Characters.

def lengthOfLongestSubstring3(s):
    if len(s) <= 0:
            return 0
        
    if len(s) == 1:
        return 1

    last_index = {}
    max_length = 0
    start_index = 0

    for current_index, current_char in enumerate(s):

        # If we've seen this character before, update the starting index
        if current_char in last_index:
            start_index = max(start_index, last_index[current_char] + 1)

        # Update to the latest last index
        last_index[current_char] = current_index

        # update the max length if there's space
        max_length = max(max_length, current_index - start_index + 1)

    return max_length

print(lengthOfLongestSubstring3('dvdf'))
