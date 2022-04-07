def is_isomorphic(str_1: str, str_2: str) -> bool:
    mapping = {}
    used = set() # character in str_2 already used as value in mapping
    if len(str_1) != len(str_2):
        return False
    for i in range(len(str_1)):
        a_char = str_1[i]
        b_char = str_2[i]
        if a_char in mapping:
            if mapping[a_char] != b_char:
                return False
        else:
            if b_char in used:
                return False
            mapping[a_char] = b_char
            used.add(b_char)
    return True

if __name__ == '__main__':
    str_1 = input()
    str_2 = input()
    res = is_isomorphic(str_1, str_2)
    print('true' if res else 'false')