# Leetcode: https://leetcode.com/problems/number-of-longest-increasing-subsequence/description/
# This is a bit trickier than the ordinary, you have to keep track of how many WAYS to create the max
# length subsequence. Beats 80%

"""
Example input:
[1, 3, 5, 4, 7]
[1, 2, 3, 3, 4]   DP list
[1, 1, 1, 1, 2]   WAYS list
"""

class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if (not nums): return 0
        
        dp = [1] * len(nums)            # Standard DP (max subsequence up til this point)
        ways = [1] * len(nums)          # How many combinations can reach this length (this is the important part)
        
        for i in range(len(nums)):
            for j in range(0, i):
                if (nums[i] > nums[j]):
                    if (dp[j] + 1 > dp[i]):
                        dp[i] = dp[j] + 1
                        ways[i] = ways[j]
                    elif (dp[j] + 1 == dp[i]):
                        ways[i] += ways[j] 
        
        max_dp = max(dp)
        count = 0
        for i in range(len(dp)):
            if (dp[i] == max_dp):
                count += ways[i]
        
        return count
