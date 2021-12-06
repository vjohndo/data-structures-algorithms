class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        common_prefix = list(strs[0])
        
        for string in strs[1:]:
            
            if len(common_prefix) > len(string):
                common_prefix = common_prefix[0:len(string)]
            
            for (index, char) in enumerate(common_prefix):
                if char != string[index]:
                    common_prefix = common_prefix[0:index]
        
        return "".join(common_prefix)