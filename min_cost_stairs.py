# Leetcode: https://leetcode.com/problems/min-cost-climbing-stairs/description/
# Pretty easy DP question, difference is they use "costs", so I guess the trick is to 
# initialise steps 0 and 1 as 0.

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # DP problem but slightly spicer
        # Subproblem is, cheapest it took to reach this step (which is either 1 or 2 steps below)
        dp = [-1] * (len(cost) + 1)
        dp[0] = 0
        dp[1] = 0
        
        for i in xrange(2, len(cost) + 1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        
        return dp[-1]
        
