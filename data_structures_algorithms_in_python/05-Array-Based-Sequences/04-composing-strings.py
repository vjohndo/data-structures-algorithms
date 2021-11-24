document = "AILOUHWDI UANWLI ALIUWND: UANW:DU"

# Inefficient implementation, strings are immutable and unless Python's reference count for "letters" variable is 1, it will be O(n^2)
letters = ''
for c in document: # Each call requires construction of new string. 1, 2, 3, 4 + ... + n ==> n(n-1)/2
    if c.isalpha():
        letters += c 


# Guaranteed linear implementation of this. 
temp = []
for c in document: # O(n)
    if c.isalpha(): # O(1)
        temp.append(c) # O(1)

letters = "".join(temp) # O(n)


# implemetnation usling list comp
letters = "".join( [c for c in document if c.isalpha()] )

