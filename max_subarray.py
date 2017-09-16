# Leetcode: https://leetcode.com/problems/maximum-subarray/description/
# Pretty straight forward DP, not as challenging as the multiplication form
# Not sure how this can be faster, only beats 20%? Does internet speed affect this?

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sub = nums[:]
        cur_max = max_sub[0]
        
        for i in range(1, len(nums)):
            max_sub[i] = max(max_sub[i - 1] + nums[i], max_sub[i])
            cur_max = max(cur_max, max_sub[i])
        
        return cur_max
