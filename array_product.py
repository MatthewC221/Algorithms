# Leetcode: https://leetcode.com/problems/product-of-array-except-self/description/
# This is actually pretty tricky, it took me a while to get this. Not in-place (advantages of using division)

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p = 1
        res = [0] * len(nums)
        for i in xrange(len(nums)):
            res[i] = p
            p *= nums[i]
        
        p = 1
        for i in xrange(len(nums) - 1, -1, -1):
            res[i] *= p
            p *= nums[i]
        
        return res
