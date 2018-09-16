# Leetcode: https://leetcode.com/problems/reordered-power-of-2/description/
# Honestly pretty straight forward, not super efficient (conversions from int to string)
# Looked kinda clean so yeah

class Solution(object):
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        # Make a string interpretation of pow2s
        # 46 = 0,0,0,0,1,0,1,0,0,0. Won't even need the commas tbh (no power of 2 has 10 or more of one digit)
        # Could optimise first by generating power of 2 to the highest possible value of N
        
        start = 1
        seen = {}
        
        while start < pow(10, 9):
            seen[self.getStringFromNum(start)] = True
            start *= 2
        
        return seen.get(self.getStringFromNum(N), False)
            
    def getStringFromNum(self, num):
        lst = [0] * 10
        while num >= 1:
            val = num % 10
            lst[val] += 1
            num /= 10
        
        return ''.join(str(e) for e in lst)
            
        
