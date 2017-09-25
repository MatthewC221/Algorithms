# Leetcode: https://leetcode.com/problems/array-nesting/description/
# I TLE'd on this my first try (it was O(n^2) initially) as I was starting at each node and finding each cycle
# This is not required because if you're jumping into an old set the current node would've been considered.

class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_size = 0
        
        # Go through each number and try to find nesting
        for i in range(len(nums)):
            count = 0
            j = i
            while (nums[j] >= 0):
                nxt = nums[j]
                nums[j] = -1
                j = nxt
                count += 1
            max_size = max(max_size, count)                         
        
        return max_size
