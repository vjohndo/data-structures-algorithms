def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    
    hash_table = {}
    
    for index, num in enumerate(nums):
        
        print(hash_table)

        if num in hash_table:
            return [hash_table[num], index]
        
        hash_table[target-num] = index
            

print(twoSum([2,7,11,15],9))

