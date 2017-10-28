# Leetcode: https://leetcode.com/problems/decode-ways/description/
# DP is the solution that won't TLE. Much better than BFS obviously
# However you have to do checks for valid double digits!

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        if (len(s) == 1): return 1 if s[0] != '0' else 0
        
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0
        
        for i in xrange(2, len(s) + 1):
            single = int(s[i-1:i])
            double = int(s[i-2:i])
            
            if (single >= 1 and single <= 9):
                dp[i] += dp[i - 1]
            
            if (double >= 10 and double <= 26):
                dp[i] += dp[i - 2]
        
        return dp[-1]

"""
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Can do a BFS, each time either pop the first element or the first two elements
        # Also seen as, how many ways can we partition N into 1s and 2s
        # Need to check if it's valid too (29 is not valid)
        
        if not s: return 0
        
        count = 0
        queue = [(list(s))]
        while queue:
            cur = queue.pop()
            if (len(cur) == 0): 
                count += 1
            else:
                pop_1 = cur[:]
                pop_2 = cur[:]

                if (len(pop_1)): 
                    n = int(pop_1.pop())
                    if (n > 0): queue.append(pop_1)

                if (len(pop_2) > 1): 
                    num = int(pop_2[-2]) * 10 + int(pop_2[-1])
                    if (num < 27 and int(pop_2[-2]) > 0):
                        pop_2.pop()
                        pop_2.pop()
                        queue.append(pop_2)
                        
        return count
"""
  
