from typing import List

def word_break(s: str, words: List[str]) -> bool:
    
    def dfs(i):
        """Where i for index will rep which characters left to be matched"""
        if i == len(s):
            # We've found a matching word
            return True
        
        for word in words:
            if s[i:].startswith(word):
                if dfs(i+len(word)):
                    return True
                
        # Otherwise return false
        return False
    
    return dfs(0)

if __name__ == '__main__':
    s = input()
    words = input().split()
    res = word_break(s, words)
    print('true' if res else 'false')

## Implementation with memoisation
def word_break(s: str, words: List[str]) -> bool:
    # Need to pass down the path somehow
    
    memo = {}
    
    def dfs(i):
        if i == len(s):
            return True
        
        if i in memo:
            return memo[i]
        
        
        ok = False # set okayness to False before proving it to be true
        for word in words:
            if s[i:].startswith(word):
                # If the path leads to true, okay
                if dfs(i+len(word)):
                    ok = True
                    break # Need to break to get out of any fursther dfs
        
        memo[i] = ok
        return ok
    
    return dfs(0)
