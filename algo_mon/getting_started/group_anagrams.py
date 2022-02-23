from typing import List

def group_anagrams(strs: List[str]) -> List[List[str]]:
    anagram_map = {}
    
    for str in sorted(strs):
        anagram_key = "".join(sorted(str))
        if anagram_key in anagram_map:
            anagram_map[anagram_key].append(str)
        else:
            anagram_map[anagram_key] = [str]
                
    return list(anagram_map.values())