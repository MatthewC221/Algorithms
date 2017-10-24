# Leetcode: https://leetcode.com/problems/valid-parenthesis-string/description/
# This TLE'd, I had to refer to the solutions for the right answer. The optimal answer is
# O(n).

# It comes from the fact that if we observe the nums array it is a range of consecutive ints only
# For example: [1] -> * -> [0, 1, 2]
# Therefore we only include low and high

class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        # Left bracket = +1, start = -1, +1, +0, right bracket = -1
        # Aiming for 0 at the end, almost like a BFS
        # Can't have negatives, consider: [)], this can't be closed ever
        
        if not s: return True
        num = [0]
        
        for i in xrange(len(s)):
            if (s[i] == '('):
                for i in xrange(len(num)): num[i] += 1
            elif (s[i] == ')'):
                num = self.fillRight(num)
            else:
                num = self.fillStar(num)
        
        for val in num: 
            if val == 0: return True
        
        return False
        
    def fillRight(self, num):
        
        new = []
        for i in xrange(len(num)):
            if (num[i] - 1 >= 0): new.append(num[i] - 1)
        
        return new
    
    def fillStar(self, num):
        
        new = []
        for i in xrange(len(num)):
            new.append(num[i])
            new.append(num[i] + 1)
            if (num[i] - 1 >= 0): new.append(num[i] - 1)
        
        return new
            
            
