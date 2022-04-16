from typing import List

def partition(s: str) -> List[List[str]]:
    res = []
    n = len(s)
    
    def is_palindrome(word):
        return word == word[::-1]
    
    def dfs(start, path):
        if start == n:
            res.append(path[:])
            return
        
        # Go through each item
        for i in range(start + 1, n + 1):
            # test the prefix e.g. a, aa, aaa, aaaa 
            prefix = s[start : i]
            
            # The prefix is palindrome, run dfs (we otherwise "prune" the response if its not a palindrome)
            if is_palindrome(prefix):
                dfs(i, path + [prefix])
                
    dfs(0, [])
    return res

if __name__ == '__main__':
    s = input()
    res = partition(s)
    for row in res:
        print(' '.join(row))