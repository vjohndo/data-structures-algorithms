from typing import List

KEYBOARD = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}

def letter_combinations_of_phone_number(digits: str) -> List[str]:
    def dfs(path, res):
        if len(path) == len(digits):
            res.append("".join(path))
            return
        
        next_number = digits[len(path)]
        for letter in KEYBOARD[next_number]:
            path.append(letter)
            dfs(path, res)
            path.pop()
    
    res = []
    dfs([], res)
    return res

if __name__ == '__main__':
    digits = input()
    res = letter_combinations_of_phone_number(digits)
    print(' '.join(res))


def letter_combinations_of_phone_number(digits: str) -> List[str]:
    """ MY OWN BLIND IMPLEMENTATION"""
    # Instead of passing through index, we can calcaulte where we're upto using index 
    def dfs(path, res, index):
        if len(path) == len(digits):
            res.append("".join(path))
            return
        
        for char in KEYBOARD[digits[index]]:
            path.append(char)
            dfs(path, res, index + 1) # Run DFS starting from next index
            path.pop()

    res = []
    if digits:
        dfs([], res, 0)
    return res