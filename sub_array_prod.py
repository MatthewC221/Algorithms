# Leetcode: https://leetcode.com/problems/subarray-product-less-than-k/description/ 
# This is pretty hard to think about, I first made the O(n^2) solution with O(n) space, however the passing solution
# is O(n) time and O(1) space. Refer to the commented code

class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        # Similar to contiguous subarray sum
        # TLE on O(n^2)
        # [10, 5, 2, -1, 6] -> [1, 10, 50, 100, -100, 600]
        # Initialise first element to 1
        if not nums: return 0
        
        mult = [1] * (len(nums) + 1)
        
        cur = 1
        for i in xrange(len(nums)):
            cur *= nums[i]
            mult[i+1] = cur
        
        # O(n^2)
        ret = []
        count = 0
        
        for i in xrange(1, len(mult)):
            for j in xrange(i):
                if (mult[i] / mult[j] < k): count += 1
        
        return count

"""
        if not nums: return 0
        if k < 2: return 0
        
        count = 0
        cur = 1
        j = 0
        
        for i in xrange(len(nums)):
            cur *= nums[i]
            while (j < len(nums) and cur >= k):
                cur = cur / nums[j]
                j += 1
            count += i - j + 1
        
        return count
"""
  
