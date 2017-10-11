# Leetcode: https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/
# Beats 93%, pretty straight forward. I thought it was subsequence problem at first so this is actually new. 
# One thing to keep in mind is the last (mx = max(mx, cur_win)), if nums is strictly increasing you need to 
# compare at some point.

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Not a DP problem, just keep the window running
        # O(n) solution
        
        if not nums: return 0
        mx = 1
        cur_win = 1
        
        for i in xrange(1, len(nums)):
            if (nums[i] > nums[i - 1]):
                cur_win += 1
            else:
                mx = max(mx, cur_win)
                cur_win = 1
            
        mx = max(mx, cur_win)
        
        return mx
        
        
