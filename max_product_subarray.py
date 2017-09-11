# Leetcode: https://leetcode.com/problems/maximum-product-subarray/description/
# Definitely trickier than max subarray, the difficult thing is thinking of negatives. e.g. [2, 3, -2, -2]
# A good choice is to keep track of the minimum, that way as you go really negative e.g. -12 from above
# You'll always have that number.

# You could also look ahead but this ruins the O(n) approach

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        max_arr = [0] * len(nums)
        min_arr = [0] * len(nums)
        max_arr[0] = min_arr[0] = nums[0]
        
        for i in range(1, len(nums)):
            max_arr[i] = min_arr[i] = nums[i]
            min_arr[i] = min(min(max_arr[i - 1] * nums[i], min_arr[i - 1] * nums[i]), nums[i]);
            max_arr[i] = max(max(max_arr[i - 1] * nums[i], min_arr[i - 1] * nums[i]), nums[i]);
        
        return max(max(max_arr), max(min_arr))
            
