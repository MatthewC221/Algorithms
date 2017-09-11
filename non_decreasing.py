# Leetcode: https://leetcode.com/problems/non-decreasing-array/description/
# This leetcode easy has a 20% success rate, it's tricky if you don't draw it down.
# I thought not copying the array would save time but apparently not (I tried a different implementation)

class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        first, second = nums[:], nums[:]
        for i in range(len(nums) - 1):
            if (nums[i] > nums[i + 1]):
                first[i] = nums[i + 1]
                second[i + 1] = nums[i]
                break
        
        count = 0
        for i in range(len(nums) - 1):
            if (first[i] > first[i + 1]):
                count += 1
            if (second[i] > second[i + 1]):
                count += 1
            
            if (count >= 2):
                return False
        
        return True
