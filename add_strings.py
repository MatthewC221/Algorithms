# Leetcode: https://leetcode.com/problems/add-strings/description/
# Same as add binary, definitely could save time with the reverses and the check limits
# But solution is elegant

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        # O(n) operation
        
        num1 = num1[::-1]
        num2 = num2[::-1]
        overflow = 0
        ret = ""
        
        for i in range(max(len(num1), len(num2))):
            n = overflow
            if (i < len(num1)): n += int(num1[i])
            if (i < len(num2)): n += int(num2[i])
            
            if (n > 9):
                n -= 10
                overflow = 1
            else:
                overflow = 0        
            ret += str(n)
        
        if (overflow): ret += "1"
        
        return ret[::-1]
