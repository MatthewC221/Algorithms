# Leetcode: https://leetcode.com/problems/single-number/description/
# Using XOR to find the missing number, doesn't work well if there is no missing number!

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        ret = 0
        for i in range(len(nums)):
            ret ^= nums[i]
        
        # OR 
        # Put all elements in the dict, constantly delete them / set them to
        # complete, recheck the dict
        
        return ret
