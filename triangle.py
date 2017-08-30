# Leetcode: https://leetcode.com/problems/triangle/description/
# Very similar to the DP on chessboard / going down and right. The trick is, the only indexes
# you can compare to is (i) and (i - 1). Go through the triangle and that's apparent
# I keep making slow implementations, I think my first pass in making dp is slow.

class Solution(object):
    
    def isValid(self, i, size):
        return (i >= 0 and i < size)
    
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        
        if (not triangle):
            return 0
        
        dp = [[] for x in range(len(triangle))]
        
        for i in range(len(triangle)):
            dp[i] = [False for y in range(len(triangle[i]))]

        dp[0][0] = triangle[0][0]
        
        for i in range(1, len(dp)):
            for j in range(len(dp[i])):
                
                row_above = len(dp[i - 1])          # Length of the row above
                left = sys.maxint
                right = sys.maxint
                
                if (self.isValid(j - 1, row_above)):
                    left = dp[i - 1][j - 1]
                
                if (self.isValid(j, row_above)):
                    right = dp[i - 1][j]
                
                dp[i][j] = min(left + triangle[i][j], right + triangle[i][j])
        
        return min(dp[len(dp) - 1])
        
