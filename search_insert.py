# Leetcode: https://leetcode.com/problems/search-insert-position/description/
# Binary search with twist, be wary of edge cases. In the binary search, where you would normally exit
# if not found, such as line 26 return that index. (the higher one).
# E.g: [1, 5, 7, 9], looking for 6. Low and high will be [5, 7] therefore return index of 7

# Beats 85%

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        # Do bin search, if it's not found. Use the last indexes
        if not nums: return 0
        
        if (target < nums[0]): return 0
        if (target > nums[-1]): return len(nums)
        if (target == nums[0]): return 0
    
        low = 0
        high = len(nums) - 1
        
        while (low < high):
            mid = (low + high) / 2
            print nums[mid]
            if (nums[mid] == target): return mid
            else:
                if (low + 1 == high): return high
                if (nums[mid] > target): high = mid
                elif (nums[mid] < target): low = mid
        
        return -1
