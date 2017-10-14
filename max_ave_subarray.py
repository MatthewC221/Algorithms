# Leetcode: https://leetcode.com/problems/maximum-average-subarray-i/description/
# Max subarray O(n), very straight forward. The average doesn't need to be included until the very end (division is pretty
# expensive computationally). Just find the largest window sum of len = k

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if not nums: return float(0)
        
        # Window of length k (slide the window)
        mx = sum(nums[:k])
        cur = mx
        for i in xrange(k, len(nums)):
            cur += nums[i] - nums[i - k]
            mx = max(mx, cur)
        
        return (float(mx) / k)
