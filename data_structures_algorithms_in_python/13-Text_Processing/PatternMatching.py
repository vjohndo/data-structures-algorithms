def find_brute(T, P):
    """Return the lowest index of T at which substring P beings (or else -1)."""
    n, m = len(T), len(P)
    # Try every potential starting index within t 
    for i in range(n - m + 1):  # (notice how we set up the range to only pick valid starting indexes, but need to account for range printing upto but not inluding last digit)
        k = 0
        # iterate through to match the kth index of P (i.e. until it does not exceed m)
        while k < m and T[i + k] == P[k]:
            k += 1
        # eventually the while loop will end and if it so happens to be the end of the P string
        if k == m:
            return i # subtring mathces on T[i:i+m]

    return -1

def find_boyer_moore(T, P):
    """Return the lowest index of T at which substring P beings (or else -1)"""
    n, m = len(T), len(P)
    if m == 0:
        return 0 # Trivial search for empty string

    last = {}
    for k in range(m):
        last[P[k]] = k # Go through and create a map of the last (rightmost occurence of c)

    # align end of pattern at index m-1 of text
    # remember that we are comparing from the right 
    i = m - 1
    k = m - 1 # k walks P, always 0 <= k < p

    while i < n:
        if T[i] == P[k]:
            if k == 0:
                return i
            else:
                i -= 1
                k -= 1
        else:
            j = last.get(T[i], -1) 
            # find the mismtached index j in P, it could be the case that k is less than j (i.e. the matching index is to the right)
            # We have a case for when (j-1) > k i.e. if a matching index is to the left of k (or if no matching index exists)
            #   ---> if the j is still less than k or not there bigger skip
            #   ---> if the j is greater than k --> mini skip

            
            # Possible step back options 
            # j can be -1 (i.e. the match ) --> if no matching char, full skip with no step back (j-1) = 0
            # j can be some value 0 <= j < m --> if there is a matchking char, full skip and step back to matching index
            # k will be the (number of things we've checked -1) --> full skip, and step back until just after mismatched index
            # Notice how the max skip always takes precendence in the case analysis
                # i.e. check for FULL SKIP, then matched skip, then min skip
            # We take the max skip possible, i.e. the min of the (step back options)

            i += m - min(k, j+1) 
            #   k ==> move the alignment up for full length and shift back for the number of items already checked, 
            #                   --> Case(b) mismatch has already passed, move the index such that the left most checked value is just beyond the msmatched alignment
            #   j + 1 ==> move the alignment up for full length and shift back such that the mismatched character lines up with jth index,
            #   otherindex + 1... where otherindex can be -1) , 
            #                   --> if the mismatch if not at all in P, move aligment up by m and step back 0 times as i was not in the string
            #                       --> remember that i refers to the end of the string, this movement will have it so that hte first char of P will be infront of the mismatched char in T
            #                   --> if the mismatch is in P but less than k, will 
            #                       --> If j is not -1, it will step back enough so that the mismatched index of T lands on the jth index
            # )
            
            k = m - 1 # restart the case analysis comparison for the sequence P
    
    return -1 # could not find it

