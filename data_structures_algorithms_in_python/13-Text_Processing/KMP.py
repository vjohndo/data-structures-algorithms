def find_kmp(T, P):
    """Return the lowest index of T at which substring P beings (or else -1)"""
    n, m = len(T), len(P)
    if m == 0:
        return 0
    
    fail = compute_kmp_fail(P)
    j = 0 # index for text
    k = 0 # index for patten

    while j < n:
        if T[j] == P[k]:
            if k == m - 1:
                # end character we are at in the Text less the length of the pattern
                # since j is an index not a length, need to + 1 (m is an index)
                return j - m + 1

            j += 1
            k += 1

        elif k > 0:
            # otherwise no match and we've checked at least one character
            # reuse suffix of P[0:k] i.e. we hit a mismatch, look back the suffix, can we reuse it?
            k = fail[k-1]
        else:
            # Otherwise still no match and mismatch on first char, no suffice to reuse
            # k still = 0
            j += 1
    return -1

def compute_kmp_fail(P):
    """Utility that computes and retusn KMP 'fail' list"""
    m = len(P)
    fail = [0] * m # assume an overlap of zero everywhere
    j = 1 # Suffix marker
    k = 0 # Prefix marker

    while j < m:
        if P[j] == P[k]:
            fail[j] = k + 1
            j += 1
            k += 1
        elif k > 0:
            # k followsing a matching prefix,
            # we need to set k back to previous element
            k = fail[k-1]
        else:
            j += 1 # Progress the suffix marker until we find a suffix matching the prefix 
    
    return fail