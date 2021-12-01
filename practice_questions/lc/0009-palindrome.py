class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if x < 0:
            return False
        
        x_str = str(x)
        
        for i in range(x):
            if x_str[i] == x_str[-i-1]:
                return True
        
        return False

    def isPalindrome2(self,x):
        if x < 0:
            return False

        