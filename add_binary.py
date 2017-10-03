# Leetcode: https://leetcode.com/problems/add-binary/description/
# Annoying to work with so I reversed 
# Beats 75%, can be faster if we didnt check length that many times, but reduces elegancy

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        a = a[::-1]
        b = b[::-1]
        overflow = 0
        ret = ""
        for i in range(0, max(len(a), len(b))):
            n = overflow
            if (i < len(a)): n += int(a[i])
            if (i < len(b)): n += int(b[i])
            if (n > 1):
                overflow = 1
                n -= 2
            else:
                overflow = 0
            ret += str(n)
        
        if (overflow):
            ret += str(1)
            
        return ret[::-1]
        
        
