# Leetcode: https://leetcode.com/problems/perfect-squares/description/
# DP with a little twist. Not sure if this is the best speed. Time complexity = O(n * sqrt(n))
# O(n * sqrt(n)) because sqrt(n) will be the size of the squares array. Space complexity: O(n)

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # DP
        squares = []
        start = 1
        
        # Create square list as long as <= n
        # E.g. for n = 13, squares=[1,4,9]
        # For n = 16, squares=[1,4,9,16]
        
        while (start*start <= n):
            squares.append(start*start)
            start += 1
        
        # Basically coin problem
        dp = [sys.maxint] * (n + 1)
        dp[0] = 0
        for i in xrange(len(dp)):
            for j in xrange(len(squares)):
                if (i - squares[j] >= 0):
                    dp[i] = min(dp[i], dp[i - squares[j]] + 1)
        
        return dp[-1]
        
