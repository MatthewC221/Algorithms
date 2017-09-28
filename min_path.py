# Leetcode: https://leetcode.com/problems/minimum-path-sum/description/
# I feel like I've done this before somewhere else (on a chessboard?), not sure it was on LC so

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for x in xrange(n)] for y in xrange(m)]
        
        dp[0][0] = grid[0][0]
        
        for i in xrange(1, n):
            dp[0][i] = dp[0][i - 1] + grid[0][i]
        
        for i in xrange(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
            
        for i in xrange(1, m):
            for j in xrange(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1])
                dp[i][j] += grid[i][j]
        
        return dp[m - 1][n - 1]
