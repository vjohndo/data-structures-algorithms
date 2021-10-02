def hash_str(a_string, table_size):
    """Simple hash function for a string"""
    return sum([ord(char) for char in a_string]) % table_size


class HashTable:
    """ Implementation of hash table """
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size     #Holds key items
        self.data = [None] * self.size      #Holds the datavalue
    
    def hash_function(self, key, size):
        return key % size

    def rehash(self, old_hash, size):
        return (old_hash + 1) % size        # Linear probing
    
    def put(self, key, data):
        # Hash the key to get to right slot and add data.
        # Need to account for collisions and key already in hash table
        hash_value = self.hash_function(key, len(self.slots))           # Generate hash to know where to store in table... note than in python len(iterable) is O(1)

        if self.slots[hash_value] is None:                              # If the slot is empty, this is the correct spot
            self.slots[hash_value] = key                                # Add in the key
            self.data[hash_value] = data                                # Add in the data using the hash_value

        else:                                                           # Else we'll need to rehash and/or check for key already in table
            if self.slots[hash_value] == key:                           # If key is the same, we are replacing the data
                self.data[hash_value] = data
            else:                                                       # Otherwise, this is a collision and need to rehash
                start_slot = self.slots[hash_value]
                next_slot = self.rehash(hash_value, len(self.slots))    # Determine next slot... note than in python len(iterable) is O(1)
                                                                        # Need to add code to account for no empty slots left.
                while (                                                 # So long as the rehashed slot is not empty or we've not hit a matching key keep rehashing
                    self.slots[next_slot] is not None
                    and self.slots[next_slot] != key
                    and self.slots[next_slot] != start_slot
                ):
                    next_slot = self.rehash(next_slot, len(self.slots))

                if self.slots[next_slot] is None:                       # Must be the case the slot is empty, set new key and data
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                elif self.slots[next_slot] == key:
                    self.data[next_slot] = data                         # Must be the case this slot has a matching key
                else:
                    raise KeyError("HashTable is Full")

    def get(self, key):
        start_slot = self.hash_function(key, len(self.slots)) #start by hashing the key and seeing if there's anything in the table 

        position = start_slot
        while self.slots[position] is not None:
            if self.slots[position] == key:
                return self.data[position]
            
            
            else: # else need to rehash until empty
                position = self.rehash(position, len(self.slots))
                if position == start_slot:
                    return None

    def __getitem__(self,key):
        return self.get(key)
    
    def __setitem__(self,key,data):
        self.put(key,data)


h = HashTable()
h[54] = "cat"
h[26] = "dog"
h[93] = "lion"
h[17] = "tiger"
h[77] = "bird"
h[31] = "cow"
h[44] = "goat"
h[55] = "pig"
h[20] = "chicken"

# Check if full hash table error is raised properly
# h[30] = "human"
# h[29] = "alpha" 
# h[99] = "erroid"

print(h.slots)
print(h.data)
print(h[20])
print(h[17])
h[20] = "duck"
print(h[20])
print(h[99])
print(h.data)