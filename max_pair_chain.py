# Leetcode: https://leetcode.com/problems/maximum-length-of-pair-chain/description/
# I TLE'd on my dp O(n^2) version, however apparently a Java one passed. I assume I was really close to passing.
# This problem is actually a greedy problem after sorting. I should've realised this.

class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        
        before = -sys.maxint
        res = 0
        pairs = sorted(pairs, key=lambda x: x[1])
        
        for now in pairs:
            if (now[0] > before):
                before, res = now[1], res + 1
                        
        return res
        
        
