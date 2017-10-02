# Leetcode: https://leetcode.com/problems/rotate-array/description/
# The hard part of this question is finding the trick, which is to reverse the two portions. Then do a total reverse
# Also watch out for edge cases with k > len(nums), beats 95%

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = (k % len(nums)) 
        self.reverse(nums, 0, len(nums) - k - 1)
        self.reverse(nums, len(nums) - k, len(nums) - 1)
        self.reverse(nums, 0, len(nums) - 1)
        
    def reverse(self, nums, start, end):
        
        while (end > start):
            nums[start], nums[end] = nums[end], nums[start]
            end -= 1
            start += 1
