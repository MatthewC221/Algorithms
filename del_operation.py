# Leetcode: https://leetcode.com/problems/delete-operation-for-two-strings/description/
# This is the LCS DP problem, I had to revise it quickly.
# Slight variation that you have to subtract the max LCS

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        
        if (m == 0):
            return len(word2)
        elif (n == 0):
            return len(word1)
        
        dp = [[0 for x in xrange(m + 1)] for y in xrange(n + 1)] 
        
        for i in range(n):
            for j in range(m):
                num = -1
                if (word1[j] == word2[i]):
                    num = dp[i][j] + 1
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j], num)
        
        delete = dp[n][m]
        return (m - delete) + (n - delete)
