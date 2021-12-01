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

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Want to pass through 0 as an palindrome, anything ending in 0 can never be palindrom
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        # Start a reverse palindrom at 0
        y = 0
        
        # We're interested in running the loop until the reverse 'y' is > x
        while x >= y:
            y = (y * 10) + (x % 10)
            # Check after adding reversed number (even palindrom)
            if x == y:
                return True
            x = (x // 10)
            # Check after removing middle palindrome (odd integered)
            if x == y:
                return True
    
        return False
        