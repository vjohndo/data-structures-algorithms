class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500, 
            "M": 1000
        }
        
        total = 0
        prev = s[0]
        
        for numeral in s: 
            
            if values[prev] >= values[numeral]:
                total += values[numeral]
            else:
                total += values[numeral] - 2*values[prev]
            
            prev = numeral
        
        return total
    
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500, 
            "M": 1000
        }
        
        total = 0
        
        for i in range(len(s) - 1): 
            
            if values[s[i]] < values[s[i+1]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]
        
        return total + values[s[-1]]