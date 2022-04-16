from typing import List

def permutations(letters: str) -> List[str]:
    
    def dfs(path, used, res): # sure i need something else
        # Check if solution and report
        if len(path) == len(letters):
            res.append("".join(path))
            return
        
        # Iterate through options
        for i, letter in enumerate(letters):
            # Check if solution is workable
            if used[i]:
                continue
            
            # Add to state 
            path.append(letter)
            used[i] = True
            
            # Run DFS
            dfs(path, used, res)
            
            # Backtrack now i.e. remove state
            path.pop() # we do this instead of path + "new part of path" to save memory 
            used[i] = False
        
    
    res = []
    if letters:
        dfs([], [False] * len(letters), res)
    return res
    

if __name__ == '__main__':
    letters = input()
    res = permutations(letters)
    for line in res:
        print(line)
