# Leetcode: https://leetcode.com/problems/search-for-a-range/description/
# The mistake I made was setting high = len(nums) - 1, when it should be len(nums)
# Do a binary search for all three (start, middle and end). The bounds are changed to optimise

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """        
        
        low = 0
        high = len(nums)
        index = -1
        start = -1
        end = -1
        
        # Find number (regardless of range)
        while (low < high):
            med = (low + high) / 2
            if (nums[med] == target):
                index = med 
                break
            elif (low + 1 == high):
                break
            elif (nums[med] > target):
                high = med
            elif (nums[med] < target):
                low = med
        
        if (index < 0): return [start, end]
        
        # Use the range before to narrow the bounds, bin search for start
        high = index + 1
        low = 0
        
        while (low < high):
            med = (low + high) / 2
            if (nums[med] == target):
                if (med == 0 or nums[med - 1] != target):
                    start = med 
                    break
                else:
                    high = med
            elif (nums[med] > target):
                high = med
            elif (nums[med] < target):
                low = med            
        
        # Use the range before to bin search for end
        high = len(nums)
        low = index
        
        while (low < high):
            med = (low + high) / 2
            if (nums[med] == target):
                if (med == len(nums) - 1 or nums[med + 1] != target):
                    end = med 
                    break
                else:
                    low = med
            elif (nums[med] > target):
                high = med
            elif (nums[med] < target):
                low = med
        
        return [start, end]
